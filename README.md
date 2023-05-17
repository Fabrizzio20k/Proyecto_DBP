<a name="readme-top"></a>

<div align="center">
  <a href="https://github.com/CS1103/proyecto-final-2023_0-proyecto-final-2023_0-grupo-5">
    <img src="static/logo/logo_2.png" alt="hex board" width="300" height="100">
  </a>
  <h1>👾 GPT VIDEOGAMES 👾</h1>
  
  <p>
  Este proyecto ha sido desarrollado por estudiantes del curso de Desarrollo Basado en Plataformas
de la Universidad de Ingeniería y Tecnología 💙🤍. Esperemos les guste. 🎮
    
  </p>
</div>

<details open>
  <summary>Índice:</summary>
  <ol>
    <li><a href="#integrantes">
      Integrantes
    </a></li>
    <li><a href="#acerca-del-proyecto">
      Acerca del proyecto
      <ul>
        <li><a href="#descripción">Descripción</a></li>
        <li><a href="#objetivos-principales">Objetivos Principales</a></li>
        <li><a href="#librerías-framworks-y-plugins">Librerías, Frameworks y Plugins</a></li>
        <li><a href="#script">Script</a></li>
        <li><a href="#hosts">Hosts</a></li>
        <li><a href="#manejo-de-errores-http">Manejo de Errores HTTP</a></li>
        <li><a href="#ejecución-del-sistema">Ejecución del Sistema</a></li>
      </ul>
    </a></li>
  </ol>
</details>

---

## Integrantes

- Piero Jesus Guerrero Jimenez				
- Fabrizzio Nicolay Vilchez Espinoza				
- Manuel Jesus Silva 				
- Ariana Vega Huamán				 

## Acerca del proyecto

### Descripción

Este proyecto consiste en el desarrollo de una aplicación virtual llamada GPT VIDEOGAMES,
la cual consiste en vender videojuegos de manera virtual, ya sea por marcas, plataformas o categorías.

### Objetivos Principales

#### Misión

Esta página tiene como misión llegar a ser de total comodidad para el cliente y cumplirlo ofreciendo videojuegos de alta calidad.

#### Visión

La visión de esta página es ser una de las plataformas líderes en la industria de entretenimiento electrónico y afines en el Perú.

### Librerías, Frameworks y Plugins

Front-end:
- Flask: Estamos usando flask para servir datos. En este caso, se devuelven respuestas en formato JSON para ser trabajadas por JavaScript.
- Fetch: Fetch es una función integrada en JavaScript que permite realizar solicitudes HTTP desde el navegador. Proporciona una forma moderna y flexible de hacer peticiones a servidores web, obtener datos y manejar respuestas. Fetch es fácil de usar y compatible con Promises, lo que facilita el manejo de datos asíncronos en el frontend.

Back-end:
- Flask: Flask es un framework ligero de desarrollo web en Python que permite crear aplicaciones web rápidas y eficientes. Proporciona herramientas y bibliotecas para manejar solicitudes HTTP, enrutar URL, generar respuestas dinámicas y gestionar bases de datos. Flask es altamente personalizable y fácil de aprender, lo que lo convierte en una elección popular para desarrolladores de backend. Se usa en este proyecto para manejar las solicitudes a la base de datos y algunas operaciones de verificación.

- SQLAlchemy: SQLAlchemy es una biblioteca de mapeo objeto-relacional en Python que facilita la interacción con bases de datos relacionales. Proporciona una capa de abstracción que permite interactuar con la base de datos utilizando objetos y consultas en lugar de escribir consultas SQL directamente. SQLAlchemy simplifica el manejo de la persistencia de datos y la creación de consultas complejas.
- SMTPLIB: La biblioteca smtplib de Python se utiliza para enviar correos electrónicos a través de un servidor SMTP. Primero, se establece una conexión con el servidor utilizando smtplib.SMTP, luego se autentica con credenciales y se envía el correo utilizando sendmail. Todo esto se usa para enviar correos al usuario al final de la compra.

Base de Datos:
- Flask_migrate
- SQLAlchemy

### Script

Para cargar las bases de datos se ejecuta:
```sh
./load.sh
```
- Se debe estar dentro del repositorio, en el mismo nivel que app.py.
- Dentro del script, primero se ejecuta python app.py, para crear las bases de datos. -
- Luego de cargar, se debe cancelar con Ctr+c.
- Después, se usa ejecuta el código de los sql scripts encontrados dentro de la carpate /sql. Estos llenan las tablas de la base de datos con los datos de los videojuegos.

### Hosts

Local host 5000

### Manejo de Errores HTTP

- Para la sección del login del usuario, el servidor responde con código 400 si el usuario no existe o la contraseña es incorrecta, y 200 si es que todo ha ido bien.
- Para la sección de recuperar constraseña, el servidor responde con código 400 si al momento de verificar las credenciales del usuario estas no coinciden, o con código 200 si pasa lo contrario.
- Para la sección de crear usuario, el servidor responde con código 400 (BAD_REQUEST) si se trata de ingresar un correo ya registrado, o con código, o con código 200 si el registro es exitoso.
- Para la sección de busqueda, el servidor siempre responde con código 200, ya que el que encuentre resultados o no, no indica que la petición de busqueda no se haya realizado correctamente.
- Para la sección de compra, el servidor siempre responde con código 200, ya que lo único que se hace es una inserción de datos dentro de la base de datos con datos verificados en pasos anteriores.
- Para la sección de editar datos, el servidor siempre responde con código 200, ya que el único dato relevante para definir si hay un error o no al insertar datos en la base de datos es el correo, el cual ya esta restringido para edición desde el principio.
- Para la sección de compras realizadas por el usuario, el servidor siempre responde con código 200, ya que la petición de busqueda siempre se hace con los datos obtenido anteriormente, y lo único que varia es el contenido dentro del JSON que se devuelve.

### Ejecución del Sistema

Para ejecutar el sistema se tiene que correr server.py
