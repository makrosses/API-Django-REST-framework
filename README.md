# Factory API

REST API для управления производственной базой данных завода. Реализовано на Django REST Framework с подключением к Microsoft SQL Server.

---

## Используемые технологии

- **Python** 3.12
- **Django** 6.0.5
- **Django REST Framework** 3.17.1
- **mssql-django** — подключение к Microsoft SQL Server
- **drf-spectacular** — автоматическая Swagger документация
- **pyodbc** — ODBC драйвер для SQL Server

---

## Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone <ссылка на репозиторий>
cd <папка проекта>
```

### 2. Создать виртуальное окружение
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Настроить подключение к БД

В файле `library_api/settings.py` указать параметры подключения к SQL Server:
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'factorydb',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
```

### 5. Запустить сервер
```bash
python manage.py runserver
```

---

## Документация API

После запуска сервера документация доступна по адресу:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

---

## Эндпоинты

Все эндпоинты доступны по базовому пути `/api/v1/`.

### Clients — Клиенты
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/clients/` | Список всех клиентов |
| GET | `/api/v1/clients/?name=<имя>` | Поиск клиента по имени |
| GET | `/api/v1/clients/{id}/` | Получить клиента по ID |
| POST | `/api/v1/clients/` | Создать клиента |
| PATCH | `/api/v1/clients/{id}/` | Обновить клиента |
| DELETE | `/api/v1/clients/{id}/` | Удалить клиента |

### Employees — Сотрудники
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/employees/` | Список всех сотрудников |
| GET | `/api/v1/employees/?lastname=<фамилия>` | Поиск по фамилии |
| GET | `/api/v1/employees/?role=<id>` | Фильтр по роли |
| GET | `/api/v1/employees/{id}/` | Получить сотрудника по ID |
| POST | `/api/v1/employees/` | Создать сотрудника |
| PATCH | `/api/v1/employees/{id}/` | Обновить сотрудника |
| DELETE | `/api/v1/employees/{id}/` | Удалить сотрудника |

### Materials — Материалы
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/materials/` | Список всех материалов |
| GET | `/api/v1/materials/?name=<название>` | Поиск по названию |
| GET | `/api/v1/materials/?producer=<id>` | Фильтр по производителю |
| GET | `/api/v1/materials/{id}/` | Получить материал по ID |
| POST | `/api/v1/materials/` | Создать материал |
| PATCH | `/api/v1/materials/{id}/` | Обновить материал |
| DELETE | `/api/v1/materials/{id}/` | Удалить материал |

### Orders — Заказы
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/orders/` | Список всех заказов |
| GET | `/api/v1/orders/?client=<id>` | Фильтр по клиенту |
| GET | `/api/v1/orders/?status=<id>` | Фильтр по статусу |
| GET | `/api/v1/orders/{id}/` | Получить заказ по ID |
| POST | `/api/v1/orders/` | Создать заказ |
| PATCH | `/api/v1/orders/{id}/` | Обновить заказ |
| DELETE | `/api/v1/orders/{id}/` | Удалить заказ |

### Order Items — Позиции заказа
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/order-items/` | Список всех позиций |
| GET | `/api/v1/order-items/?order=<id>` | Фильтр по заказу |
| POST | `/api/v1/order-items/` | Создать позицию |
| PATCH | `/api/v1/order-items/{id}/` | Обновить позицию |
| DELETE | `/api/v1/order-items/{id}/` | Удалить позицию |

### Order Statuses — Статусы заказов
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/order-statuses/` | Список статусов |
| POST | `/api/v1/order-statuses/` | Создать статус |
| PATCH | `/api/v1/order-statuses/{id}/` | Обновить статус |
| DELETE | `/api/v1/order-statuses/{id}/` | Удалить статус |

### Producers — Производители
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/producers/` | Список производителей |
| GET | `/api/v1/producers/?name=<название>` | Поиск по названию |
| POST | `/api/v1/producers/` | Создать производителя |
| PATCH | `/api/v1/producers/{id}/` | Обновить производителя |
| DELETE | `/api/v1/producers/{id}/` | Удалить производителя |

### Products — Продукты
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/products/` | Список продуктов |
| GET | `/api/v1/products/?name=<название>` | Поиск по названию |
| POST | `/api/v1/products/` | Создать продукт |
| PATCH | `/api/v1/products/{id}/` | Обновить продукт |
| DELETE | `/api/v1/products/{id}/` | Удалить продукт |

### Recipes — Рецепты
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/recipes/` | Список рецептов |
| GET | `/api/v1/recipes/?product=<id>` | Фильтр по продукту |
| POST | `/api/v1/recipes/` | Создать рецепт |
| PATCH | `/api/v1/recipes/{id}/` | Обновить рецепт |
| DELETE | `/api/v1/recipes/{id}/` | Удалить рецепт |

### Roles — Роли сотрудников
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/roles/` | Список ролей |
| POST | `/api/v1/roles/` | Создать роль |
| PATCH | `/api/v1/roles/{id}/` | Обновить роль |
| DELETE | `/api/v1/roles/{id}/` | Удалить роль |

### Shifts — Смены
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/shifts/` | Список смен |
| GET | `/api/v1/shifts/?worker=<id>` | Фильтр по сотруднику |
| POST | `/api/v1/shifts/` | Создать смену |
| PATCH | `/api/v1/shifts/{id}/` | Обновить смену |
| DELETE | `/api/v1/shifts/{id}/` | Удалить смену |

### Statuses — Статусы сотрудников
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/statuses/` | Список статусов |
| POST | `/api/v1/statuses/` | Создать статус |
| PATCH | `/api/v1/statuses/{id}/` | Обновить статус |
| DELETE | `/api/v1/statuses/{id}/` | Удалить статус |

### Supplies — Поставки
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/supplies/` | Список поставок |
| GET | `/api/v1/supplies/?supplier=<id>` | Фильтр по поставщику |
| POST | `/api/v1/supplies/` | Создать поставку |
| PATCH | `/api/v1/supplies/{id}/` | Обновить поставку |
| DELETE | `/api/v1/supplies/{id}/` | Удалить поставку |

### Supply Items — Позиции поставки
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/supply-items/` | Список позиций поставки |
| GET | `/api/v1/supply-items/?supply=<id>` | Фильтр по поставке |
| POST | `/api/v1/supply-items/` | Создать позицию |
| PATCH | `/api/v1/supply-items/{id}/` | Обновить позицию |
| DELETE | `/api/v1/supply-items/{id}/` | Удалить позицию |

### Supply Statuses — Статусы поставок
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/v1/supply-statuses/` | Список статусов поставок |
| POST | `/api/v1/supply-statuses/` | Создать статус |
| PATCH | `/api/v1/supply-statuses/{id}/` | Обновить статус |
| DELETE | `/api/v1/supply-statuses/{id}/` | Удалить статус |

---

## Используемые библиотеки

Полный список в файле `requirements.txt`. Основные:

| Библиотека | Версия | Назначение |
|------------|--------|------------|
| Django | 6.0.5 | Веб-фреймворк |
| djangorestframework | 3.17.1 | REST API |
| mssql-django | 1.7.2 | Поддержка MS SQL Server |
| drf-spectacular | latest | Swagger документация |
| pyodbc | latest | ODBC подключение |
| pytz | latest | Работа с временными зонами |
