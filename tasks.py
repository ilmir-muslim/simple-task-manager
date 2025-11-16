class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.id}. [{status}] {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if title.strip():
            task = Task(self.next_id, title.strip())
            self.tasks.append(task)
            self.next_id += 1
            print("Задача добавлена!")
        else:
            print("Ошибка: задача не может быть пустой")

    def show_tasks(self):
        if not self.tasks:
            print("Задач нет")
            return

        print("\nСписок задач:")
        for task in self.tasks:
            print(task)

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task:
            task.completed = True
            print("Задача выполнена!")
        else:
            print("Ошибка: задача не найдена")

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            print("Задача удалена!")
        else:
            print("Ошибка: задача не найдена")

    def _find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
