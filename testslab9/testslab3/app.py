from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Простая "база" пользователей
USERS = {
    "admin": "password123",
    "user1": "pass123"
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username:
            error = "Поле «Имя пользователя» обязательно для заполнения."
        elif not password:
            error = "Поле «Пароль» обязательно для заполнения."
        elif username not in USERS or USERS[username] != password:
            error = "Неверное имя пользователя или пароль."
        else:
            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)