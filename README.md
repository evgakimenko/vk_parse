# vk_parse

# Instruction:

* Before the first run, you need to generate API Token from VK.com
* insert in the browser next url: https://oauth.vk.com/authorize?client_id=	51723285&scope=offline,photos,friends,wall&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.131&response_type=token
  in the  response url line you will recieve your token. Insert this in .env file with name VK_TOKEN
* If necessary, change the configuration of ports etc.
* Download, install and run Docker
* Run "make dev" command in console
* If you have a Windows, then run the command instead of the previous command: docker compose up -d --build

you can access Swagger by the link http://localhost:8000/api/docs


Задача №1

SELECT 
    c.client_id AS ID,
    CONCAT(c.first_name, ' ', c.last_name) AS Name,
    o.category AS Category,
    GROUP_CONCAT(o.product ORDER BY o.product) AS Products
FROM
    clients c
JOIN
    client_orders co ON c.client_id = co.client_id
JOIN
    orders o ON co.order_id = o.order_id
WHERE
    c.age BETWEEN 18 AND 65
GROUP BY
    c.client_id, o.category
HAVING
    COUNT(DISTINCT o.product) = 2
    AND COUNT(DISTINCT o.category) = 1;

