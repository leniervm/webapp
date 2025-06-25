import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html', title="Dashboard")

@app.route('/login')
def login():
    return render_template('pages/auth/auth-login.html', title="Inicio de Sesión")

@app.route('/register')
def register():
    return render_template('pages/auth/auth-register.html', title="Regístrate")

@app.route('/recoverpw')
def recoverpw():
    return render_template('pages/auth/auth-recoverpw.html', title="Recupera tu contraseña")

@app.route('/confirm_mail')
def confirm_mail():
    return render_template('pages/auth/auth-confirm_mail.html', title="Confirma tu email")    

@app.route('/lock_screen')
def lock_screen():
    return render_template('pages/auth/auth-lock_screen.html', title="Lock screen")

@app.route('/logout')
def logout():
    return render_template('pages/auth/auth-logout.html', title="Sesión cerrada")

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
