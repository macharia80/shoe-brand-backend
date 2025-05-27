👟 Adidas Shoe Brand CLI App
A simple command-line interface (CLI) application to manage a database of Adidas shoes using Python, SQLAlchemy (ORM), and Click.

This app allows you to add, list, update, and delete shoe records from the command line. It uses SQLite by default , but can be configured for PostgreSQL if needed.

🧰 Features
Add new shoes to the database
List all shoes
Update shoe details by ID
Delete shoes by ID
Uses SQLAlchemy ORM for database interaction
Simple and easy-to-use CLI with click
📦 Requirements
Make sure you have these installed:

Python 3.7+
pip
Optional: PostgreSQL (if not using SQLite)
Install dependencies:
pip install sqlalchemy click psycopg2-binary python-dotenv

🛠 Setup Instructions
1. Clone the repository
git clone git@github.com:macharia80/shoe-brand-backend.git
cd adidas-shoe-cli

2. Install dependencies
pip install -r requirements.txt

3. Initialize the database
The first time you run the app, it will automatically create a SQLite database (shoe.db) and set up the required tables.

🚀 Usage
Run the CLI tool:
python cli.py --help

Available Commands:
🔹 Add a shoe
python cli.py add "Adidas" "Ultraboost 22" 9.5 190.0

🔹 List all shoes
python cli.py list

🔹 Update a shoe
python cli.py update 1 --brand Adidas --model Samba --size 10 --price 80

🔹 Delete a shoe
python cli.py delete 1

🗃️ Database Configuration
By default, this project uses SQLite with a local file named shoe.db.

To switch to PostgreSQL , update the DATABASE_URL in database.py:

DATABASE_URL = "postgresql://username:password@localhost:5432/shoedb"

Or use environment variables for better security:
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./shoe.db")

Then create a .env file:
DATABASE_URL=postgresql://sam:password@localhost:5432/shoedb

📁 Project Structure

adidas-shoe-cli/
│
├── cli.py             # Main CLI commands
├── models.py          # Shoe model definition
├── database.py        # DB setup and engine
├── requirements.txt   # Dependencies
└── README.md          # This file

✅ Contributing
Feel free to fork this repo, submit issues, or make pull requests!
