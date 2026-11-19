import sqlite3
from pathlib import Path
from datetime import datetime

# Путь к базе данных
DB_PATH = Path(__file__).resolve().parent.parent / ".private" / "planner.db"


def create_database():
    # Создаем папку для хранения данных
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Подключаемся к базе данных
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT,
                deadline TEXT,
                priority TEXT DEFAULT 'medium',
                duration_minutes INTEGER,
                status TEXT DEFAULT 'pending'
            )
        """)

    print("Database created successfully!")


# функция добавляет новую задачу в базу данных. Сохраняет название, категорию, дедлайн, приоритет и время выполнения.
# Перед сохранением она проверяет правильность введённых данных.
# Если всё правильно, сохраняет задачу и возвращает её номер.

def add_task(title, category, deadline, priority, duration_minutes):

    # Проверяем, что название задачи не пустое
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Task title cannot be empty.")

    # Проверяем формат дедлайна: YYYY-MM-DD
    if deadline:
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except (ValueError, TypeError):
            raise ValueError("Deadline must be in YYYY-MM-DD format.")

    # Проверяем приоритет задачи
    if priority not in ["low", "medium", "high"]:
        raise ValueError("Priority must be low, medium, or high.")

    # Проверяем продолжительность задачи
    if type(duration_minutes) is not int or duration_minutes <= 0:
        raise ValueError("Duration must be a positive integer.")

    # Подключаемся к базе данных
    with sqlite3.connect(DB_PATH) as connection:

        # Сохраняем новую задачу в таблице tasks
        cursor = connection.execute("""
            INSERT INTO tasks
            (title, category, deadline, priority, duration_minutes)
            VALUES (?, ?, ?, ?, ?)
        """, (title.strip(), category, deadline, priority, duration_minutes))

        # Получаем номер созданной задачи
        task_id = cursor.lastrowid

    return task_id


# Получаем все сохранённые задачи из базы данных
def get_tasks():

    with sqlite3.connect(DB_PATH) as connection:

        # Получаем все задачи
        cursor = connection.execute("SELECT * FROM tasks")

        # Сохраняем результат в список
        tasks = cursor.fetchall()

    # Возвращаем список задач
    return tasks


# Отмечаем задачу как выполненную по её номеру
def complete_task(task_id):

    with sqlite3.connect(DB_PATH) as connection:

        # Меняем статус задачи на completed
        cursor = connection.execute("""
            UPDATE tasks
            SET status = 'completed'
            WHERE id = ?
        """, (task_id,))

        # Проверяем, была ли найдена задача
        updated = cursor.rowcount

    return updated > 0


# Изменяем приоритет задачи по её номеру
def update_priority(task_id, new_priority):

    # Проверяем новый приоритет
    if new_priority not in ["low", "medium", "high"]:
        raise ValueError("Invalid priority.")

    with sqlite3.connect(DB_PATH) as connection:

        # Обновляем приоритет задачи
        cursor = connection.execute("""
            UPDATE tasks
            SET priority = ?
            WHERE id = ?
        """, (new_priority, task_id))

    # Проверяем, была ли задача обновлена
    return cursor.rowcount > 0


# Удаляем задачу из базы данных по её номеру
def delete_task(task_id):

    with sqlite3.connect(DB_PATH) as connection:

        # Удаляем выбранную задачу
        cursor = connection.execute("""
            DELETE FROM tasks
            WHERE id = ?
        """, (task_id,))

    # Проверяем, была ли задача удалена
    return cursor.rowcount > 0


# Проверяем удаление задачи из базы данных
if __name__ == "__main__":
    create_database()

    # Удаляем задачу №1
    result = delete_task(1)

    print("Task deleted:", result)

    # Показываем оставшиеся задачи
    tasks = get_tasks()

    for task in tasks:
        print(task)