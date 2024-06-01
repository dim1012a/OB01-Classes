class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Выполнено' if self.completed else 'Не выполнено'
        return f'{self.description} (Срок: {self.deadline}) - {status}'

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print(f'Задача с индексом {task_index} не найдена.')

    def get_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        return pending_tasks

    def show_tasks(self):
        if not self.tasks:
            print('Нет задач.')
        for index, task in enumerate(self.tasks):
            print(f'{index + 1}. {task}')

# Пример использования
if __name__ == '__main__':
    manager = TaskManager()

    # Добавление задач
    manager.add_task('Купить продукты', '2024-10-15')
    manager.add_task('Сделать домашнее задание', '2024-10-16')
    manager.add_task('Позвонить другу', '2024-10-17')

    # Показ всех задач
    print('Все задачи:')
    manager.show_tasks()

    # Отметка задачи как выполненной
    manager.mark_task_completed(1)

    # Показ текущих (не выполненных) задач
    print('\nТекущие задачи:')
    pending_tasks = manager.get_pending_tasks()
    for task in pending_tasks:
        print(task)