# Theatre API Service

An API service designed to automate theatre operations. This project provides a robust system for managing performance schedules, ticket bookings, and theatre hall configurations.

## Features

- **Repertoire Management:** Add and manage plays, genres, and actors.
- **Booking System:**
  - Configuration of theatre halls with specific row and seat counts.
  - Performance scheduling for specific dates and times.
  - Ticket reservation system with seat availability validation.
- **Data Validation:** Ensures seats cannot be double-booked.
- **Administration:** Built-in admin panel for comprehensive data management.

## Technologies

- Python 3.12
- Django & Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions (CI/CD)

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Viktor395/theatre-api-service.git
   cd theatre-api-service

2. Create a .env file in the root directory and add your SECRET_KEY and database credentials:

   SECRET_KEY=your_secret_key_here
   DATABASE_URL=postgres://user:password@db:5432/dbname

3. Run the project using Docker:

   docker-compose up --build

4. The API will be available at: http://localhost:8000/api/theatre/

## API Endpoints

/api/theatre/plays/ — List and create plays.

/api/theatre/actors/ — Manage actors.

/api/theatre/genres/ — Manage genres.

/api/theatre/theatre-halls/ — View theatre halls.

/api/theatre/performances/ — View performance schedule.

/api/theatre/reservations/ — Create and view reservations (requires authentication).

/api/user/register/ — User registration.

/api/token/ — Obtain JWT token for login.

## API Documentation
Once the service is running, you can access the interactive Swagger documentation here:
http://localhost:8000/api/doc/swagger/

Author: Viktor Velychko
Python Developer