from tabulate import tabulate
from Util.DBConn import DBConnection
from MyExceptions.loan_exceptions import LoanNotFoundException
from abc import ABC, abstractmethod


class ILoanService(ABC):
    @abstractmethod
    def apply_loan(self, loan):
        pass

    @abstractmethod
    def calculate_interest(self, loan_id):
        pass

    @abstractmethod
    def loan_status(self, loan_id):
        pass

    @abstractmethod
    def calculateEMI(self, loan_id):
        pass

    @abstractmethod
    def loan_repayment(self, loan_id, amount):
        pass

    @abstractmethod
    def get_all_loan(self):
        pass

    @abstractmethod
    def get_loan_by_id(self, loan_id):
        pass


class LoanService(ILoanService, DBConnection):

    def apply_loan(self, loan):
        try:
            confirm = input("Confirm before applying for the loan (yes/No):")
            if confirm.lower() == "yes":
                self.cursor.execute(
                    """
                            INSERT INTO Loan 
	                        (CustomerID,PrincipalAmount,InterestRate,LoanTerm,LoanType,LoanStatus)
                                    VALUES (?,?,?,?,?,?)""",
                    (
                        loan.customer_id,
                        loan.principal_amount,
                        loan.interest_rate,
                        loan.loan_term,
                        loan.loan_type,
                        loan.loan_status,
                    ),
                )
                self.conn.commit()
        except Exception as e:
            print(e)

    def calculate_interest(self, loan_id):
        try:
            self.cursor.execute(
                "SELECT PrinicipalAmount,InterestRate,LoanTerm from Loan where LoanID=?",
                (loan_id),
            )
            loan_data = self.cursor.fetchone()
            if loan_data:
                principal_amount, interest_rate, loan_term = loan_data
                interest = (principal_amount * interest_rate * loan_term) / 12
                return interest
            else:
                raise LoanNotFoundException(
                    f"Sorry, we could'nt find your loan with {loan_id}"
                )
        except Exception as e:
            print("OOPS Error Happened: ", e)

    def loan_status(self, loan_id):
        self.cursor.execute(
            "SELECT CreditScore from Customer where CustomerID IN (SELECT customerID from Loan where LoanID=?)",
            (loan_id),
        )
        credit_score = self.cursor.fetchone()[0]
        if credit_score > 650:
            self.cursor.execute(
                "UPDATE Loan set Loanstatus='Approved' where LoanId=?", (loan_id)
            )
            self.conn.commit()
            print("Congratulations, Your Loan has been approved ✅")
        else:
            self.cursor.execute(
                "UPDATE Loan set Loanstatus='Rejected' where LoanId=?", (loan_id)
            )
            self.conn.commit()
            print("Sorry, Your Loan has been rejected due to less credit score❌")

    def calculateEMI(self, loan_id):
        try:
            self.cursor.execute(
                "SELECT PrincipalAmount,InterestRate,Loanterm from Loan where LoanID=?",
                (loan_id),
            )
            loan_data = self.cursor.fetchone()
            if loan_data:
                principal_amount, interest_rate, loan_term = loan_data
                monthly_interest_rate = interest_rate / 12 / 100
                EMI = (
                    principal_amount
                    * monthly_interest_rate
                    * (1 + monthly_interest_rate) ** loan_term
                ) / ((1 + monthly_interest_rate) ** loan_term - 1)
                return EMI
            else:
                raise LoanNotFoundException(
                    f"Sorry, we could'nt find your loan with {loan_id}"
                )
        except Exception as e:
            print("OOPS Error Happened: ", e)

    def loan_repayment(self, loan_id, amount):
        self.cursor.execute(
            "SELECT PrincipalAmount,InterestRate,Loanterm from Loan where LoanID=?",
            (loan_id),
        )
        loan_data = self.cursor.fetchone()[0]
        principal_amount = loan_data
        emi = self.calculateEMI(loan_id)
        no_Of_emi = amount / emi
        updated_amount = principal_amount - amount
        if no_Of_emi >= 1:
            print(
                f"Your Payment has been accepted successfully , emi's paid :{no_Of_emi}"
            )
            self.cursor.execute(
                "UPDATE Loan set principalamount=? where LoanId=?",
                (principal_amount, loan_id),
            )
            self.conn.commit()
        else:
            print("Payment Rejected")

    def get_all_loan(self):
        try:
            self.cursor.execute("SELECT * FROM Loan")
            Loan_data = [list(row) for row in self.cursor.fetchall()]
            headers = [
                "LoanID",
                "customer_ID",
                "principal_amount",
                "interest_rate",
                "loan_term",
                "loan_type",
                "loan_status",
            ]
            print(tabulate(Loan_data, headers=headers, tablefmt="rounded_outline"))
        except Exception as e:
            print(e)

    def get_loan_by_id(self, loan_id):
        try:
            self.cursor.execute("SELECT * FROM Loan where LoanId=?", (loan_id))
            loan_data = self.cursor.fetchall()
            if len(loan_data) == 0:
                raise LoanNotFoundException(loan_id)
            else:
                print(loan_data)
        except Exception as e:
            print("OOPs Error happend: ", e)
