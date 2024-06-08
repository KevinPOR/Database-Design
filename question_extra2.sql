-- extra 2 For each region which his the best ranked country for 2019? And what is that rank? (region, country,rank)

SELECT region, country_name, rank as best_rank_2019 

FROM country join happiness USING (country_name) 

WHERE ((year = 2019) and  (region, rank) IN (SELECT region, min(rank) as best 

                                             FROM country join happiness USING (country_name) 

                                             WHERE(year=2019) 

                                             GROUP BY region 

                                             ORDER BY region)) 