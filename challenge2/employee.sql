SELECT first_name, last_name FROM employee
WHERE id_employee IN (SELECT id_employee FROM table_1 
WHERE dt_work_from >= '2020-01-01';
AND dt_work_to <= '2020-01-31';)
UNION
SELECT first_name, last_name FROM manager
WHERE id_manager IN (SELECT id_manager FROM table_1 
WHERE dt_work_from >= '2020-01-01';
AND dt_work_to <= '2020-01-31';)

