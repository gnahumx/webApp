from flask import Flask, render_template
#from flask_bootstrap import Bootstrap
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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
