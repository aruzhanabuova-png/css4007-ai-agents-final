import sqlite3
import src.database as database
import pytest

# Проверяем, что новая задача сохраняется в базе данных
def test_add_task(tmp_path, monkeypatch):

    # Используем временную базу для теста
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test.db")
    database.create_database()

    # Добавляем задачу
    task_id = database.add_task(
        "Math homework",
        "Study",
        "2026-11-25",
        "high",
        60
    )

    # Проверяем сохранённую задачу
    tasks = database.get_tasks()

    assert task_id == 1
    assert len(tasks) == 1
    assert tasks[0][1] == "Math homework"
    assert tasks[0][4] == "high"


# Проверяем, что нельзя добавить задачу без названия
def test_empty_title():

    # Пытаемся добавить задачу с пустым названием
    with pytest.raises(ValueError):
        database.add_task("", "Study", "2026-11-25", "high", 60)


# Проверяем, что неправильный приоритет вызывает ошибку
def test_invalid_priority():

    # Пытаемся добавить задачу с недопустимым приоритетом
    with pytest.raises(ValueError):
        database.add_task("Math homework", "Study", "2026-11-25", "urgent", 60)


# Проверяем, что время выполнения должно быть положительным
def test_invalid_duration():

    # Пытаемся добавить задачу с отрицательным временем
    with pytest.raises(ValueError):
        database.add_task("Math homework", "Study", "2026-11-25", "high", -30)


# Проверяем, что задача получает статус completed
def test_complete_task(tmp_path, monkeypatch):

    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test.db")
    database.create_database()

    task_id = database.add_task(
        "Math homework", "Study", "2026-11-25", "high", 60
    )

    # Отмечаем задачу как выполненную
    result = database.complete_task(task_id)

    # Проверяем результат и статус
    tasks = database.get_tasks()

    assert result is True
    assert tasks[0][6] == "completed"


# Проверяем изменение приоритета задачи
def test_update_priority(tmp_path, monkeypatch):

    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test.db")
    database.create_database()

    task_id = database.add_task(
        "Math homework", "Study", "2026-11-25", "high", 60
    )

    # Меняем приоритет на low
    result = database.update_priority(task_id, "low")

    # Проверяем новый приоритет
    tasks = database.get_tasks()

    assert result is True
    assert tasks[0][4] == "low"


# Проверяем удаление задачи из базы данных
def test_delete_task(tmp_path, monkeypatch):

    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test.db")
    database.create_database()

    task_id = database.add_task(
        "Math homework", "Study", "2026-11-25", "high", 60
    )

    # Удаляем задачу
    result = database.delete_task(task_id)

    # Проверяем, что задача удалена
    tasks = database.get_tasks()

    assert result is True
    assert len(tasks) == 0


# Проверяем, что неправильная дата вызывает ошибку
def test_invalid_deadline():

    # Пытаемся добавить задачу с неправильной датой
    with pytest.raises(ValueError):
        database.add_task(
            "Math homework", "Study", "wrong-date", "high", 60
        )