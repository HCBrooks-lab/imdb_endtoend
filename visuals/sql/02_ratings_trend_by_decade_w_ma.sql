WITH base AS (
  SELECT
    CAST(SUBSTR(CAST(start_year AS TEXT), 1, 3) || '0' AS INT) AS decade,
    rating,
    COALESCE(numVotes, 0) AS votes
  FROM movies_clean
  WHERE start_year IS NOT NULL
    AND rating IS NOT NULL
    AND COALESCE(numVotes, 0) >= 50
),
agg AS (
  SELECT
    decade,
    SUM(votes) AS total_votes,
    SUM(rating * votes) * 1.0 / NULLIF(SUM(votes), 0) AS avg_rating_w
  FROM base
  GROUP BY decade
),
ma AS (
  SELECT
    decade,
    total_votes,
    avg_rating_w,
    ROUND((
      COALESCE(LAG(avg_rating_w)  OVER (ORDER BY decade), avg_rating_w) +
      avg_rating_w +
      COALESCE(LEAD(avg_rating_w) OVER (ORDER BY decade), avg_rating_w)
    ) / 3.0, 3) AS avg_rating_w_ma3
  FROM agg
)
SELECT * FROM ma ORDER BY decade;

