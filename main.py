from flask import Flask, render_template, request, redirect, url_for
import psycopg2

# Database connection
# _____________________________________
import psycopg2

db_config = {
    'dbname': 'db',
    'user': 'postgres',
    'password': 'postgresql',
    'host': '127.0.0.1'
}

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

def get_post_list():
    return query("SELECT * FROM Post")

def get_post_by_id(post_id):
    post_data = query("SELECT * FROM Post WHERE PostID = %s", (post_id,))
    if post_data:
        post_dict = {
            'PostID': post_data[0][0],
            'postName': post_data[0][1],
            'salary': post_data[0][2]
        }
    else:
        post_dict = {}
    return post_dict


def update_post(data):
    update_post_sql = "UPDATE Post SET postName = %s, salary = %s WHERE PostID = %s"
    query(update_post_sql, data)


#___________________________________


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')
# _______________________________

@app.route('/edit')
def edit_page():
    return render_template('./data/edit.html')

@app.route('/edit/post')
def list_post():
    posts = get_post_list()
    return render_template('./data/post/list.html', posts=posts)

@app.route('/edit/post/<int:post_id>')
def edit_post(post_id):
    post = get_post_by_id(post_id)
    if post is None:
        # Обработка случая, когда запись не найдена
        return "Запись не найдена"
    return render_template('/data/post/edit.html', post=post)

@app.route('/edit/post/<int:post_id>', methods=['POST'])
def save_post(post_id):
    new_post_name = request.form['postName']
    new_salary = request.form['salary']
    update_post((new_post_name, new_salary, post_id))
    return redirect(url_for('edit_post', post_id=post_id))


# ___________________________________
@app.route('/compose_routes')
def compose_routes_page():
    return render_template('./data/compose_routes.html')

# ___________________________________
@app.route('/queries')
def queries_page():
    return render_template('./data/queries.html')


if __name__ == '__main__':
    app.run(debug=True)