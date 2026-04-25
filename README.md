# Theatre API Service

API-сервіс для автоматизації роботи театру. Проєкт розроблений для управління розкладом вистав, бронюванням квитків та обліком залів.

## Функціонал
- Управління п'єсами, акторами та жанрами.
- Створення розкладу вистав у залах.
- Бронювання квитків на конкретні місця.
- Аутентифікація користувачів (JWT).

## Технології
- Python 3.12
- Django & Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions (CI/CD)

## Як запустити проєкт локально

1. Клонуйте репозиторій:
   ```bash
   git clone [https://github.com/Viktor395/theatre-api-service.git](https://github.com/Viktor395/theatre-api-service.git)
   cd theatre-api-service

2. Запустіть за допомогою Docker:
   docker-compose up --build

3. API буде доступне за адресою: http://localhost:8000/api/

## Основні endpoints

   /api/theatre/plays/ — перегляд та створення п'єс.

   /api/theatre/actors/ — управління акторами.

   /api/theatre/theatre-halls/ — перегляд залів.

   /api/theatre/performances/ — розклад вистав.

   /api/user/register/ — реєстрація користувача.

## Документація API

   Після запуску ви можете переглянути інтерактивну документацію Swagger за адресою:
   http://localhost:8000/api/doc/swagger/

   Автор: Viktor Velychko
   Python Developer