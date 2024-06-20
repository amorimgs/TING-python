from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue({"qtd_linhas": 2})
    pq.enqueue({"qtd_linhas": 10})
    pq.enqueue({"qtd_linhas": 5})
    pq.enqueue({"qtd_linhas": 4})

    assert len(pq) == 4

    assert pq.search(0) == {"qtd_linhas": 2}
    assert pq.search(1) == {"qtd_linhas": 4}
    assert pq.search(2) == {"qtd_linhas": 10}
    assert pq.search(3) == {"qtd_linhas": 5}

    with pytest.raises(IndexError):
        pq.search(4)

    assert pq.dequeue() == {"qtd_linhas": 2}
    assert pq.dequeue() == {"qtd_linhas": 4}
    assert len(pq) == 2
