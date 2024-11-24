from uuid import uuid4
from domain.task.task_entity import Task
import pytest


class TestTask:

    #TESTE PARA VERIFICAR O CONSTRUTOR DA CLASSE TAREFA
    def test_task_inicialization(self):
        task_id = uuid4()
        user_id = uuid4()
        title = "Estudo de Teste Unitários"
        description = "Os teste unitários são os mais baratos e rápidos de implemenção"
        completed = False

        task = Task(id= task_id
                    , user_id=user_id
                    , title=title
                    , description=description
                    , completed=completed)
        
        assert task.id == task_id
        assert task.user_id == user_id
        assert task.title == title
        assert task.description == description
        assert task.completed == completed

    # TESTE PARA VERIFICAR O ID DA TASK
    def test_task_id_validate(self):
        with pytest.raises(Exception, match="id must be an UUID"):
            Task(
                id="INVALID ID"
                ,user_id=uuid4()
                ,title="Titulo da task"
                ,description="Descricao da task"
                ,completed=False
            )


    # TESTE PARA VERIFICAR O USER ID
    def test_task_user_id_validate(self):
        with pytest.raises(Exception, match="user_id must be an UUID"):
            Task(
                id=uuid4()
                ,user_id="INVALID ID"
                ,title="Titulo da task"
                ,description="Descricao da task"
                ,completed=False
            )

    # TESTE PARA VERIFICAR O TITULO
    def test_task_title_validate(self):
        with pytest.raises(Exception, match="title is required"):
            Task(
                id=uuid4()
                ,user_id=uuid4()
                ,title=""
                ,description="Descricao da task"
                ,completed=False
            )

    # TESTE PARA VERIFICAR A DESCRIÇÃO
    def test_task_description_validate(self):
        with pytest.raises(Exception, match="description is required"):
            Task(
                id=uuid4()
                ,user_id=uuid4()
                ,title="Titulo da task"
                ,description=""
                ,completed=False
            )

    # TESTE PARA VERIFICAR O COMPLETED
    def test_task_completed_validate(self):
        with pytest.raises(Exception, match="invalid completed status: must be a boolean"):
            Task(
                id=uuid4()
                ,user_id=uuid4()
                ,title="Titulo da task"
                ,description="Descricao da task"
                ,completed="False"
            )

    # TESTE PARA VERIFICAR SE UMA TAREFA FOI COMPLETADA COM UMA FUNÇÃO `MASK_AS_COMPLETED`
    def test_task_mark_as_completed(self):
        # Instaciar a tarefa
        task =  Task(
                id=uuid4()
                ,user_id=uuid4()
                ,title="Titulo da task"
                ,description="Descricao da task"
                ,completed=False
            )
        
        # Marcar como concluido
        task.mark_as_completed()

        # Verificar se o atributo foi para completed
        assert task.completed == True
