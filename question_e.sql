--part 1 
SELECT tab2015.country_name,  tab2019.h2019-tab2015.h2015 as improvement 

FROM (SELECT country_name, happiness_score as h2015  

       FROM country JOIN happiness USING (country_name)     

       WHERE (year IN (SELECT  year --this case the minimum year is 2015 

                       FROM  happiness  

                       ORDER BY year  

                       LIMIT 1  ))  

                     ORDER BY country_name) as tab2015  

       JOIN (SELECT country_name, happiness_score as h2019  

                FROM country JOIN happiness USING (country_name)     

               WHERE (year IN (SELECT  year  -- this case the most updated year is 2019 

               		   FROM  happiness  

                 		  Order by year DESC  

                                            LIMIT 1  ))  

       	ORDER BY country_name) as tab2019 ON (tab2015.country_name  	=tab2019.country_name)  

 ORDER BY improvement DESC  

 LIMIT 3 

--part 2

SELECT tab2015.country_name,  tab2019.h2019-tab2015.h2015 as regression 

FROM (SELECT country_name, happiness_score as h2015  

       FROM country JOIN happiness USING (country_name)     

       WHERE (year IN (SELECT  year --this case the minimum year is 2015 

                       FROM  happiness  

                       ORDER BY year  

                       LIMIT 1  ))  

                     ORDER BY country_name) as tab2015  

       JOIN (SELECT country_name, happiness_score as h2019  

                FROM country JOIN happiness USING (country_name)     

               WHERE (year IN (SELECT  year  -- this case the most updated year is 2019 

               		   FROM  happiness  

                 		  Order by year DESC  

                                            LIMIT 1  ))  

       	ORDER BY country_name) as tab2019 ON (tab2015.country_name  	=tab2019.country_name)  

 ORDER BY regression  

 LIMIT 3 