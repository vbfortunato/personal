-- Work against a staging copy first. This script only shows the correction.
-- Keep the six-digit term in its own column before trimming the CRN.
BEGIN TRANSACTION;

SELECT CourseCRN, LEFT(CourseCRN, CHARINDEX('|', CourseCRN) - 1) AS NewCRN
FROM dbo.DimBookAdoption
WHERE Source = 'Akademos' AND CHARINDEX('|', CourseCRN) > 0;

UPDATE dbo.DimBookAdoption
SET CourseCRN = LEFT(CourseCRN, CHARINDEX('|', CourseCRN) - 1)
WHERE Source = 'Akademos' AND CHARINDEX('|', CourseCRN) > 0;

SELECT COUNT(*) AS RemainingCompoundCRNs
FROM dbo.DimBookAdoption
WHERE Source = 'Akademos' AND CHARINDEX('|', CourseCRN) > 0;

-- This example does not change your database permanently.
ROLLBACK TRANSACTION;
