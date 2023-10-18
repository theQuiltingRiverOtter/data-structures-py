from node import Node

# peek - return last item


class Queue:
    """Implements a queue data structure that adds items to end of list and removes them from beginning"""

    def __init__(self):
        self.head = None

    def enqueue(self, value):
        """Adds items to end of queue"""
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node

    def dequeue(self):
        """Removes item from beginning of queue"""
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        """Returns item at beginning of queue(last item)"""
        if self.head.value is None:
            return None
        return self.head.value

    def size(self):
        """Returns number of items"""
        current = self.head
        index = 0
        while current is not None:
            index += 1
            current = current.next
        return index

    def is_empty(self):
        """Returns True if the queue is empty, False if it is not"""
        if self.head is None:
            return True
        return False


if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())  # True
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue("hello")
    queue.enqueue("goodbye")
    queue.enqueue(42)
    print(queue.is_empty())  # False
    print(queue.peek())  # 4
    print(queue.dequeue())  # 4
    print(queue.peek())  # 5
    print(queue.size())  # 4
