# Shop Finder

Shop Finder is a Django-based web application that allows users to find nearby shops based on their current location. It provides a RESTful API for managing shop information and searching for shops.

## Features

- CRUD operations for shops (Create, Read, Update, Delete)
- Search functionality to find nearby shops based on latitude and longitude
- RESTful API with Django Rest Framework
- Automatic API documentation with Swagger and ReDoc

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/shop-finder.git
   cd shop-finder
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Access the API at `http://localhost:8000/api/`

3. View API documentation:
   - Swagger UI: `http://localhost:8000/swagger/`
   - ReDoc: `http://localhost:8000/redoc/`

## API Endpoints

- `GET /api/shops/`: List all shops
- `POST /api/shops/`: Create a new shop
- `GET /api/shops/{id}/`: Retrieve a specific shop
- `PUT /api/shops/{id}/`: Update a specific shop
- `PATCH /api/shops/{id}/`: Partially update a specific shop
- `DELETE /api/shops/{id}/`: Delete a specific shop
- `GET /api/shops/search/?latitude=<lat>&longitude=<lon>`: Search for nearby shops

## Example API Usage

### Creating a new shop

```bash
curl -X POST http://localhost:8000/api/shops/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Coffee Haven", "latitude": 40.7128, "longitude": -74.0060}'
```

### Searching for nearby shops

```bash
curl "http://localhost:8000/api/shops/search/?latitude=40.7128&longitude=-74.0060"
```

## Contributing

Contributions to Shop Finder are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Sameer Parmar - sameerparmar.sp@gmail.com

Project Link: [https://github.com/sameer-parmar/shop-finder](https://github.com/yourusername/shop-finder)
