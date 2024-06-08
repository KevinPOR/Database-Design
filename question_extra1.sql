-- extra 1 What is the average GDP and happiness score for each region? (region, avg_gdp, avg_happiness) 

SELECT region, avg(gdp) as avg_GDP, avg(happiness_score) as avg_happiness 

FROM country join happiness USING (country_name) 

GROUP BY region 

ORDER BY avg_GDP 