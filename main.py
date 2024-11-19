from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')  # Renderiza el archivo HTML desde la carpeta templates

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/ver')
def ver():
    return render_template("ver.html")

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/editar/modificar')
def nuevo_elemento():
    return render_template('modificar.html')


if __name__ == '__main__':
    app.run(debug=True)
