from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.__len__() == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        print(self.__len__)
        if (index < 0 or index > self.__len__() - 1):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
