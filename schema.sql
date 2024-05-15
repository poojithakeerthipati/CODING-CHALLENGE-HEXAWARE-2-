CREATE DATABASE LoanManagementDB;
Use LoanManagementDB;

CREATE TABLE Customer(
		CustomerID INT PRIMARY KEY IDENTITY(1,1),
		Name NVARCHAR(100),
		Email NVARCHAR(100),
		Phone_Number NVARCHAR(100),
		Address NVARCHAR(200),
		CreditScore float
		)

CREATE TABLE Loan(
		LoanID INT PRIMARY KEY IDENTITY(1,1),
		CustomerID INT,
		PrincipalAmount float,
		InterestRate float,
		LoanTerm float,
		LoanType NVARCHAR,
		LoanStatus NVARCHAR,
		FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
		)