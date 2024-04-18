from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="courier_system"
)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Booking form route
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Retrieve form data
        sender_name = request.form['senderName']
        receiver_name = request.form['receiverName']
        pickup_address = request.form['pickupAddress']
        delivery_address = request.form['deliveryAddress']

        # Save form data to the database (insert query)
        cursor = db.cursor()
        query = "INSERT INTO parcels (sender_name, receiver_name, pickup_address, delivery_address, status) VALUES (%s, %s, %s, %s, %s)"
        values = (sender_name, receiver_name, pickup_address, delivery_address, "Pending")
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('index'))

    return render_template('booking.html')

# Status update form route
@app.route('/status_update', methods=['GET', 'POST'])
def status_update():
    if request.method == 'POST':
        # Retrieve form data
        parcel_id = request.form['parcelID']
        status = request.form['status']

        # Update status in the database (update query)
        cursor = db.cursor()
        query = "UPDATE parcels SET status = %s WHERE parcel_id = %s"
        values = (status, parcel_id)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('index'))

    return render_template('status_update.html')

# Feedback form route
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save feedback to the database (insert query)
        cursor = db.cursor()
        query = "INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('index'))

    return render_template('feedback.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Here, you can implement your own logic to check the username and password
    # against a database or any other authentication mechanism
    # For simplicity, let's assume the username is 'admin' and password is 'password'
    if username == 'admin' and password == 'password':
        return redirect('/dashboard')
    else:
        return render_template('login.html', error=True)

# Dashboard route
@app.route('/dashboard')
def dashboard():
    # Here, you can render the dashboard template
    # and perform any necessary operations for the logged-in user
    return render_template('dashboard.html', username='admin')

if __name__ == '__main__':
    app.run(debug=True)
