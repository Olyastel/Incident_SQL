# Система учета инцидентов с ИИ в транспорте

## О проекте

Система для сбора и анализа данных об инцидентах, связанных с системами искусственного интеллекта в транспортных средствах.
База данных предназначена для учета и анализа инцидентов с автономными транспортными средствами, включая:
- Учет условий происшествий
- Отслеживание используемых систем ИИ
- Анализ правового регулирования по странам
- Классификацию типов транспорта и производителей

## Структура базы данных

### Основные таблицы:

1. **`incident`** - Основная таблица инцидентов
2. **`incident_conditions`** - Условия происшествий (погода, освещение, тип дороги)
3. **`legal_regulations`** - Правовое регулирование по странам
4. **`transport`** - Информация о транспортных средствах
5. **`ai_system`** - Данные о системах искусственного интеллекта

### Установка на Arch Linux

```bash
# Обновление системы и установка зависимостей
sudo pacman -Syu python python-pip sqlite sqlitebrowser

# Клонирование или создание проекта
mkdir incident_db
cd incident_db
```

### Настройка проекта

1. **Создайте файлы проекта**:
   - `database.py` - основной класс для работы с БД
   - `main.py` - пример использования

2. **Установите права доступа:**
```bash
chmod +x database.py main.py
```

3. **Запустите инициализацию базы данных:**
```bash
python main.py
```

## Использование

### Основные функции

```python
from database import IncidentDB

# Инициализация базы данных
db = IncidentDB()

# Добавление страны
db.add_country(1, "Россия", True, "ФЗ-123, ФЗ-456")

# Добавление системы ИИ
db.add_ai_system(1, 4, "Autopilot", "компьютерное зрение")

# Добавление транспортного средства
db.add_vehicle(1, 1, "легковой автомобиль", "Tesla")

# Добавление инцидента
db.add_incident(
    incident_id=1,
    condition_id=1,
    country_id=1,
    vehicle_id=1,
    description="Столкновение с ограждением"
)

# Получение всех инцидентов
incidents = db.get_all_incidents()

# Получение инцидентов по стране
russia_incidents = db.get_incidents_by_country("Россия")
```

### Просмотр данных

**Через терминал:**
```bash
sqlite3 incidents.db

# Полезные команды:
.tables                    # Показать таблицы
.schema incident           # Структура таблицы инцидентов
SELECT * FROM incident;    # Все инциденты
.quit                      # Выход
```

**Через графический интерфейс:**
```bash
sqlitebrowser incidents.db
```

## API методы

### Методы добавления данных:
- `add_country(country_id, name, has_regulation, laws)`
- `add_ai_system(ai_system_id, sae_level, name, type)`
- `add_vehicle(vehicle_id, ai_system_id, type, manufacturer)`
- `add_incident_conditions(condition_id, country_id, date, weather, illumination, road_type, severity)`
- `add_incident(incident_id, condition_id, country_id, vehicle_id, description)`

### Методы получения данных:
- `get_all_incidents()`
- `get_incidents_by_country(country_name)`

## Пример данных

### Поддерживаемые значения:

**Погодные условия:** `ясно`, `дождь`, `снег`, `туман`  
**Освещенность:** `день`, `ночь`, `сумерки`  
**Тип дороги:** `автострада`, `городская дорога`  
**Тяжесть инцидента:** `столкновение`, `травма`, `смерть`, `материальный ущерб`  
**Тип транспорта:** `легковой автомобиль`, `грузовик`, `беспилотное такси`, `поезд`, `дрон`  
**Тип системы ИИ:** `компьютерное зрение`, `планирование пути`, `контроль`

## Структура проекта

```
incident_db/
├── database.py          # Основной класс работы с БД
├── main.py              # Пример использования и тестовые данные
├── incidents.db         # Файл базы данных (автосоздание)
└── README.md           # Документация
```

## Примеры запросов

### Получение статистики по странам:
```sql
SELECT l.country_name, COUNT(i.incident_id) as incident_count
FROM incident i
JOIN legal_regulations l ON i.country_id = l.country_id
GROUP BY l.country_name;
```

### Инциденты по уровню автономности:
```sql
SELECT a.sae_level, COUNT(i.incident_id) 
FROM incident i
JOIN transport t ON i.vehicle_id = t.vehicle_id
JOIN ai_system a ON t.ai_system_id = a.ai_system_id
GROUP BY a.sae_level;
```

## Устранение неполадок

**Проблема:** Ошибка при создании таблиц  
**Решение:** Убедитесь, что файл базы данных не открыт в других программах

**Проблема:** Нет доступа к SQLite  
**Решение:** Установите пакет: `sudo pacman -S sqlite`

**Проблема:** Ошибки кодировки  
**Решение:** Убедитесь, что файлы сохранены в UTF-8

## Лицензия

Проект распространяется под MIT License.

---

**Примечание:** Эта система предназначена для исследовательских целей и сбора статистических данных об инцидентах с системами ИИ в транспорте.
