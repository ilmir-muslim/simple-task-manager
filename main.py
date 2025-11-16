from tasks import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n=== Simple Task Manager ===")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Выполнить задачу")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            title = input("Введите задачу: ")
            manager.add_task(title)
        elif choice == "3":
            manager.show_tasks()
            try:
                task_id = int(input("Номер задачи для выполнения: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Ошибка: введите номер задачи")
        elif choice == "4":
            manager.show_tasks()
            try:
                task_id = int(input("Номер задачи для удаления: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Ошибка: введите номер задачи")
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
