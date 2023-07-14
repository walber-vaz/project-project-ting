import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    task_one = {
        "nome_do_arquivo": "",
        "qtd_linhas": 9,
        "linhas_do_arquivo": [],
    }

    high_task_one = {
        "nome_do_arquivo": "",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }

    task_two = {
        "nome_do_arquivo": "",
        "qtd_linhas": 11,
        "linhas_do_arquivo": [],
    }

    high_task_two = {
        "nome_do_arquivo": "",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    priority_queue = PriorityQueue()

    priority_queue.enqueue(task_one)
    priority_queue.enqueue(high_task_one)
    priority_queue.enqueue(task_two)
    priority_queue.enqueue(high_task_two)

    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue) == 4
    assert priority_queue.high_priority.search(0) == high_task_one
    assert priority_queue.high_priority.search(1) == high_task_two
    assert priority_queue.regular_priority.search(0) == task_one
    assert priority_queue.regular_priority.search(1) == task_two

    assert priority_queue.search(1) == high_task_two
    assert priority_queue.search(2) == task_one
    assert priority_queue.search(3) == task_two

    assert priority_queue.dequeue() == high_task_one
    assert priority_queue.dequeue() == high_task_two
    assert priority_queue.dequeue() == task_one
    assert priority_queue.dequeue() == task_two
    assert len(priority_queue) == 0
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(1)
