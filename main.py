import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/auth/auth-login.html', title="Inicio de Sesión")

@app.route('/')
def login():
    return render_template('pages/auth/auth-login.html', title="Inicio de Sesión")

@app.route('/register')
def register():
    return render_template('pages/auth/auth-register.html', title="Regístrate")

@app.route('/recoverpw')
def recoverpw():
    return render_template('pages/auth/auth-recoverpw.html', title="Recupera tu contraseña")    

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
