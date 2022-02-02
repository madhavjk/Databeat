  #INNER JOIN

# a.1)- HIGHEST VARIABLE

SELECT CONCAT(e.FIRST_NAME," ",e.LAST_NAME) AS "FULL_NAME" , e.DEPARTMENT
FROM employeetable e
JOIN  variablesdetails v
ON e.EMP_ID = v.EMP_REF_ID
AND v.VARIABLES_AMOUNT= (SELECT MAX(variablesdetails.VARIABLES_AMOUNT)
					       FROM variablesdetails
                           LIMIT 1);


# a.2) LEAST VARIABLE
SELECT CONCAT(e.FIRST_NAME," ",e.LAST_NAME) AS "FULL_NAME" , e.DEPARTMENT, MIN(v.VARIABLES_AMOUNT)
FROM employeetable e
INNER JOIN  variablesdetails v
ON e.EMP_ID = v.EMP_REF_ID;


SELECT CONCAT(e.FIRST_NAME," ",e.LAST_NAME) AS "FULL_NAME" , e.DEPARTMENT
FROM employeetable e
JOIN  variablesdetails v
ON e.EMP_ID = v.EMP_REF_ID
AND v.VARIABLES_AMOUNT= (SELECT min(variablesdetails.VARIABLES_AMOUNT)
					       FROM variablesdetails
                           LIMIT 1);
--------------------------------------------------------------------------------------------

#b) 

SELECT  AS "FULL_NAME" , e.DEPARTMENT, MIN(v.VARIABLES_AMOUNT)
FROM employeetable e
INNER JOIN  variablesdetails v
ON e.EMP_ID = v.EMP_REF_ID;
-------------------------------------------------------------------------------


# c) CROSS JOIN
SELECT CONCAT(e.FIRST_NAME," ",e.LAST_NAME) AS "FULL_NAME", e.DEPARTMENT, e.JOINING_DATE,e.SALARY, 
d.EMP_TITLE,d.AFFECTED_FORM
FROM employeetable e 
CROSS JOIN designationtable d;

-----------------------------------------------------------------------------



--------------------------------------------------------
# D) 



 

