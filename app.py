from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import os
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# MongoDB configuration
client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017/'))
db = client['nerd']
users = db['users']
orders = db['orders']

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        login_user = users.find_one({'username': username})

        if login_user and check_password_hash(login_user['password'], password):
            session['username'] = username
            session['role'] = login_user['role']
            return redirect(url_for('index'))
        
        flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        
        if users.find_one({'username': username}):
            flash('Username already exists')
        else:
            hashed_password = generate_password_hash(password)
            users.insert_one({
                'username': username,
                'password': hashed_password,
                'role': role
            })
            flash('Registration successful. Please log in.')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/index')
def index():
    if 'username' in session:
        user_role = session.get('role')
        username = session.get('username')
        return render_template('index.html', user_role=user_role, username=username)
    return redirect(url_for('login'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'username' in session and session.get('role') == 'admin':
        return render_template('admin_dashboard.html')
    flash('Access denied. Admins only.')
    return redirect(url_for('login'))

@app.route('/user_dashboard')
def user_dashboard():
    if 'username' in session and session.get('role') == 'user':
        return 'Welcome to the user dashboard, {}'.format(session['username'])
    flash('Access denied. Users only.')
    return redirect(url_for('login'))

@app.route('/electronics')
def electronics():
    if 'username' in session:
        return render_template('electronics.html')
    flash('You need to log in to access this page.')
    return redirect(url_for('login'))

@app.route('/fashion')
def fashion():
    if 'username' in session:
        return render_template('fashion.html')
    flash('You need to log in to access this page.')
    return redirect(url_for('login'))

@app.route('/addtocart')
def addtocart():
    if 'username' in session:
        return render_template('addtocart.html')
    flash('You need to log in to access this page.')
    return redirect(url_for('login'))

@app.route('/beauty')
def beauty():
    if 'username' in session:
        return render_template('beauty.html')
    flash('You need to log in to access this page.')
    return redirect(url_for('login'))

@app.route('/collection')
def collection():
    if 'username' in session:
        return render_template('collection.html')  # Use relative path for the template
    flash('You need to log in to access this page.')
    return redirect(url_for('login'))

@app.route('/myorders')
def myorders():
    if 'username' in session:
        username = session.get('username')
        user_orders_cursor = orders.find({'username': username})
        user_orders = list(user_orders_cursor)  # Convert cursor to list
        return render_template('myorders.html', orders=user_orders)
    flash('You need to log in to access this page.')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/product_details')
def product_details():
    return render_template('product_details.html')

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
    app.run(debug=True)
