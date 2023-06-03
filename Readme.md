# django-boilerplate

This is a Django boilerplate project with Docker setup, CI/CD integration, logging, and tests.

## Prerequisites
- Docker
- Python 3.9 (if not using Docker)

## Getting Started

1. Clone the repository:
git clone https://github.com/sakshishreyaa/django-boilerplate.git
cd django-boilerplate

2. Docker Setup:
- Build the Docker image and start the development server:
  ```
  docker-compose up --build
  ```
- Access the application at `http://localhost:8000`

(Alternatively, you can run the application without Docker by installing the dependencies and running the Django development server locally.)

3. Development Workflow:
- Make changes to the Django project files (e.g., views, models, templates) located in the `myproject` directory.
- The development server will automatically reload on file changes.

4. Creating and Configuring an App:
- To create a new Django app within the project, use the following command:
  ```
  python manage.py startapp myapp
  ```
- Configure the app in the project's settings (`settings.py`):
  - Open the `settings.py` file located in your project's root directory.
  - Add the name of your app (`myapp`) to the `INSTALLED_APPS` list.
- Define models within your app:
  - Open the `models.py` file located in the app directory (`myapp/models.py`).
  - Define your app's models using Django's model syntax.
- Run database migrations:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- Create a `urls.py` file within your app:
  - Create a `urls.py` file in your app directory (`myapp/urls.py`).
  - Define the URL patterns specific to your app.
- Include your app's URLs in the project's main URL configuration (`urls.py`):
  - Open the `urls.py` file located in your project's root directory.
  - Import `include` from `django.urls` and add a new `path` or `include` statement to include your app's URLs.

5. Running Tests:
- To run the tests using Docker:
  ```
  docker-compose run web python manage.py test
  ```
- To run the tests locally (without Docker):
  ```
  python manage.py test
  ```

6. Logging:
- The Django project is preconfigured with a basic logging setup.
- Use the `logger` object to log messages in your views or other modules.

7. CI/CD Integration:
- The project includes a CI/CD pipeline configuration file (`.gitlab-ci.yml`) for GitLab CI.
- Modify the file according to your CI/CD platform requirements.

8. Deployment:
- Update the deployment section of the CI/CD pipeline configuration file to deploy the project to your desired environment.

## License
This project is licensed under the [MIT License](LICENSE).
