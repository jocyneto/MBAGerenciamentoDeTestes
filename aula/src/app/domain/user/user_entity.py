from uuid import UUID

class User:
    id: UUID
    name: str

    def __init__(self, id: UUID, name:str):
        self.id = id
        self.name = name
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("ID DEVE SER UM UUID.")

        if not isinstance(self.name, str) or len(self.name.strip()) == 0:
            raise Exception("Eh necessario por um nome valido")
