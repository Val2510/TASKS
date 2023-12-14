import json
from datetime import datetime
import os

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)

def input_string(prompt):
    return input(prompt)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")

def generate_unique_id(existing_ids):
    new_id = 1
    while new_id in existing_ids:
        new_id += 1
    return new_id

def add_note():
    title = input_string("Введите заголовок заметки: ")
    body = input_string("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note_ids = [note["id"] for note in notes]
    note_id = generate_unique_id(note_ids)
    
    note = {"id": note_id, "title": title, "body": body, "timestamp": timestamp}
    
    if note_id in note_ids:
        note_id = generate_unique_id(note_ids)
        note["id"] = note_id

    notes.append(note)
    save_notes(notes)
    print(f"Заметка добавлена. ID заметки: {note_id}")

def view_notes():
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")
        print(f"Текст: {note['body']}\n")

def find_note_by_id(note_id):
    return next((note for note in notes if note["id"] == note_id), None)

def edit_note():
    note_id = input_int("Введите ID заметки для редактирования: ")
    note = find_note_by_id(note_id)
    if note:
        title = input_string("Введите новый заголовок заметки: ")
        body = input_string("Введите новый текст заметки: ")
        note["title"] = title
        note["body"] = body
        note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)
        print("Заметка отредактирована")
    else:
        print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = input_int("Введите ID заметки для удаления: ")
    note = find_note_by_id(note_id)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("Заметка удалена")
    else:
        print("Заметка с указанным ID не найдена.")

def main():
    global notes
    notes = load_notes()

    while True:
        print("\n1. Просмотреть заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        
        choice = input_int("Выберите действие (1-5): ")

        if choice == 1:
            view_notes()
        elif choice == 2:
            add_note()
        elif choice == 3:
            edit_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            print("Выход из приложения.")
            break
        else:
            print("Некорректный ввод. Выберите пункт от 1 до 5.")

if __name__ == "__main__":
    main()