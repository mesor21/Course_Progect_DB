from flask import Flask, render_template, request, redirect, url_for
from DBconnect import Database

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')
# _______________________________

@app.route('/edit')
def edit_page():
    return render_template('./data/edit.html')

# ========
#   JobTitle
# ========
@app.route('/edit/jobTitle')
def list_jobTitle():
    posts = connect.get_jobTitle_list()
    return render_template('./data/jobTitle/list.html', posts=posts)

@app.route('/edit/jobTitle/<int:jobTitle_id>')
def edit_jobTitle(jobTitle_id):
    jobTitle = connect.get_jobTitle_by_id(jobTitle_id)
    if jobTitle is None:
        return "Запись не найдена"
    return render_template('/data/jobTitle/edit.html', jobTitle=jobTitle)

@app.route('/edit/jobTitle/<int:jobTitle_id>', methods=['POST'])
def update_jobTitle(jobTitle_id):
    new_post_name = request.form['PostName']
    new_salary = request.form['Salary']
    connect.update_jobTitle((new_post_name, new_salary, jobTitle_id))
    return redirect(url_for('list_jobTitle'))

@app.route('/edit/jobTitle/delete/<int:jobTitle_id>')
def delete_jobTitle(jobTitle_id):
    connect.delete_jobTitle(jobTitle_id)
    return redirect(url_for('list_jobTitle'))


@app.route('/edit/jobTitle/add', methods=['GET', 'POST'])
def add_jobTitle():
    if request.method == 'POST':
        new_post_name = request.form['PostName']
        new_salary = request.form['Salary']
        connect.add_jobTitle((new_post_name, new_salary))
        return redirect(url_for('list_jobTitle'))
    else:
        jobTitle = {
            'postName': '',
            'salary': ''
        }
        return render_template('/data/jobTitle/add.html', jobTitle=jobTitle)

# ========
#   Department
# ========
@app.route('/edit/department')
def list_department():
    departments = connect.get_department_list()
    return render_template('./data/department/list.html', departments=departments)

@app.route('/edit/department/add', methods=['GET', 'POST'])
def add_department():
    if request.method == 'POST':
        name = request.form['name']
        connect.add_department((name,))
        return redirect(url_for('list_department'))
    return render_template('./data/department/add.html')

@app.route('/edit/department/delete/<int:department_id>')
def delete_department(department_id):
    connect.delete_department(department_id)
    return redirect(url_for('list_department'))

@app.route('/edit/department/<int:department_id>', methods=['GET', 'POST'])
def update_department(department_id):
    if request.method == 'POST':
        name = request.form['name']
        connect.update_department((name, department_id))
        return redirect(url_for('list_department'))

    department = connect.get_department_by_id(department_id)
    return render_template('./data/department/edit.html', department=department)

# ==========
#   DriverCategory
# ==========
@app.route('/edit/driverCategory')
def list_driver_category():
    driver_categories = connect.get_driver_category_list()
    return render_template('./data/driverCategory/list.html', driver_categories=driver_categories)

@app.route('/edit/driverCategory/add', methods=['GET', 'POST'])
def add_driver_category():
    if request.method == 'POST':
        category = request.form['category']
        connect.add_driver_category((category,))
        return redirect(url_for('list_driver_category'))
    return render_template('./data/driverCategory/add.html')

@app.route('/edit/driverCategory/delete/<int:driver_category_id>')
def delete_driver_category(driver_category_id):
    connect.delete_driver_category(driver_category_id)
    return redirect(url_for('list_driver_category'))

@app.route('/edit/driverCategory/<int:driver_category_id>', methods=['GET', 'POST'])
def update_driver_category(driver_category_id):
    if request.method == 'POST':
        category = request.form['category']
        connect.update_driver_category((category, driver_category_id))
        return redirect(url_for('list_driver_category'))

    driver_category = connect.get_driver_category_by_id(driver_category_id)
    return render_template('./data/driverCategory/edit.html', driver_category=driver_category)

# ==========
#   Employee
# ==========
@app.route('/edit/employee')
def list_employee():
    employee = connect.get_employee_list()
    return render_template('./data/employee/list.html', employees=employee)


@app.route('/edit/employee/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        second_name = request.form['secondName']
        last_name = request.form['LastName']
        post_id = request.form['jobTitle']
        department_id = request.form['department']
        driver_category_id = request.form['driverCategory']

        connect.add_employee((name, second_name, last_name, post_id, driver_category_id, department_id))
        return redirect(url_for('list_employee'))

    # Получите списки должностей, отделов и категорий водителей
    posts = connect.get_jobTitle_list()
    departments = connect.get_department_list()
    driver_categories = connect.get_driver_category_list()

    return render_template('./data/employee/add.html', posts=posts, departments=departments,
                           driver_categories=driver_categories)


@app.route('/edit/employee/<int:employee_id>', methods=['GET', 'POST'])
def update_employee(employee_id):
    if request.method == 'POST':
        updated_name = request.form['name']
        updated_second_name = request.form['secondName']
        updated_last_name = request.form['LastName']
        updated_post_id = request.form['jobTitle']
        updated_department_id = request.form['department']
        updated_driver_category_id = request.form['driverCategory']

        connect.update_employee((updated_name, updated_second_name, updated_last_name, updated_post_id,
                                 updated_driver_category_id, updated_department_id, employee_id))
        return redirect(url_for('list_employee'))

    employee = connect.get_employee_by_id(employee_id)
    posts = connect.get_jobTitle_list()
    departments = connect.get_department_list()
    driver_categories = connect.get_driver_category_list()
    return render_template('./data/employee/edit.html', employee=employee, posts=posts, departments=departments,
                           driver_categories=driver_categories)
@app.route('/edit/employee/delete/<int:employee_id>')
def delete_employee(employee_id):
    connect.delete_employee(employee_id)
    return redirect(url_for('list_employee'))

# ==========
#   routes
# ==========
@app.route('/edit/routes')
def list_routes():
    routes = connect.get_routes_list()
    return render_template('./data/routes/list.html', routes=routes)

@app.route('/edit/routes/add', methods=['GET', 'POST'])
def add_route():
    if request.method == 'POST':
        number = request.form['number']
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        departure_time = request.form['departure_time']
        arrival_time = request.form['arrival_time']

        connect.add_route((number, from_location, to_location, departure_time, arrival_time))
        return redirect(url_for('list_routes'))

    return render_template('./data/routes/add.html')

@app.route('/edit/routes/delete/<int:route_id>')
def delete_route(route_id):
    connect.delete_route(route_id)
    return redirect(url_for('list_routes'))

@app.route('/edit/routes/<int:route_id>', methods=['GET', 'POST'])
def update_route(route_id):
    if request.method == 'POST':
        number = request.form['number']
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        departure_time = request.form['departure_time']
        arrival_time = request.form['arrival_time']

        connect.update_route((number, from_location, to_location, departure_time, arrival_time, route_id))
        return redirect(url_for('list_routes'))

    route = connect.get_route_by_id(route_id)
    return render_template('./data/routes/edit.html', route=route)

# ========
#   Brand
# ========
@app.route('/edit/brand')
def list_brand():
    brands = connect.get_brand_list()
    return render_template('./data/brand/list.html', brands=brands)

@app.route('/edit/brand/add', methods=['GET', 'POST'])
def add_brand():
    if request.method == 'POST':
        name = request.form['name']
        brand_id = connect.add_brand({'Name': name})
        if brand_id is not None:
            return redirect(url_for('list_brand'))
        else:
            # Обработка ошибки, если вставка не удалась
            pass
    return render_template('./data/brand/add.html')

@app.route('/edit/brand/delete/<int:brand_id>')
def delete_brand(brand_id):
    connect.delete_brand(brand_id)
    return redirect(url_for('list_brand'))

@app.route('/edit/brand/<int:brand_id>', methods=['GET', 'POST'])
def update_brand(brand_id):
    if request.method == 'POST':
        name = request.form['name']
        connect.update_brand({'Name': name, 'BrandID': brand_id})
        return redirect(url_for('list_brand'))

    brand = connect.get_brand_by_id(brand_id)
    return render_template('./data/brand/edit.html', brand=brand)


# ==========
#   bus
# ==========
@app.route('/edit/bus')
def list_bus():
    buses = connect.get_bus_list()
    return render_template('./data/bus/list.html', buses=buses)

@app.route('/edit/bus/add', methods=['GET', 'POST'])
def add_bus():
    if request.method == 'POST':
        state_number = request.form['stateNumber']
        vin = request.form['vin']
        brand_id = request.form['brand']
        num_of_people = request.form['numOfPeople']

        connect.add_bus((state_number, vin, brand_id, num_of_people))
        return redirect(url_for('list_bus'))

    # Получите список брендов (Brand) для выпадающего списка
    brands = connect.get_brand_list()

    return render_template('./data/bus/add.html', brands=brands)

@app.route('/edit/bus/<int:bus_id>', methods=['GET', 'POST'])
def update_bus(bus_id):
    if request.method == 'POST':
        updated_state_number = request.form['stateNumber']
        updated_vin = request.form['vin']
        updated_brand_id = request.form['brand']
        updated_num_of_people = request.form['numOfPeople']

        connect.update_bus((updated_state_number, updated_vin, updated_brand_id, updated_num_of_people, bus_id))
        return redirect(url_for('list_bus'))

    bus = connect.get_bus_by_id(bus_id)
    brands = connect.get_brand_list()
    return render_template('./data/bus/edit.html', bus=bus, brands=brands)

@app.route('/edit/bus/delete/<int:bus_id>')
def delete_bus(bus_id):
    connect.delete_bus(bus_id)
    return redirect(url_for('list_bus'))

# ___________________________________

@app.route('/compose_routes')
def compose_routes():
    return render_template('./data/compose_routes.html')
# ___________________________________
@app.route('/queries')
def queries_page():
    return render_template('./data/queries.html')


if __name__ == '__main__':
    connect = Database()
    app.run(debug=True)