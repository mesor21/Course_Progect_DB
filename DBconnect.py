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