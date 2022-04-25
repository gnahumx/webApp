from flask import Flask, redirect, url_for, render_template, request
from forms import Persona

app = Flask(__name__)


app.secret_key = "LmCOWJ~fj3PnfHTJp"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/top')
def top():
    return render_template('top.html')


@app.route('/contacto', methods=["GET", "POST"])
def contacto():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    lugar = request.form.get("lugar")
    return render_template('contacto.html', nombre=nombre, email=email, lugar=lugar)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        return f"nombre={ request.form['nombre'] } | correo={ request.form['correo'] } | lugar={ request.form['lugar'] }"
    return render_template("form.html")


@app.route("/form-objeto", methods=["GET", "POST"])
def form_objeto():
    form = Persona()
    if form.validate_on_submit():
        return f"nombre={ request.form['nombre'] } | correo={ request.form['correo'] }"
    return render_template("form-objeto.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
