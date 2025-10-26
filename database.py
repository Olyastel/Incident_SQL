import sqlite3
from datetime import datetime

class IncidentDB:
    def __init__(self, db_name='incidents.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Создание всех таблиц базы данных"""
        try:
            self.cursor.executescript('''
                CREATE TABLE IF NOT EXISTS legal_regulations (
                    country_id INTEGER PRIMARY KEY,
                    country_name TEXT NOT NULL,
                    has_ai_regulation BOOLEAN,
                    regulation_laws TEXT
                );

                CREATE TABLE IF NOT EXISTS ai_system (
                    ai_system_id INTEGER PRIMARY KEY,
                    sae_level INTEGER,
                    system_name TEXT,
                    system_type TEXT
                );

                CREATE TABLE IF NOT EXISTS incident_conditions (
                    condition_id INTEGER PRIMARY KEY,
                    country_id INTEGER,
                    incident_date DATE,
                    weather_conditions TEXT,
                    illumination TEXT,
                    road_type TEXT,
                    severity TEXT,
                    FOREIGN KEY (country_id) REFERENCES legal_regulations(country_id)
                );

                CREATE TABLE IF NOT EXISTS transport (
                    vehicle_id INTEGER PRIMARY KEY,
                    ai_system_id INTEGER,
                    vehicle_type TEXT,
                    manufacturer TEXT,
                    FOREIGN KEY (ai_system_id) REFERENCES ai_system(ai_system_id)
                );

                CREATE TABLE IF NOT EXISTS incident (
                    incident_id INTEGER PRIMARY KEY,
                    condition_id INTEGER,
                    country_id INTEGER,
                    vehicle_id INTEGER,
                    description TEXT,
                    FOREIGN KEY (condition_id) REFERENCES incident_conditions(condition_id),
                    FOREIGN KEY (country_id) REFERENCES legal_regulations(country_id),
                    FOREIGN KEY (vehicle_id) REFERENCES transport(vehicle_id)
                );
            ''')
            self.conn.commit()
            print("Таблицы успешно созданы!")
        except Exception as e:
            print(f"Ошибка при создании таблиц: {e}")

    def add_country(self, country_id, country_name, has_regulation, laws):
        query = '''
            INSERT INTO legal_regulations (country_id, country_name, has_ai_regulation, regulation_laws)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(query, (country_id, country_name, has_regulation, laws))
        self.conn.commit()
        print(f"Страна {country_name} добавлена")

    def add_ai_system(self, ai_system_id, sae_level, system_name, system_type):
        query = '''
            INSERT INTO ai_system (ai_system_id, sae_level, system_name, system_type)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(query, (ai_system_id, sae_level, system_name, system_type))
        self.conn.commit()
        print(f"Система ИИ {system_name} добавлена")

    def add_vehicle(self, vehicle_id, ai_system_id, vehicle_type, manufacturer):
        query = '''
            INSERT INTO transport (vehicle_id, ai_system_id, vehicle_type, manufacturer)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(query, (vehicle_id, ai_system_id, vehicle_type, manufacturer))
        self.conn.commit()
        print(f"Транспорт {vehicle_type} добавлен")

    def add_incident_conditions(self, condition_id, country_id, date, weather, illumination, road_type, severity):
        query = '''
            INSERT INTO incident_conditions (condition_id, country_id, incident_date, weather_conditions, illumination, road_type, severity)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (condition_id, country_id, date, weather, illumination, road_type, severity))
        self.conn.commit()
        print("Условия инцидента добавлены")

    def add_incident(self, incident_id, condition_id, country_id, vehicle_id, description):
        query = '''
            INSERT INTO incident (incident_id, condition_id, country_id, vehicle_id, description)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (incident_id, condition_id, country_id, vehicle_id, description))
        self.conn.commit()
        print("Инцидент добавлен")

    def get_all_incidents(self):
        query = '''
            SELECT i.incident_id, i.description, l.country_name, c.incident_date, c.severity
            FROM incident i
            JOIN legal_regulations l ON i.country_id = l.country_id
            JOIN incident_conditions c ON i.condition_id = c.condition_id
        '''
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_incidents_by_country(self, country_name):
        query = '''
            SELECT i.incident_id, i.description, c.incident_date, c.severity
            FROM incident i
            JOIN legal_regulations l ON i.country_id = l.country_id
            JOIN incident_conditions c ON i.condition_id = c.condition_id
            WHERE l.country_name = ?
        '''
        self.cursor.execute(query, (country_name,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
        print("Соединение с БД закрыто")