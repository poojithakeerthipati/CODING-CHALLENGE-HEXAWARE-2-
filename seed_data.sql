Use LoanManagementDB;
INSERT INTO Customer
	(Name, Email,Phone_Number, Address ,CreditScore) 
	VALUES('James Adam','jamesadam@gmail.com','181-5638677',
			'church street,banglore,karnataka',640);

INSERT INTO Customer
	(Name, Email,Phone_Number, Address ,CreditScore) 
	VALUES('ram shetty','ramshetty@gmail.com','91-53745745',
			'Chennai,Tamilnadu',740),('kiara','kiara123@gmail.com','91-945798589',
			'Hyderabad,Telangana',230);

INSERT INTO Loan (CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus)
VALUES 
    ( 1, 10000.00, 5.25, 36, 'CarLoan', 'Approved'),
    ( 2, 150000.00, 4.75, 120, 'HomeLoan', 'Pending'),
    ( 3, 5000.00, 6.00, 24, 'PersonalLoan', 'pending');

select *from Customer;
select *from loan