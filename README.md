# Theatre API Service

API-сервіс для автоматизації роботи театру. Проєкт розроблений для управління розкладом вистав, бронюванням квитків та обліком залів.

## Функціонал

Проєкт є сервісом для керування театральною діяльністю та бронюванням квитків.

### Основні можливості:

- **Управління репертуаром:** Додавання та перегляд п'єс (`Play`), жанрів (`Genre`) та акторів (`Actor`).
- **Система бронювання:**
  - Налаштування театральних залів (`TheatreHall`) з урахуванням кількості рядів та місць.
  - Планування вистав (`Performance`) на конкретні дати та час.
  - Можливість бронювання квитків (`Reservation`) на конкретні місця (`Ticket`).
- **Валідація даних:** Захист від бронювання вже зайнятих місць.
- **Адміністрування:** Повноцінна панель адміністратора для керування всіма даними проєкту.

## Технології
- Python 3.12
- Django & Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions (CI/CD)

## Як запустити проєкт локально

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/Viktor395/theatre-api-service.git

   cd theatre-api-service

2. Запустіть за допомогою Docker:
   docker-compose up --build

3. API буде доступне за адресою: http://localhost:8000/api/theatre/

## Основні endpoints

   /api/theatre/plays/ — перегляд та створення п'єс.

   /api/theatre/actors/ — управління акторами.

   /api/theatre/genres/ — управління жанрами.

   /api/theatre/theatre-halls/ — перегляд залів.

   /api/theatre/performances/ — розклад вистав.

   /api/theatre/reservations/ — створення та перегляд бронювань (вимагає авторизації).

   /api/user/register/ — реєстрація користувача.

   /api/token/ — отримання JWT-токена для входу.

## Документація API

   Після запуску ви можете переглянути інтерактивну документацію Swagger за адресою:
   http://localhost:8000/api/doc/swagger/

   Автор: Viktor Velychko
   Python Developer