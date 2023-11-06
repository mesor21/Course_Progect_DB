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
#   Department
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

# ========
#   DriverCategory
# ========
    def get_driver_category_list(self):
        return self.query("SELECT * FROM DriverCategory")

    def get_driver_category_by_id(self, data):
        driver_category_data = self.query("SELECT * FROM DriverCategory WHERE DriverCategoryID = %s", (data,))
        if driver_category_data:
            driver_category_dict = {
                'DriverCategoryID': driver_category_data[0][0],
                'Category': driver_category_data[0][1]
            }
        else:
            driver_category_dict = {}
        return driver_category_dict

    def update_driver_category(self, data):
        update_driver_category_sql = "UPDATE DriverCategory SET Category = %s WHERE DriverCategoryID = %s"
        self.query(update_driver_category_sql, data)

    def add_driver_category(self, data):
        insert_driver_category_sql = "INSERT INTO DriverCategory (Category) VALUES (%s)"
        self.query(insert_driver_category_sql, data)

    def delete_driver_category(self, data):
        delete_driver_category_sql = "DELETE FROM DriverCategory WHERE DriverCategoryID = %s"
        self.query(delete_driver_category_sql, (data,))

# ==========
#   routes
# ==========
    def get_routes_list(self):
        return self.query("SELECT * FROM Routes")

    def get_route_by_id(self, data):
        route_data = self.query("SELECT * FROM Routes WHERE RoutesID = %s", (data,))
        if route_data:
            route_dict = {
                'RoutesID': route_data[0][0],
                'Number': route_data[0][1],
                'From': route_data[0][2],
                'To': route_data[0][3],
                'DepartureTime': route_data[0][4],
                'ArrivalTime': route_data[0][5]
            }
        else:
            route_dict = {}
        return route_dict

    def update_route(self, data):
        update_route_sql = "UPDATE Routes SET Number = %s, \"From\" = %s, \"To\" = %s, DepartureTime = %s, ArrivalTime = %s WHERE RoutesID = %s"
        self.query(update_route_sql, data)

    def add_route(self, data):
        insert_route_sql = "INSERT INTO Routes (Number, \"From\", \"To\", DepartureTime, ArrivalTime) VALUES (%s, %s, %s, %s, %s)"
        self.query(insert_route_sql, data)

    def delete_route(self, data):
        delete_route_sql = "DELETE FROM Routes WHERE RoutesID = %s"
        self.query(delete_route_sql, (data,))

# ==========
#   Employee
# ==========
    def get_employee_list(self):
        return self.query("""
            SELECT Employee.EmployeeID, Employee.name, Employee.secondName, Employee.LastName, 
            JobTitle.postName, DriverCategory.Category, Department.Name
            FROM Employee
            LEFT JOIN JobTitle ON Employee.JobTitleID = JobTitle.JobTitleID
            LEFT JOIN DriverCategory ON Employee.DriverCategoryID = DriverCategory.DriverCategoryID
            LEFT JOIN Department ON Employee.DepartmentID = Department.DepartmentID;
        """)

    def get_employee_by_id(self, id):
        employee_data = self.query("SELECT * FROM Employee WHERE EmployeeID = %s", (id,))
        if employee_data:
            employee_dict = {
                'EmployeeID': employee_data[0][0],
                'Name': employee_data[0][1],
                'SecondName': employee_data[0][2],
                'LastName': employee_data[0][3],
                'JobTitleID': employee_data[0][4],
                'DriverCategoryID': employee_data[0][5],
                'DepartmentID': employee_data[0][6]
            }
        else:
            employee_dict = {}
        return employee_dict

    def update_employee(self, data):
        update_employee_sql = "UPDATE Employee SET name = %s, secondName = %s, lastName = %s, JobTitleID = %s, DriverCategoryID = %s, DepartmentID = %s WHERE EmployeeID = %s"
        self.query(update_employee_sql, data)

    def add_employee(self, data):
        insert_employee_sql = "INSERT INTO Employee (name, secondName, lastName, JobTitleID, DriverCategoryID, DepartmentID) VALUES (%s, %s, %s, %s, %s, %s)"
        return self.query(insert_employee_sql, data)

    def delete_employee(self, id):
        delete_employee_sql = "DELETE FROM Employee WHERE EmployeeID = %s"
        self.query(delete_employee_sql, (id,))

# =======
#   Brand
# =======
    def get_brand_list(self):
        return self.query("SELECT * FROM Brand")

    def get_brand_by_id(self, brand_id):
        brand_data = self.query("SELECT * FROM Brand WHERE BrandID = %s", (brand_id,))
        if brand_data:
            brand_dict = {
                'BrandID': brand_data[0][0],
                'Name': brand_data[0][1]
            }
        else:
            brand_dict = {}
        return brand_dict

    def update_brand(self, brand_data):
        update_brand_sql = "UPDATE Brand SET Name = %s WHERE BrandID = %s"
        self.query(update_brand_sql, (brand_data['Name'], brand_data['BrandID']))

    def add_brand(self, brand_data):
        insert_brand_sql = "INSERT INTO Brand (Name) VALUES (%s) RETURNING BrandID"
        result = self.query(insert_brand_sql, (brand_data['Name'],))
        return result[0][0] if result else None

    def delete_brand(self, brand_id):
        delete_brand_sql = "DELETE FROM Brand WHERE BrandID = %s"
        self.query(delete_brand_sql, (brand_id,))
# =======
#   Bus
# =======
    def get_bus_list(self):
        return self.query("""
            SELECT Bus.BusID, Bus.StateNumber, Bus.VIN, Brand.Name, Bus.NumberOfPeople
            FROM Bus
            LEFT JOIN Brand ON Bus.BrandID = Brand.BrandID;
        """)

    def get_bus_by_id(self, id):
        bus_data = self.query("SELECT * FROM Bus WHERE BusID = %s", (id,))
        if bus_data:
            bus_dict = {
                'BusID': bus_data[0][0],
                'StateNumber': bus_data[0][1],
                'VIN': bus_data[0][2],
                'BrandID': bus_data[0][3],
                'NumberOfPeople': bus_data[0][4]
            }
        else:
            bus_dict = {}
        return bus_dict

    def update_bus(self, data):
        update_bus_sql = "UPDATE Bus SET StateNumber = %s, VIN = %s, BrandID = %s, NumberOfPeople = %s WHERE BusID = %s"
        self.query(update_bus_sql, data)

    def add_bus(self, data):
        insert_bus_sql = "INSERT INTO Bus (StateNumber, VIN, BrandID, NumberOfPeople) VALUES (%s, %s, %s, %s)"
        return self.query(insert_bus_sql, data)

    def delete_bus(self, id):
        delete_bus_sql = "DELETE FROM Bus WHERE BusID = %s"
        self.query(delete_bus_sql, (id,))

# =============
#   Itineraty
# =============
    def get_itineraty_list(self):
        return self.query("""
            SELECT
                Itineraty.ItineratyID,
                Bus.StateNumber AS bus_state_number,
                Routes.Number AS route_number,
                CONCAT(Driver.Name, ' ', Driver.SecondName) AS driver_name,
                CONCAT(Conductor.Name, ' ', Conductor.SecondName) AS conductor_name,
                Itineraty.DateTime AS date_time
            FROM Itineraty
            LEFT JOIN Bus ON Itineraty.BusID = Bus.BusID
            LEFT JOIN Routes ON Itineraty.RoutesID = Routes.RoutesID
            LEFT JOIN Employee AS Driver ON Itineraty.Driver_EmployeeID = Driver.EmployeeID
            LEFT JOIN Employee AS Conductor ON Itineraty.Conductor_EmployeeID = Conductor.EmployeeID;
        """)

    def get_itineraty_by_id(self, id):
        itineraty_data = self.query("SELECT * FROM Itineraty WHERE ItineratyID = %s", (id,))
        if itineraty_data:
            itineraty_dict = {
                'ItineratyID': itineraty_data[0][0],
                'BusID': itineraty_data[0][1],
                'RoutesID': itineraty_data[0][2],
                'DateTime': itineraty_data[0][3],
                'Driver_EmployeeID': itineraty_data[0][4],
                'Conductor_EmployeeID': itineraty_data[0][5]
            }
        else:
            itineraty_dict = {}
        return itineraty_dict
    def update_itineraty(self, data):
        update_itineraty_sql = "UPDATE Itineraty SET BusID = %s, RoutesID = %s, DateTime = %s, Driver_EmployeeID = %s, Conductor_EmployeeID = %s WHERE ItineratyID = %s"
        self.query(update_itineraty_sql, data)
    def add_itineraty(self, data):
        insert_itineraty_sql = "INSERT INTO Itineraty (BusID, RoutesID, DateTime, Driver_EmployeeID, Conductor_EmployeeID) VALUES (%s, %s, %s, %s, %s)"
        return self.query(insert_itineraty_sql, data)

# ===========
#   Queries
# ===========
    def get_routes_by_date(self, date):
        # Пример SQL-запроса для поиска маршрутов и количества автобусов на заданную дату
        sql = """
        SELECT R.Number, COUNT(I.BusID)
        FROM Itineraty AS I
        JOIN Routes AS R ON I.RoutesID = R.RoutesID
        WHERE DATE(I.DateTime) = %s
        GROUP BY R.Number
        """
        routes_data = self.query(sql, (date,))
        return routes_data

    def get_buses_for_route_by_date(self, route_number, date):
        sql = """
        SELECT B.StateNumber, B.VIN, Br."name" AS BrandName, B.NumberOfPeople
        FROM Itineraty AS I
        JOIN Routes AS R ON I.RoutesID = R.RoutesID
        JOIN Bus AS B ON I.BusID = B.BusID
        JOIN Brand AS Br ON B.BrandID = Br.BrandID
        WHERE R.Number = %s AND DATE(I.DateTime) = %s
        """
        bus_data = self.query(sql, (route_number, date))
        return bus_data

    def get_routes_and_counts_by_month(self, month):
        sql = """
        SELECT r."number", COUNT(i."routesid")
        FROM Itineraty i
        JOIN Routes r ON i."routesid" = r."routesid"
        WHERE DATE_TRUNC('month', i."datetime") = %s
        GROUP BY r."number"
        ORDER BY r."number";
        """
        result_data = self.query(sql, (month,))
        return result_data

    def get_buses_and_counts_by_month(self, month):
        sql = """
        SELECT b."statenumber", COUNT(i."busid")
        FROM Itineraty i
        JOIN Bus b ON i."busid" = b."busid"
        WHERE DATE_TRUNC('month', i."datetime") = %s
        GROUP BY b."statenumber"
        ORDER BY b."statenumber";
        """
        result_data = self.query(sql, (month,))
        return result_data

    def get_shifts_by_employee(self):
        sql = """
        SELECT e."lastname", COUNT(I."itineratyid") AS "ShiftsCount"
        FROM Employee e
        LEFT JOIN Itineraty AS i ON e."employeeid" = i."driver_employeeid" OR e."employeeid" = i."conductor_employeeid"
        WHERE DATE(i."datetime") >= NOW() - interval '6 months'
        GROUP BY e."lastname"
        ORDER BY "ShiftsCount" DESC
        """
        result_data = self.query(sql)
        return result_data
