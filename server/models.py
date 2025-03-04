from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Metadata object to store table definitions and schema information
metadata = MetaData()

# Initialize the database instance using SQLAlchemy
db = SQLAlchemy(metadata=metadata)

# Define the Pet model, which maps to the 'pets' table in the database
class Pet(db.Model):
    __tablename__ = 'pets'  # Specifies the name of the database table

    # Unique identifier for each pet (Primary Key)
    id = db.Column(db.Integer, primary_key=True)

    # Name of the pet (Required, maximum length: 80 characters)
    name = db.Column(db.String(80), nullable=False)

    # Species of the pet (e.g., Dog, Cat, Bird) (Required, maximum length: 80 characters)
    species = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        """Returns a string representation of a Pet instance, useful for debugging."""
        return f"<Pet id={self.id}, name={self.name}, species={self.species}>"
