# Easily handle authentication in Django tests - Code Repository
This repository contains the code used in the [Easily handle authentication in Django tests](https://isilviu.com/blog/easily-handle-authentication-in-django-tests/). The code is organized in a way that matches the structure of the article and is designed to help readers understand and replicate the results described in the article.

## Getting Started
These instructions will get you a copy of the code up and running on your local machine for development and testing purposes.

### Prerequisites
You will need to have the following software installed on your computer: `python3`. For the tutorial, I've used `python 3.9.6`.

### Installing
1. Clone the repository to your local machine
```bash
git clone https://github.com/ISilviu/authentication-django-tests
```

2. Navigate into the repository
```bash
cd authentication-django-tests
```

3. Create the python virtual environment and activate it
```bash
python3 -m venv env
source env/bin/activate
```

4. Install the required dependencies
```bash
Copy code
pip install -r requirements.txt
```

5. Run the application
```bash
python manage.py runserver
```

6. Run the tests
```bash
python manage.py test
```

### Contributing
If you'd like to contribute to this repository, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the changes.
4. Commit your changes and push to your fork.
5. Submit a pull request to the repository.