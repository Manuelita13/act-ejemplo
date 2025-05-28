from flask import Flask, render_template, request

app = Flask(__name__)

datos = []  # Variable global

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        datos.append({'nombre': nombre, 'apellido': apellido, 'edad': edad})
    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
    
    {3r5gkinitñrh.lgjhn.lhok}