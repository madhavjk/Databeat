#Q3-a)
DELIMITER &&
CREATE PROCEDURE Emp()
BEGIN
     SELECT e.FIRST_NAME, e.LAST_NAME, e.SALARY, e.DEPARTMENT, e.SALARY, 
     e.JOINING_DATE, d.EMP_TITLE, 
     EXTRACT(MONTH FROM d.AFFECTED_FORM) AS MONTH
     FROM employeetable e,designationtable d, variablesdetails v
     WHERE MONTH(d.AFFECTED_FORM)>6
     ORDER BY v.VARIABLES_AMOUNT DESC;
 END &&
 -----------------------------------------------------------------------------------------------------
 # b
 
 DELIMITER &&
CREATE PROCEDURE Emp1(IN var1 INT)  #using  argument var1
BEGIN
     SELECT CONCAT(e.FIRST_NAME," ",e.LAST_NAME) AS "FULL_NAME" , e.DEPARTMENT
     FROM employeetable e
     JOIN  variablesdetails v
     ON e.EMP_ID = v.EMP_REF_ID
     AND v.VARIABLES_AMOUNT= (SELECT MAX(variablesdetails.VARIABLES_AMOUNT)
					       FROM variablesdetails
                           LIMIT var1);
                           
	  SELECT CONCAT(e.FIRST_NAME," ",e.LAST_NAME) AS "FULL_NAME" , e.DEPARTMENT
      FROM employeetable e
      JOIN  variablesdetails v
      ON e.EMP_ID = v.EMP_REF_ID
      AND v.VARIABLES_AMOUNT= (SELECT min(variablesdetails.VARIABLES_AMOUNT)
					       FROM variablesdetails
                           LIMIT var1);
 END &&
 
 
 
 
 
 

 