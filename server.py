from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from functionalities.validate_email import validar_correo
from app import (
    app,
    db,
    Usuario,
    genre,
    platform,
    Publisher,
    game,
    Compra,
    Publisher,
    Game_publisher,
    Game_platform
)

migrate = Migrate(app, db)

login_val = False
email = ''
password = ''
nombre = ''
apellido = ''
bio = ''
compra = False


@app.route('/', methods=['GET'])
def principal():
    global login_val

    if login_val:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

# Todo referente al login va aqui


@app.route('/login', methods=['GET'])
def login():
    global login_val
    if login_val:
        return redirect(url_for('principal'))
    else:
        return render_template('login.html')


@app.route('/data_login', methods=['POST'])
def data_login():
    global login_val, email, password, nombre, apellido, bio

    email = request.form['email']
    password = request.form['password']

    # Buscar el usuario en la base de datos
    user = Usuario.query.filter_by(email=email).first()

    if user:
        if user.email == email and user.password == password:
            login_val = True
            email = user.email
            password = user.password
            nombre = user.firstname
            apellido = user.lastname
            bio = user.bio
            return jsonify({'success': True,
                            'message':'Inicio de sesion correcto'}),200
        else:
            return jsonify({'success': False,
                            'message':'Correo y/o contraseña incorrectos. Intente nuevamente &#128577;'}),400
    else:
        return jsonify({'success': False,
                        'message':'Este usuario no está registrado &#128577;'}),400


@app.route('/logout', methods=['GET'])
def logout():
    global login_val, email, password, nombre, apellido, bio
    if login_val:
        login_val = False
        email = ''
        password = ''
        nombre = ''
        apellido = ''
        bio = ''

    return redirect(url_for('login'))


# Todo referente al login va aqui

# Todo referente al "recuperar contrasenia" va aqui

@app.route('/recover_password', methods=['GET'])
def recover_password():
    return render_template('recover_password.html')


@app.route('/data_recover', methods=['POST'])
def data_recover():
    global email, password

    email = request.form['email']
    name = request.form['name']

    # Buscar el usuario en la base de datos
    user = Usuario.query.filter_by(email=email).first()

    if email == user.email and name == user.firstname:
        return jsonify({'success': True,
                        'message': 'El usuario y nombre coinciden'}), 200
    else:
        return jsonify({'success': False,
                        'message': 'Datos de acceso incorrectos. Intente nuevamente &#128577;'}), 400


@app.route('/reset_password', methods=['POST'])
def reset_password():
    global password

    password1 = request.form['password1']
    password2 = request.form['password2']

    if password1 == password2:
        user = Usuario.query.filter_by(email=email).first()
        password = password1
        user.password = password
        db.session.commit()
        return jsonify({'success': True,
                        'message': 'Cambio de contraseña correcto'}), 200
    else:
        return jsonify({'success': False,
                        'message': 'Las contraseñas no coinciden &#128577;'}), 400

# Todo referente al "recuperar contrasenia" va aqui

# Todo referente al "Nuevo usuario" va aqui


@app.route('/new_user', methods=['GET'])
def new_user():
    return render_template('register.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    global login_val, nombre, apellido, email, password, bio
    name = request.form['name']
    lastname = request.form['lastname']
    biog = request.form['bio']
    e_mail = request.form['email']
    password1 = request.form['password']

    if validar_correo(e_mail):
        login_val = True
        nombre = name
        apellido = lastname
        email = e_mail
        password = password1
        bio = biog
        new_user = Usuario(firstname=name, lastname=lastname,  email=e_mail,
                           bio=biog, password=password1)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True,
                        'message': 'El correo ingresado es válido &#128577;'}), 200
    else:
        return jsonify({'success': False,
                        'message': 'El correo ingresado no es válido &#128577;'}), 400

# Todo referente al "Nuevo usuario" va aqui

# Todo referente a la pagina de "profile" va aqui


@app.route('/profile', methods=['GET'])
def profile():
    if login_val:
        return render_template('user.html')
    else:
        return redirect(url_for('principal'))


@app.route('/get_profile', methods=['GET'])
def get_profile():
    user = Usuario.query.filter_by(email=email)[0]
    return jsonify({"success": True, 'user': user.serialize()}), 200

# Todo referente a la pagina de "delete-user" va aqui


@app.route('/delete_user', methods=['POST'])
def delete_user():
    global nombre, apellido, bio, email, password, login_val
    fila_a_eliminar = Usuario.query.filter_by(email=email).first()

    if fila_a_eliminar:
        db.session.delete(fila_a_eliminar)
        db.session.commit()
        login_val = False
        nombre = ''
        apellido = ''
        bio = ''
        email = ''
        password = ''
        return jsonify({'success': True,
                        'message': 'El usuario se ha eliminado correctamete.'}), 200
    else:
        return jsonify({'success': False,
                        'message': 'El usuario no se ha podido eliminar. Intentalo nuevamente'}), 400

# Todo referente a la pagina de "actualizar_datos" va aqui


@app.route('/update_data', methods=['POST'])
def update_data():

    global nombre, apellido, bio, email, password

    user = Usuario.query.filter_by(email=email).first()

    nombre = request.form['username']
    apellido = request.form['lastname']
    bio = request.form['bio']
    email = request.form['email']
    password = request.form['password']

    user.firstname = nombre
    user.lastname = apellido
    user.bio = bio
    user.email = email
    user.password = password

    db.session.commit()

    return redirect(url_for('principal'))


# Todo referente a la pagina de "videogame" va aqui


@app.route('/get_videogame', methods=['GET'])
def get_videogame():
    id_game = request.args("id")

    game_platform = game.query.filter_by(id=id_game)[0].game_publisher.game_platform.serialize()
    return jsonify({"success": True, 'game_platform': game_platform}), 200


@app.route('/videogame', methods=['GET'])
def videogame():
    return render_template('game.html')


# Todo referente a la pagina de "search" va aqui


@app.route('/get_genre', methods=['GET'])
def get_genre():
    genres = [g.serialize for g in genre.query.all()]
    return jsonify({"success": True, 'elementos': genres}), 200


@app.route('/get_platform', methods=['GET'])
def get_platform():
    platforms = [p.serialize for p in platform.query.all()]
    return jsonify({"success": True, 'elementos': platforms}), 200


@app.route('/get_publisher', methods=['GET'])
def get_publisher():
    publishers = [p.serialize for p in Publisher.query.all()]
    return jsonify({"success": True, 'elementos': publishers}), 200


@app.route('/do_search', methods=['GET'])
def do_search():
    # 1. Usar search params para obtener las categorias de busqueda. Su nombre
    # estan en search.js, especificamente es: genre, platform, publisher y
    # name. Por default el valor es Todas.
    # 2. Hacer un if por cada categoria para verificar si el valor es Todas.
    # Si es asi, se escoje a todos los posibles, ya que eso se significa Todas.
    # Caso contrario, se hace un querry con el valor de la categoria.
    # 3. Luego de tener la lista de coincidencias de cada categoria deberias
    # hacer que llegen a su forma de game.
    # 4. En su forma de game, debes hacer una interseccion entre las 4 para
    # encontrar los juegos que coinciden con todo. Estoy recomendado que lo
    # lleves a su forma de game, pero no se si la comparacion funcionara bien.
    # Tambien lo podrias hacer por su game id y despues de tener la
    # interseccion llevarlo a su forma de game.
    # 5. Hacer un serialize para cada objeto game encontrado, guardarlo en una
    # lista.
    # 6. Regresar un jsonify para indicar si funciono y con la lista del paso
    # 5. Seria bueno que todo este dentro de un try. Te puedes guiar del
    # get_departments del ejercicio del profesor.
    return


@app.route('/search', methods=['GET'])
def search():
    global login_val
    if login_val:
        return render_template('search.html')
    else:
        return redirect(url_for('principal'))


@app.route('/purchases', methods=['GET'])
def purchases():
    global login_val
    if login_val:
        return render_template('purchases.html')
    else:
        return redirect(url_for('principal'))


@app.route('/buy_game', methods=['POST'])
def verify_checkout():
    global compra
    compra = True
    return jsonify({'success': True, 'message': 'Compra casi lista'})


@app.route('/checkout', methods=['GET'])
def checkout():
    global compra
    if compra:
        return render_template('wait.html')
    else:
        return redirect(url_for('principal'))


@app.route('/resume', methods=['GET'])
def resume():
    global compra
    if compra:
        compra = False
        return render_template('resume.html')
    else:
        return redirect(url_for('principal'))
    
@app.route('/get_purchase_resume', methods = ['GET'])
def get_purchase_resume():
    #Se debe de devolver los datos de la compra realizada
    return

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))
