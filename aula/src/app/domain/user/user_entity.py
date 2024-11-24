from typing import List
from uuid import UUID
from domain.task.task_entity import Task


class User:
    id: UUID
    name: str
    tasks: List[Task]

    def __init__(self, id: UUID, name:str):
        self.id = id
        self.name = name
        self.tasks = []
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("ID DEVE SER UM UUID.")

        if not isinstance(self.name, str) or len(self.name.strip()) == 0:
            raise Exception("Eh necessario por um nome valido")

    def collect_tasks(self, tasks_list: List[Task]) -> None:
        self.tasks.extend(tasks_list)
