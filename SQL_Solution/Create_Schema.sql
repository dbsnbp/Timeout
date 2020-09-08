--Create Product table
create table Products 
(
product varchar(255),
price_effective_date date,
price int
);


--Create Sales Table
create table Sales 
(
product varchar(255),
sales_date date,
quantity int
);

