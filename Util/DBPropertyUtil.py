class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "DESKTOP-BJQV7BU\SQLEXPRESS"
        database_name = "LoanManagementDB"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )
        return conn_str
