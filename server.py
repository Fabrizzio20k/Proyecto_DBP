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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/project_dbp'
db.init_app(app)

login_val = False
email = ''
password = ''
nombre = ''
apellido = ''
bio = ''


@app.route('/', methods=['GET'])
def principal():
    global login_val,nombre

    if login_val:
        return render_template('index.html',nombre=nombre)
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

    email=request.form['email']
    password=request.form['password']

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
            return jsonify({'success': True, 'message':'Inicio de sesion correcto'}),200
        else:
            return jsonify({'success': False, 'message':'Correo y/o contraseña incorrectos. Intente nuevamente &#128577;'}),400
    else:
        return jsonify({'success': False, 'message':'Este usuario no está registrado &#128577;'}),400

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

    if email == 'fabrizzio785@gmail.com' and name == 'Fabrizzio':
        return jsonify({'success': True, 'message': 'El usuario y nombre coinciden'}), 200
    else:
        return jsonify({'success': False, 'message': 'Datos de acceso incorrectos. Intente nuevamente &#128577;'}), 400


@app.route('/reset_password', methods=['POST'])
def reset_password():
    global password

    password1 = request.form['password1']
    password2 = request.form['password2']

    if password1 == password2:
        password = password1
        return jsonify({'success': True, 'message': 'Cambio de contraseña correcto'}), 200
    else:
        return jsonify({'success': False, 'message': 'Las contraseñas no coinciden &#128577;'}), 400

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
        new_user = Usuario(firstname=name ,lastname = lastname ,  email=e_mail, bio=biog , password= password1)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True, 'message': 'El correo ingresado es válido &#128577;'}), 200
    else:
        return jsonify({'success': False, 'message': 'El correo ingresado no es válido &#128577;'}), 400

# Todo referente al "Nuevo usuario" va aqui

# Todo referente a la pagina de "profile" va aqui


@app.route('/profile', methods=['GET'])
def profile():
    # 1. Hacer un querry para obtener el usuario. Como estamos guardando su
    # informacion, puedes usar eso.
    # 2. Regresar un jsonify con el usuario luego de un serialize.
    # Como ya se verifica que exista el usuario en el login, no deberia fallar,
    # asi que tu decide si pones un try
    return


# Todo referente a la pagina de "videogame" va aqui


@app.route('/videogame', methods=['GET'])
def videogame():
    # 1. Usar search params para obtener el titulo del game
    # 1. Hacer un querry para obtener el game
    # 2. Regresar un jsonify con el game luego de un serialize.
    # No deberia fallar, ya que los videojuegos que aparecen son de la base de datos
    return


# Todo referente a la pagina de "search" va aqui


@app.route('/search', methods=['GET'])
def search():
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


if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))
