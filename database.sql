create table faculty(
    id int(11) not null auto_increment,
    name varchar(20) not null,
    password varchar(20) not null,
    primary key(id)
);

create table student(
    id int(11) not null auto_increment,
    rollno varchar(20) not null,
    name varchar(20) not null,
    password varchar(20) not null,
    primary key(id)
);

create table attendance(
    id int(11) not null auto_increment,
    rollno varchar(20) not null,
    date varchar(20) not null,
    status varchar(20) not null,
    primary key(id)
);

insert into faculty values(1,'admin','admin');
insert into faculty values(2,'sir','sir');
insert into faculty values(3,'madam','madam');
insert into student values(1,'501','Rishi','rishi');
insert into student values(2,'502','Charan','charan');
insert into student values(3,'503','Manju','manju');
