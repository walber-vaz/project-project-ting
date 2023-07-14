from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.list = list()

    def __len__(self):
        """
        Return the length of the list.

        :return: The length of the list.
        :rtype: int
        """
        return len(self.list)

    def enqueue(self, value):
        """
        Adds a value to the end of the list.

        Args:
            value: The value to be added to the list.

        Returns:
            None
        """
        return self.list.append(value)

    def dequeue(self):
        """
        Remove and return the element at the front of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        return self.list.pop(0)

    def search(self, index):
        """
        Search for an element in the list at the given index.

        Parameters:
            index (int): The index of the element to search for.

        Returns:
            object: The element found at the given index.

        Raises:
            IndexError: If the index is invalid or does not exist in the list.
        """
        if index < 0 or index >= len(self.list):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.list[index]
