SELECT year , AVG (happiness_score) as average_happiness 

FROM happiness  

GROUP BY year 

ORDER BY year 