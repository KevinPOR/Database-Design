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

--part2

SELECT year, AVG(happiness_score) as average_happiness 

FROM country JOIN happiness USING(country_name)  

WHERE GDP <= ANY(SELECT GDP  

              FROM country JOIN happiness USING (country_name)  

              GROUP BY country_name  

              ORDER BY GDP ASC  

              LIMIT 10)  

GROUP BY year 

ORDER BY year 

--part3

SELECT year, AVG(happiness_score) as average_happiness  

FROM country JOIN happiness USING(country_name)   

WHERE infant_mortality >= ANY(SELECT infant_mortality 

                 FROM country JOIN happiness USING (country_name)  

                 GROUP BY country_name 

                 ORDER BY infant_mortality DESC 

                 LIMIT 10) 

   

GROUP BY year  

ORDER BY year

--part4

SELECT year, AVG(happiness_score) as average_happiness   

FROM country JOIN happiness USING(country_name)    

 WHERE literacy >= ANY(SELECT literacy 

                  FROM country JOIN happiness USING (country_name)   

                  GROUP BY country_name  

                  ORDER BY literacy DESC  

                  LIMIT 10)  

GROUP BY year   

 ORDER BY year 

--part 5

SELECT year, AVG(happiness_score) as average_happiness   

FROM country JOIN happiness USING(country_name)    

WHERE literacy <= ANY(SELECT literacy 

                 FROM country JOIN happiness USING (country_name)   

                 GROUP BY country_name  

                  ORDER BY literacy ASC  

                  LIMIT 10)  

GROUP BY year   

ORDER BY year 