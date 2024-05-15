CREATE DATABASE LoanManagementDB;
Use LoanManagementDB;

CREATE TABLE Customer(
		CustomerID INT PRIMARY KEY IDENTITY(1,1),
		Name NVARCHAR(200),
		Email NVARCHAR(200),
		Phone_Number NVARCHAR(200),
		Address NVARCHAR(200),
		CreditScore INT
		)

CREATE TABLE Loan(
		LoanID INT PRIMARY KEY IDENTITY(1,1),
		CustomerID INT,
		PrincipalAmount float,
		InterestRate float,
		LoanTerm float,
		LoanType NVARCHAR(200),
		LoanStatus NVARCHAR(200),
		FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
		)