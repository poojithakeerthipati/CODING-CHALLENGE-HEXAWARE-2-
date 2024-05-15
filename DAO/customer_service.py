from tabulate import tabulate
from Util.DBConn import DBConnection


class CustomerService(DBConnection):
    def read_customers(self):
        try:
            self.cursor.execute("SELECT * FROM Customeer")
            customers = [list(row) for row in self.cursor.fetchall()]
            headers = [
                "CustomerID",
                "name",
                "Email",
                "phone_number",
                "address",
                "credit_score",
            ]
            print(tabulate(customers, headers=headers, tablefmt="rounded_outline"))
        except Exception as e:
            print(e)
