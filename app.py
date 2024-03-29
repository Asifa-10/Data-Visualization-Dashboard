from flask import Flask, render_template

app = Flask(__name__)

# Dashboard route
@app.route('/dashboard')
def dashboard():
    # Logic to fetch data from backend and pass it to the template
    data = {
        'title': 'Backend Dashboard',
        'stats': {
            'users': 100,
            'orders': 500,
            'revenue': 100000
        }
    }
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)