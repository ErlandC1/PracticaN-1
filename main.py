from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerca')
def about():
    return render_template('acerca.html')

@app.route('/servicios')
def services():
    return render_template('servicios.html')

@app.route('/noticias')
def news():
    return render_template('noticias.html')

@app.route('/contactos', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['nombre']
        email = request.form['email']
        message = request.form['mensaje']
        # Aquí puedes manejar el envío del formulario
        return render_template('contactos.html', success=True)
    return render_template('contactos.html')

if __name__ == '__main__':
    app.run(debug=True)