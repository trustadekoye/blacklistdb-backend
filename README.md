# BlacklistDB Backend

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL 12+

### Installation

1. Clone the repository

```bash
git clone https://github.com/trustadekoye/blacklistdb-backend.git
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add the following variables in the .env.example file

4. Run the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the server

```bash
python manage.py runserver
```

## Structure

The project is structured as follows:

```
.
├── README.md
├── requirements.txt
├── server
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── migrations
│       └── __init__.py
├── scammers
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations
│       └── __init__.py
├── manage.py
├── supabase_client.py

```
