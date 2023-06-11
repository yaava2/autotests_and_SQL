--задание 1
SELECT c.login, COUNT(o."inDelivery") FROM "Couriers" AS c RIGHT JOIN "Orders" AS o ON c.id=o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;

-- задание 2
SELECT track, finished, "inDelivery", "Orders".cancelled, CASE  WHEN finished = true THEN '2' WHEN "inDelivery" = true THEN '1' WHEN "Orders".cancelled= true THEN '-1'    ELSE '0' END FROM "Orders";