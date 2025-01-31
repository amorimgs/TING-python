from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        try:
            if index < 0 or index > len(self.data):
                raise IndexError()
            return self.data[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
