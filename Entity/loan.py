class Loan:
    def __init__(
        self,
        customer_id,
        principal_amount,
        interest_rate,
        loan_term,
        loan_type,
        loan_status,
    ):
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status
        self.customer_id = customer_id

    # def get_all_details(self):
    #     print(f"Customer ID : {self.customer_id}")
    #     print(f"principal amount is : {self.principal_amount}")
    #     print(f"interste rate : {self.interest_rate}")
    #     print(f"loan term for 10 years: {self.loan_term}")
    #     print(f"type of loan is : {self.loan_type}")
    #     print(f"status of the loan: {self.loan_status}")


class HomeLoan(Loan):
    def __init__(
        self,
        customer_id,
        principal_amount,
        interest_rate,
        loan_term,
        loan_status,
        property_address,
        property_value,
    ):
        super().__init__(
            customer_id,
            principal_amount,
            interest_rate,
            loan_term,
            "HomeLoan",
            loan_status,
        )
        self.property_address = property_address
        self.property_value = property_value

    # def get_home_loan_details(self):
    #     super().get_all_details()
    #     print(f"property address :{self.property_address}")
    #     print(f"property value :{self.property_value}")


class CarLoan(Loan):
    def __init__(
        self,
        customer_id,
        principal_amount,
        interest_rate,
        loan_term,
        loan_status,
        car_model,
        car_value,
    ):
        super().__init__(
            customer_id,
            principal_amount,
            interest_rate,
            loan_term,
            "CarLoan",
            loan_status,
        )
        self.car_model = car_model
        self.car_value = car_value

    # def get_car_loan_details(self):
    #     super().get_all_details()
    #     print(f"car model :{self.car_model}")
    #     print(f"car value :{self.car_value}")


# pooji = CarLoan(1, 10000, 3573, 10, "approved", "mercedes", 7835764)
# pooji.get_car_loan_details()
