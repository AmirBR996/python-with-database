CREATE DATABASE bank;
CREATE TABLE DETAILS(
  account_number varchar(20) primary key,
  name varchar(20) ,
  balance bigint
  );
use bank;
insert into DETAILS
(account_number,name,balance)
values
('p000','amir',10000),
('p002','micheal',1000);

select * from DETAILS
