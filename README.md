# 📅 Event Management API

A robust RESTful API built with Django and Django Rest Framework (DRF) for managing events. This API allows users to register, create events, and manage their own event listings securely. It features authentication, permission handling, and advanced filtering capabilities.

**[View Live Demo](https://darkpearlzz.pythonanywhere.com/api/events/)**

---

## 🚀 Features

* **User Authentication:** Secure registration and login system.
* **CRUD Operations:** Create, Read, Update, and Delete events.
* **Permissions:** * Public access to view events.
    * Authenticated access to create events.
    * **Owner-only** access to update or delete specific events.
* **Validation:** Prevents the creation of events with past dates.
* **Search & Filtering:** Filter events by upcoming dates, or search by title and location.
* **Pagination:** Handles large datasets efficiently.

---

## 🛠 Tech Stack

* **Backend:** Python, Django
* **API:** Django Rest Framework (DRF)
* **Database:** SQLite (Development) 
* **Deployment:** PythonAnywhere

---

## 💾 Database Schema (ERD)

The database consists of a `User` model (Organizer) and an `Event` model.
* **One** User can organize **Many** Events.
* **One** Event belongs to **One** Organizer.

---

## 🔌 API Endpoints

### Base URL: `/api/`

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **User Ops** | | | |
| `POST` | `/register/` | Register a new user | ❌ |
| **Event Ops** | | | |
| `GET` | `/events/` | List all events | ❌ |
| `POST` | `/events/` | Create a new event | ✅ |
| `GET` | `/events/<id>/` | Retrieve specific event details | ❌ |
| `PUT` | `/events/<id>/` | Update an event | ✅ (Owner Only) |
| `DELETE` | `/events/<id>/` | Delete an event | ✅ (Owner Only) |

### 🔍 Filtering & Search

You can filter results using query parameters:

* **View Upcoming Events:** `GET /events/?upcoming=true`
* **Search by Title/Location:** `GET /events/?search=concert`
* **Pagination:** `GET /events/?page=2`

---

## 💻 Installation & Local Setup

Follow these steps to run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/Darkpearlzz/Capstone-Project-BE.git
cd event_manager

2. Set up Virtual Environment
Windows (Git Bash):
Bash - 
python -m venv venv
source venv/Scripts/activate

Mac/Linux:
Bash - 
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Bash:
pip install -r requirements.txt

4. Run Migrations
Create the database tables.

Bash:
python manage.py migrate
5. Create Superuser (Optional)
To access the Django Admin panel.

Bash:
python manage.py createsuperuser

6. Run Server
Bash:
python manage.py runserver
Access the API at http://127.0.0.1:8000/api/events/

🧪 Testing
To test the API, you can use:

Browsable API: Simply navigate to the URLs in your browser (Django REST Framework provides a GUI).

Postman/Insomnia: Import the endpoints and test JSON payloads.

Sample JSON for Creating an Event (POST):

JSON

{
    "title": "Tech Conference 2024",
    "description": "A gathering of tech enthusiasts.",
    "date_and_time": "2024-12-25T14:00:00Z",
    "location": "Lagos, Nigeria",
    "capacity": 500
}
