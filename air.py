from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/book')
def book():
    return render_template("book.html")

@app.route('/service', methods=['GET', 'POST'])
def service():
   return render_template("service.html")


# Flight Status Page
@app.route('/status')
def status():
    return render_template("status.html")

# Terminal Info Page
@app.route('/terminal')
def terminal():
    return render_template("terminal.html")

# Flight report and lost
@app.route('/report')
def report():
    return render_template("report.html")

# Admin Dashboard Page
@app.route('/admin')
def admin():
    return render_template("admin.html")

# About Page
@app.route('/bookedtickets')
def about():
    return render_template("bookedtickets.html")

# Available Flights Page
@app.route('/available')
def flights():
    return render_template("available.html")

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
