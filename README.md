
# Wallet Manager

A Flask-based wallet management application designed to track and manage financial transactions with ease. This application includes user registration, wallet creation, transaction management, and an intuitive API interface for seamless interaction.

## Features

- **User Management**: Create, retrieve, and manage users.
- **Wallet Management**: Create and manage wallets for different users.
- **Transaction Handling**: Perform and track wallet transactions.
- **Error Handling**: Custom error handling for consistent API responses.
- **Environment Configuration**: Environment-based configurations with `dotenv`.

## Project Structure

```plaintext
wallet-manager/
├── app/
│   ├── __init__.py          # Application factory and database setup
│   ├── errors.py            # Custom error handling
│   ├── models.py            # Database models for users, wallets, transactions
│   └── routes.py            # API routes for the wallet management system
├── config.py                # Configuration settings
├── main.py                  # Entry point of the application
└── requirements.txt         # Project dependencies
```

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- PostgreSQL (for database)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Bahram03/wallet-manager.git
    cd wallet-manager
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the environment**:

    - Create a `.env` file in the root directory.
    - Define the following environment variables:

    ```plaintext
    FLASK_APP=main.py
    FLASK_ENV=development
    DATABASE_URL=postgresql://username:password@localhost/dbname
    SECRET_KEY=your_secret_key
    ```

5. **Initialize the database**:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

### Running the Application

To start the Flask application, use:

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### User Endpoints

- `POST /users` - Create a new user
- `GET /users/<id>` - Retrieve a user's details

### Wallet Endpoints

- `POST /wallets` - Create a new wallet for a user
- `GET /wallets/<id>` - Retrieve wallet information

### Transaction Endpoints

- `POST /transactions` - Perform a transaction between wallets
- `GET /transactions/<id>` - Retrieve transaction details

## Error Handling

All errors are handled consistently and return JSON responses with the following format:

```json
{
  "error": "Error message",
  "status_code": 400
}
```

## Dependencies

All dependencies are listed in `requirements.txt`:

```plaintext
Flask==2.2.2
Flask-Migrate==3.1.0
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
psycopg2-binary==2.9.3
python-dateutil==2.8.2
python-dotenv==0.21.0
WTForms==3.0.1
```

## License

This project is licensed under the MIT License.
