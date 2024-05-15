from tabulate import tabulate
from DAO import CustomerService, LoanService
from Entity import Loan, Customer


class MainMenu:
    customer_service = CustomerService()
    loan_service = LoanService()

    def apply_loan_menu(self):
        customerId = int(input("enter the customer Id: "))
        principal_amount = float(input("Enter principal amount: "))
        interest_rate = float(input("Enter the Interest rate: "))
        loan_term = int(input("Enter the term loan: "))
        loan_type = input("Enter the loan type (CarLoan/HomeLoan): ")
        new_loan = Loan(
            customerId,
            principal_amount,
            interest_rate,
            loan_term,
            loan_type,
            loan_status="pending",
        )
        self.loan_service.apply_loan(new_loan)

    def calculate_interest_menu(self, loan_id):
        self.loan_service.calculate_interest(loan_id)

    def loan_status_menu(self, loan_id):
        self.loan_service.loan_status(loan_id)

    def calculate_emi_menu(self, loan_id):
        loan_id = int(input("Please Enter your loan ID :"))
        self.loan_service.calculateEMI(loan_id)

    def loan_repayment_menu(self, loan_id, amount):
        self.loan_service.loan_repayment(loan_id, amount)

    def get_all_loan_menu(self):
        self.loan_service.get_all_loan()

    def get_loan_by_id_menu(self, loan_id):
        self.loan_service.get_loan_by_id(loan_id)


def main():
    main_menu = MainMenu()

    while True:
        print(
            """" 
                1.Apply for Loan
                2.Get All Loan
                3.Get The Loan
                4.Repay Your Loan
                5.Check your loan status
                6.Calculate Interest
                7.Exit"""
        )

        option = int(input("Please choose from above options: "))
        if option == 1:
            main_menu.apply_loan_menu()
            # customerId = int(input("enter the customer Id: "))
            # principal_amount = float(input("Enter principal amount: "))
            # interest_rate = float(input("Enter the Interest rate: "))
            # loan_term = int(input("Enter the term loan: "))
            # loan_type = input("Enter the loan type (CarLoan/HomeLoan): ")
            # new_loan = Loan(
            #     customerId,
            #     principal_amount,
            #     interest_rate,
            #     loan_term,
            #     loan_type,
            #     loan_status="pending",
            # )
            # self.loan_service.apply_loan(new_loan)
        elif option == 2:
            main_menu.get_all_loan_menu()
        elif option == 3:
            loan_id = int(input("Please Enter your loan ID :"))
            main_menu.get_loan_by_id_menu(loan_id)
        elif option == 4:
            loan_id = int(input("Please Enter your loan ID :"))
            amount = float(input("Enter the amount:"))
            main_menu.loan_repayment_menu(loan_id, amount)
        elif option == 5:
            loan_id = int(input("Please Enter your loan ID :"))
            main_menu.loan_status_menu(loan_id)
        elif option == 6:
            loan_id = int(input("Please Enter your loan ID :"))
            main_menu.calculate_interest_menu(loan_id)
        elif option == 7:
            main_menu.loan_service.close()
            main_menu.customer_service.close()
            break


if __name__ == "__main__":
    print("Welcome to the Loan management app")
    main()
