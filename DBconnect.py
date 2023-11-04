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
#   JobTitle
# ========
    def get_jobTitle_list(self):
        return self.query("SELECT * FROM JobTitle")

    def get_jobTitle_by_id(self, data):
        post_data = self.query("SELECT * FROM JobTitle WHERE JobTitleID = %s", (data,))
        if post_data:
            post_dict = {
                'JobTitleID': post_data[0][0],
                'PostName': post_data[0][1],
                'Salary': post_data[0][2]
            }
        else:
            post_dict = {}
        return post_dict


    def update_jobTitle(self, data):
        update_post_sql = "UPDATE JobTitle SET PostName = %s, Salary = %s WHERE JobTitleID = %s"
        self.query(update_post_sql, data)

    def add_jobTitle(self, data):
        insert_post_sql = "INSERT INTO JobTitle (PostName, Salary) VALUES (%s, %s)"
        self.query(insert_post_sql, data)

    def delete_jobTitle(self, data):
        delete_post_sql = "DELETE FROM JobTitle WHERE JobTitleID = %s"
        self.query(delete_post_sql, (data,))

# ========
#   department
# ========
    def get_department_list(self):
        return self.query("SELECT * FROM department")

    def get_department_by_id(self, data):
        department_data = self.query("SELECT * FROM department WHERE DepartmentID = %s", (data,))
        if department_data:
            department_dict = {
                'DepartmentID': department_data[0][0],
                'Name': department_data[0][1]
            }
        else:
            department_dict = {}
        return department_dict

    def update_department(self, data):
        update_department_sql = "UPDATE department SET Name = %s WHERE DepartmentID = %s"
        self.query(update_department_sql, data)

    def add_department(self, data):
        insert_department_sql = "INSERT INTO department (Name) VALUES (%s)"
        self.query(insert_department_sql, data)

    def delete_department(self, data):
        delete_department_sql = "DELETE FROM department WHERE DepartmentID = %s"
        self.query(delete_department_sql, (data,))

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