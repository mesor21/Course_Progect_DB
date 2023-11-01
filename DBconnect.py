import psycopg2

db_config = {
    'dbname': 'db',
    'user': 'postgres',
    'password': 'postgresql',
    'host': '127.0.0.1'
}

class Database:
    @staticmethod
    def query(query, data=None):
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        if data is not None:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        if query.strip().lower().startswith("select"):
            data = cursor.fetchall()
        else:
            conn.commit()

        cursor.close()
        conn.close()

        return data

# ========
#   POST
# ========
    def get_post_list(self):
        return self.query("SELECT * FROM Post")

    def get_post_by_id(self, post_id):
        post_data = self.query("SELECT * FROM Post WHERE PostID = %s", (post_id,))
        if post_data:
            post_dict = {
                'PostID': post_data[0][0],
                'postName': post_data[0][1],
                'salary': post_data[0][2]
            }
        else:
            post_dict = {}
        return post_dict


    def update_post(self, data):
        update_post_sql = "UPDATE Post SET postName = %s, salary = %s WHERE PostID = %s"
        self.query(update_post_sql, data)

    def add_post(self, data):
        insert_post_sql = "INSERT INTO Post (postName, salary) VALUES (%s, %s)"
        self.query(insert_post_sql, data)

    def delete_post(self, post_id):
        delete_post_sql = "DELETE FROM Post WHERE PostID = %s"
        self.query(delete_post_sql, (post_id,))

# ==========
#   routes
# ==========
    def get_routes_list(self):
        return self.query("SELECT * FROM routes")

    def get_routes_by_id(self, id):
        post_data = self.query("SELECT * FROM routes WHERE RoutesID = %s", (id,))
        if post_data:
            post_dict = {
                'RoutesID': post_data[0][0],
                'Name': post_data[0][1]
            }
        else:
            post_dict = {}
        return post_dict

    def update_routes(self, data):
        update_post_sql = "UPDATE routes SET name = %s WHERE RoutesID = %s"
        self.query(update_post_sql, data)

    def add_routes(self, data):
        insert_routes_sql = "INSERT INTO Routes (name) VALUES (%s)"
        return self.query(insert_routes_sql, (data,))

    def delete_routes(self, id):
        delete_post_sql = "DELETE FROM Routes WHERE RoutesID = %s"
        self.query(delete_post_sql, (id,))
# ==========
#   Employee
# ==========
    def get_employee_list(self):
        return self.query("""
            SELECT Employee.EmployeeID, Employee.name, Employee.secondName, Employee.LastName, Post.postName
            FROM Employee
            LEFT JOIN Post ON Employee.PostID = Post.PostID;
        """)

    def get_employee_by_id(self, id):
        employee_data = self.query("SELECT * FROM Employee WHERE EmployeeID = %s", (id,))
        if employee_data:
            employee_dict = {
                'EmployeeID': employee_data[0][0],
                'name': employee_data[0][1],
                'secondName': employee_data[0][2],
                'lastName': employee_data[0][3],
                'PostId': employee_data[0][4],
            }
        else:
            employee_dict = {}
        return employee_dict

    def update_employee(self, data):
        update_employee_sql = "UPDATE Employee SET name = %s ,secondName = %s, lastName = %s, PostId = %s WHERE EmployeeID = %s"
        self.query(update_employee_sql, data)

    def add_employee(self, data):
        insert_employee_sql = "INSERT INTO Employee (name, secondName, lastName, PostId) VALUES (%s, %s, %s, %s)"
        return self.query(insert_employee_sql, data)

    def delete_employee(self, id):
        delete_employee_sql = "DELETE FROM Employee WHERE EmployeeID = %s"
        self.query(delete_employee_sql, (id,))

# =======
#   Bus
# =======
    def get_bus_list(self):
        return self.query("SELECT * FROM Bus")

    def get_bus_by_id(self, id):
        employee_data = self.query("SELECT * FROM Bus WHERE BusID = %s", (id,))
        if employee_data:
            employee_dict = {
                'stateNumber': employee_data[0][0],
                'vin': employee_data[0][1],
                'brand': employee_data[0][2],
                'numberOfPeople': employee_data[0][3]
            }
        else:
            employee_dict = {}
        return employee_dict

    def update_bus(self, data):
        update_employee_sql = "UPDATE Bus SET stateNumber = %s ,vin = %s, brand = %s, numberOfPeaple = %s WHERE BusID = %s"
        self.query(update_employee_sql, data)

    def add_bus(self, data):
        insert_employee_sql = "INSERT INTO Bus (stateNumber, vin, brand, numberOfPeaple) VALUES (%s, %s, %s, %s)"
        return self.query(insert_employee_sql, data)

    def delete_bus(self, id):
        delete_employee_sql = "DELETE FROM Bus WHERE BusID = %s"
        self.query(delete_employee_sql, (id,))