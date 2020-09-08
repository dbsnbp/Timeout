--Logic to calculate the total revenue
--Calculation is as below
--We get  price for max[(price_effective_Date)<=sales_date] record for the related product in Products table.
--If we had to 
--Question 1 Answer:Total Revenue is 4390.
--Question 2 Answer : Below
    SELECT sum(quantity*price) as "Total_Revenue" from (select 
        s.quantity
        ,(SELECT TOP 1 p.price
        FROM products AS p
        WHERE p.price_Effective_Date <= s.Sales_Date and p.product=s.product
        ORDER BY p.price_Effective_Date DESC) AS Price
    FROM
        sales s) x

