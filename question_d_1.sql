--part 1 

SELECT year, AVG(happiness_score) as average_happiness 

FROM country JOIN happiness USING(country_name)  

WHERE GDP >= ANY(SELECT GDP  

              FROM country JOIN happiness USING (country_name)  

              GROUP BY country_name  

              ORDER BY GDP DESC  

              LIMIT 10)  

GROUP BY year 

ORDER BY year 