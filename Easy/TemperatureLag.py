# | id | recordDate | temperature |
# | -- | ---------- | ----------- |
# | 1  | 2015-01-31 | 10          |
# | 2  | 2015-02-01 | 25          |
# | 3  | 2015-02-03 | 20          |
WITH RankedWeather AS (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
)
SELECT id
FROM RankedWeather# | 4  | 2015-02-04 | 30          |