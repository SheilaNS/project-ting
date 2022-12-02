class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        first_item = self._data[0]
        self._data.pop(0)
        return first_item

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self._data):
            raise IndexError
        return self._data[index]
