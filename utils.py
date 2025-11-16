import json
from datetime import datetime


def save_tasks_to_file(tasks, filename="tasks.json"):
    """Сохраняет задачи в JSON файл"""
    try:
        data = []
        for task in tasks:
            data.append(
                {
                    "id": task.id,
                    "title": task.title,
                    "completed": task.completed,
                    "created_at": datetime.now().isoformat(),
                }
            )

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Задачи сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")


def load_tasks_from_file(filename="tasks.json"):
    """Загружает задачи из JSON файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Файл с задачами не найден")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        return []


def format_date(date_string):
    """Форматирует дату для красивого отображения"""
    try:
        date = datetime.fromisoformat(date_string)
        return date.strftime("%d.%m.%Y %H:%M")
    except:
        return date_string
