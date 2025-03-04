from flask import Flask
from flask_migrate import Migrate
from models import db  # Import the database instance from models.py

# Create a Flask application instance
app = Flask(__name__)

# Set up the database connection (using SQLite as the database engine)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Disable SQLAlchemy's modification tracking feature to reduce memory usage
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate to handle database migrations
migrate = Migrate(app, db)

# Link the database instance to the Flask app
db.init_app(app)

if __name__ == '__main__':
    # Start the Flask development server on port 5555 with debugging enabled
    app.run(port=5555, debug=True)
