# Cipher Backend

A small Django project used to learn the basics of backend development with
models, views, templates, forms, URL routing, migrations, and the Django admin
site.

## What we built

The project contains one Django app, `myapp`, with three user-facing pages:

- **Registration page (`/`)** - collects a username, email, password, and
  password confirmation.
- **Contact page (`/contact/`)** - stores messages submitted by visitors.
- **Employee page (`/employee/`)** - stores employee information.

The Django admin site is available at `/admin/` and includes both application
models.

## Backend concepts learned

### 1. Django project and app structure

- `cipherbackend/settings.py` contains project configuration such as installed
  apps, middleware, templates, database settings, and static files.
- `cipherbackend/urls.py` is the project-level URL configuration.
- `myapp/` contains the application logic.
- `manage.py` is used to run development and database commands.

Keeping project configuration separate from application code makes the code
easier to organize and extend.

### 2. Creating models

The application defines two database models in `myapp/models.py`.

#### Contact

The `Contact` model stores:

- Full name
- Email address
- Subject
- Message
- Automatically generated creation time

#### Employee

The `Employee` model stores:

- First and last names
- Email address
- Phone number
- Job position
- Department
- Hire date
- Salary

Each model field describes the expected data type and constraints. For example,
`EmailField` provides email-oriented validation, `DateField` stores dates, and
`DecimalField` is appropriate for monetary values.

The `__str__` methods make records easier to identify in the admin site.

### 3. Migrations and database changes

Migrations translate model changes into database changes:

1. The initial migration created the `Contact` model.
2. A later migration added `created_at` to `Contact`.
3. Another migration created the `Employee` model.
4. The final migration added the employee phone number and salary fields.

This demonstrates that models can evolve over time while Django tracks the
changes in a repeatable way.

### 4. Handling requests in views

The views use the request method to distinguish between displaying a page and
processing a submitted form:

- `GET` requests render the relevant template.
- `POST` requests read submitted values and save records.
- `redirect()` sends the user back to the appropriate page after a successful
  submission.
- Django messages provide success and error feedback.

The registration view also uses Django's built-in `User` model and
`create_user()` for account creation. The contact and employee views create
records using the application's custom models.

### 5. URL routing

The project-level URL file includes `myapp.urls`, while the app-level URL file
maps each path to a named view. Named URLs are used by templates with the
`{% url %}` tag, which avoids hard-coding links throughout the HTML.

### 6. Templates, CSRF, and static files

- Templates are stored under `myapp/templates/`.
- Forms use `{% csrf_token %}` to protect POST requests against cross-site
  request forgery.
- The contact page loads shared CSS from `myapp/static/css/style.css` using
  `{% load static %}`.
- Django messages are displayed in templates to communicate the result of an
  operation.

### 7. Admin integration

Registering `Contact` and `Employee` in `myapp/admin.py` makes them manageable
through Django's built-in admin interface. This is useful for inspecting and
maintaining stored data during development.

## Running the project

From the repository root:

```bash
cd cipherbackend
../bin/python manage.py migrate
../bin/python manage.py runserver
```

Then open <http://127.0.0.1:8000/>.

To create an admin user:

```bash
../bin/python manage.py createsuperuser
```

## Database

The project currently uses SQLite, stored in `cipherbackend/db.sqlite3`. This
is convenient for learning and local development. A production deployment
would normally use a dedicated database server and environment-specific
configuration.

## Current development notes

- `myapp/tests.py` currently contains the default empty test class, so automated
  coverage for registration, contact submissions, and employee submissions
  still needs to be added.
- The default settings have development values such as `DEBUG = True` and an
  insecure development secret key. These must be replaced with environment
  variables and production-safe settings before deployment.
- Django forms or custom validation could be introduced to centralize input
  validation instead of reading all values directly from `request.POST`.

## Main lessons

This project shows the complete basic Django flow:

**URL -> view -> template/form -> model -> migration -> database**

The most important lesson is that Django provides a consistent structure for
turning browser requests into validated database records, while migrations,
templates, messages, and the admin site support the rest of the development
workflow.
