USE MUSEUM;

-- 1) Show all tables and explain how they are related to one another (keys, triggers, etc.) (Bonus)
-- 2) A basic retrieval query
-- 3) A retrieval query with ordered results
-- 4) A nested retrieval query
-- 5) A retrieval query using joined tables
-- 6) An update operation with any necessary triggers (Bonus for full custom trigger)
-- 7) A deletion operation with any necessary triggers (Bonus for full custom trigger)

-- 1)
SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = "MUSEUM"
ORDER BY TABLE_NAME;

-- 2)
SELECT *
FROM ART_OBJECT;

-- 3)
SELECT *
FROM ART_OBJECT
ORDER BY Year_of_creation DESC;

-- 4)
SELECT DISTINCT ARTIST_NAME
FROM ARTIST
WHERE Id_no IN (SELECT Id_no 
				FROM ART_OBJECT
                WHERE COST > 1000000);
-- Retrives the names of artists that have an art piece sold for a million dollars or more.

-- 5)
SELECT TITLE, O.COUNTRY_OF_ORIGIN AS "Origin", YEAR_OF_CREATION AS "Made Circa", OBJECT_DESCRIPTION AS "Description", ARTIST_NAME AS "Created By"
FROM ART_OBJECT AS O JOIN ARTIST AS A ON O.Id_no = A.Id_no
ORDER BY YEAR_OF_CREATION DESC;

-- 6)
UPDATE ART_OBJECT
SET OWNERSHIP_TYPE = "Permanent", DATE_ACQUIRED = "2023-12-05", COST = "645000", DATE_BORROWED = NULL, DATE_RETURNED = NULL
WHERE Id_no = "SC003";

-- 7)
DELETE 
FROM ART_OBJECT
WHERE Id_no = "PA001";

-- Checking update/delete 
SELECT *
FROM art_object
ORDER BY Id_no