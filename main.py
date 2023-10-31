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
def save_post():
    new_post_name = request.form['postName']
    new_salary = request.form['salary']
    connect.update_post((new_post_name, new_salary))
    return redirect(url_for('edit_post'))

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



# ___________________________________
@app.route('/compose_routes')
def compose_routes_page():
    return render_template('./data/compose_routes.html')

# ___________________________________
@app.route('/queries')
def queries_page():
    return render_template('./data/queries.html')


if __name__ == '__main__':
    connect = Database()
    app.run(debug=True)