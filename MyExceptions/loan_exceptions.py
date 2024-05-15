class LoanNotFoundException(Exception):
    def __init__(self, loan_id):
        super().__init__(f"Sorry, we could'nt find your loan with {loan_id}")
