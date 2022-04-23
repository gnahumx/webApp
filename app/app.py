from flask import Flask, render_template, request
from forms import Persona

app = Flask(__name__)
# Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/top')
def top():
    return render_template('top.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        return f"nombre={ request.form['nombre'] } | genero={ request.form['genero'] } | correo={ request.form['correo'] }"
    return render_template("form.html")


@app.route("/form-objeto", methods=["GET", "POST"])
def form_objeto():
    return render_template("form-objeto.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
