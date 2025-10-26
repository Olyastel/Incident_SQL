from database import IncidentDB

def main():
    db = IncidentDB()
    
    try:
        # Добавление тестовых данных
        # Страны
        db.add_country(1, "Россия", True, "ФЗ-123, ФЗ-456")
        db.add_country(2, "США", True, "AV-1, AV-2")
        db.add_country(3, "Германия", True, "StVZO §1a")
        
        # Системы ИИ
        db.add_ai_system(1, 4, "Autopilot", "компьютерное зрение")
        db.add_ai_system(2, 3, "ProPILOT", "планирование пути")
        db.add_ai_system(3, 5, "Drive Pilot", "контроль")
        
        # Транспорт
        db.add_vehicle(1, 1, "легковой автомобиль", "Tesla")
        db.add_vehicle(2, 2, "грузовик", "Nissan")
        db.add_vehicle(3, 3, "беспилотное такси", "Mercedes")
        
        # Условия инцидентов
        db.add_incident_conditions(1, 1, "2024-01-15", "дождь", "ночь", "автострада", "столкновение")
        db.add_incident_conditions(2, 2, "2024-01-20", "ясно", "день", "городская дорога", "травма")
        db.add_incident_conditions(3, 3, "2024-01-25", "туман", "сумерки", "автострада", "материальный ущерб")
        
        # 5. Сами инциденты
        db.add_incident(1, 1, 1, 1, "Столкновение с ограждением на мокрой дороге")
        db.add_incident(2, 2, 2, 2, "Наезд на пешехода на пешеходном переходе")
        db.add_incident(3, 3, 3, 3, "Столкновение с другим транспортным средством в условиях тумана")
        
        print("\n=== Все инциденты ===")
        incidents = db.get_all_incidents()
        for incident in incidents:
            print(f"ID: {incident[0]}, Описание: {incident[1]}, Страна: {incident[2]}, Дата: {incident[3]}, Тяжесть: {incident[4]}")
        
        print("\n=== Инциденты в России ===")
        russia_incidents = db.get_incidents_by_country("Россия")
        for incident in russia_incidents:
            print(f"ID: {incident[0]}, Описание: {incident[1]}, Дата: {incident[2]}, Тяжесть: {incident[3]}")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()