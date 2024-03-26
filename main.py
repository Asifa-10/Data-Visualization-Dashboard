from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sql'
db = SQLAlchemy(app)


# Define your database model here
class mytable(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # Define your table columns here
    url = db.Column(db.String(80), primary_key= True)
    region = db.Column(db.String(80), unique=False, nullable=True)
    start_year = db.Column(db.Integer, unique=False, nullable=True)


# Routes and other configurations will be added here
@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/api/data')
def get_data():
    # Query SQLite database and return data as JSON
    data = mytable.query.all()
    # Convert data to JSON format

    json_data = [{'url': x.url, 'region': x.region,'start_year':x.start_year} for x in data]
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
