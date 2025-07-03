Electronics Retail Chain

This project is a simple Django-based backend for managing an electronics retail chain. It supports operations on product catalogs, manufacturers, and stores, and allows managing their relationships via a RESTful API built on Django REST Framework.

Features
	•	Manage a list of products
	•	Manage manufacturers of products
	•	Manage store locations
	•	Link products to manufacturers
	•	Link products to stores
	•	REST API for CRUD operations
	•	JSON-based API responses

Technologies Used
	•	Python 3.x
	•	Django
	•	Django REST Framework
	•	SQLite (by default)

Project Structure

electronics_retail_chain/
├── manage.py
├── electronics/
│   ├── models.py      # database models
│   ├── serializers.py # DRF serializers
│   ├── views.py       # API views
│   ├── urls.py        # routing
│   └── ...
├── electronics_retail_chain/
│   ├── settings.py    # Django settings
│   └── ...
└── README.md

API Endpoints

Examples of available endpoints:
	•	/api/products/ — list and create products
	•	/api/manufacturers/ — list and create manufacturers
	•	/api/stores/ — list and create stores

All endpoints support standard GET, POST, PUT, PATCH, DELETE HTTP methods.

How to Contribute

Contributions are welcome! Feel free to open issues or submit pull requests. Please make sure to follow best practices and keep the code clean.

License

This project is licensed under the MIT License.

