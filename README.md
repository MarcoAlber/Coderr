<h1 align="center">Coderr</h1>

<p align="center">
  <em>Coderr is the backend for a freelance platform, built with **Django** and **Django REST Framework (DRF)**. 
  It provides a fully functional RESTful API that allows user registration, authentication, profile management (business and customer), 
  offer and order handling, and a review system – all with strict role-based access control.</em>
  <br>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.13.2-blue?logo=python&logoColor=white" alt="Python version"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-5.2.7-success?logo=django&logoColor=white" alt="Django version"></a>
  <a href="https://www.django-rest-framework.org/"><img src="https://img.shields.io/badge/DRF-3.16.1-red?logo=django&logoColor=white" alt="DRF version"></a>
</p>

<hr>

## 🔧 Features

- User registration and JWT authentication
- Business and customer profile types
- Create, manage, and delete offers
- Place and manage freelance orders
- Leave and manage reviews
- Clean and RESTful API structure
- Role-based access control

---

## 🚀 Tech Stack

- **Python** 3.13.2
- **Django** 5.2.7
- **Django REST Framework (DRF)**
- **SQLite** (for development)
- **CORS support** via `django-cors-headers`
- **Nested routing** with `drf-nested-routers`

---

## 📁 Project Structure

```text
coderr/
├── user_auth_app/
├── profile_app/
├── offer_app/
├── order_app/
├── review_app/
├── core/               # API routing and settings
├── manage.py
└── db.sqlite3
```

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/MarcoAlber/Coderr.git .
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Run the development server**
```bash
python manage.py runserver
```

---

## 🔑 API Endpoints

Authentication
| Method | Endpoint             | Description                  |
| ------ | -------------------- | ---------------------------- |
| POST   | `/api/registration/` | Register a new user          |
| POST   | `/api/login/`        | Log in and receive JWT token |


Profile
| Method | Endpoint                  | Description                |
| ------ | ------------------------- | -------------------------- |
| GET    | `/api/profile/{pk}/`      | Retrieve a user profile    |
| PATCH  | `/api/profile/{pk}/`      | Update a profile           |
| GET    | `/api/profiles/business/` | List all business profiles |
| GET    | `/api/profiles/customer/` | List all customer profiles |


Offers
| Method | Endpoint                  | Description                    |
| ------ | ------------------------- | ------------------------------ |
| GET    | `/api/offers/`            | List all offers                |
| POST   | `/api/offers/`            | Create a new offer             |
| GET    | `/api/offers/{id}/`       | Retrieve offer details         |
| PATCH  | `/api/offers/{id}/`       | Update an offer                |
| DELETE | `/api/offers/{id}/`       | Delete an offer                |
| GET    | `/api/offerdetails/{id}/` | Get extended offer information |


Orders
| Method| Endpoint                                        | Description                                  |
| ----- | ----------------------------------------------- | -------------------------------------------- |
| GET   | `/api/orders/`                                  | List all orders                              |
| POST  | `/api/orders/`                                  | Create a new order                           |
| PATCH | `/api/orders/{id}/`                             | Update an order                              |
| DELETE| `/api/orders/{id}/`                             | Delete an order                              |
| GET   | `/api/order-count/{business_user_id}/`          | Get total order count for a business user    |
| GET   | `/api/completed-order-count/{business_user_id}/`| Get completed order count for a business user|


Reviews
| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| GET    | `/api/reviews/`      | List all reviews |
| POST   | `/api/reviews/`      | Create a review  |
| PATCH  | `/api/reviews/{id}/` | Update a review  |
| DELETE | `/api/reviews/{id}/` | Delete a review  |


General Information
| Method | Endpoint          | Description                        |
| ------ | ----------------- | ---------------------------------- |
| GET    | `/api/base-info/` | Fetch general platform information |

---

## 🥪 Testing (optional)

If you have tests in place, run:
```bash
python manage.py test
```

---

## ⚙️ Requirements

    asgiref==3.10.0
    Django==5.2.7
    django-cors-headers==4.9.0
    django-filter==25.2
    djangorestframework==3.16.1
    sqlparse==0.5.3
    tzdata==2025.2

---

## 📌 Notes

- SQLite is used for development; for production, consider switching to PostgreSQL or another robust database system.
- JWT authentication is implemented for secure login sessions.
- CORS is enabled, allowing communication with external frontend applications (e.g., React).
- Users can only access and manage their own data, based on their authenticated role (business or customer).

---

## 📨 Contact

For questions or contributions, feel free to reach out or open an issue:

Marco Alber 

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

Let me know if you'd like:
- Swagger or ReDoc API documentation setup
- Docker support for easy deployment
- A matching frontend `README.md` file

I'm happy to help!