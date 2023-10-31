from flask import Flask, render_template, request, redirect, url_for
from DBconnect import Database
#___________________________________


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')
# _______________________________

@app.route('/edit')
def edit_page():
    return render_template('./data/edit.html')

# ========
#   POST
# ========
@app.route('/edit/post')
def list_post():
    posts = connect.get_post_list()
    return render_template('./data/post/list.html', posts=posts)

@app.route('/edit/post/<int:post_id>')
def edit_post(post_id):
    post = connect.get_post_by_id(post_id)
    if post is None:
        # Обработка случая, когда запись не найдена
        return "Запись не найдена"
    return render_template('/data/post/edit.html', post=post)

@app.route('/edit/post/<int:post_id>', methods=['POST'])
def update_post(post_id):
    new_post_name = request.form['postName']
    new_salary = request.form['salary']
    connect.update_post((new_post_name, new_salary, post_id))
    return redirect(url_for('list_post'))

@app.route('/edit/post/delete/<int:post_id>')
def delete_post(post_id):
    connect.delete_post(post_id)
    return redirect(url_for('list_post'))


@app.route('/edit/post/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        new_post_name = request.form['postName']
        new_salary = request.form['salary']
        connect.add_post((new_post_name, new_salary))
        return redirect(url_for('list_post'))
    else:
        post = {
            'postName': '',
            'salary': ''
        }
        return render_template('/data/post/add.html', post=post)

# ==========
#   routes
# ==========
@app.route('/edit/routes')
def list_routes():
    routes = connect.get_routes_list()
    return render_template('./data/routes/list.html', routes=routes)

@app.route('/edit/routes/<int:routes_id>')
def edit_routes(routes_id):
    routes = connect.get_routes_by_id(routes_id)
    if routes is None:
        return "Запись не найдена"
    return render_template('/data/routes/edit.html', routes=routes)

@app.route('/edit/routes/<int:routes_id>', methods=['POST'])
def update_routes(routes_id):
    new_name = request.form['Name']
    connect.update_routes((new_name, routes_id))
    return redirect(url_for('list_routes'))

@app.route('/edit/routes/delete/<int:routes_id>')
def delete_routes(routes_id):
    connect.delete_routes(routes_id)
    return redirect(url_for('list_routes'))

@app.route('/edit/routest/add', methods=['GET', 'POST'])
def add_routes():
    if request.method == 'POST':
        new_name = request.form['Name']
        connect.add_routes(new_name)
        return redirect(url_for('list_routes'))
    else:
        routes = {
            'Name': ''
        }
        return render_template('/data/routes/add.html', routes=routes)


# ___________________________________


# ___________________________________
@app.route('/queries')
def queries_page():
    return render_template('./data/queries.html')


if __name__ == '__main__':
    connect = Database()
    app.run(debug=True)