CREATE TABLE country(
  country_name VARCHAR PRIMARY KEY,
  population INTEGER,
  area INTEGER,
  infant_mortality REAL,
  gdp INTEGER,
  literacy REAL,
  region VARCHAR,
  climate NUMERIC(2,1)
  );

CREATE TABLE happiness(
  ref SERIAL PRIMARY KEY,
  rank INTEGER,
  happiness_score real,
  country_name VARCHAR REFERENCES country NOT NULL,
  year INTEGER
  );
