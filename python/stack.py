from node import Node


class Stack:
    """Implenting a stack data structure with methods for push, pop, peek, size, and is_empty"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"| {self.head if self.head is not None else ''} <>"

    def __iter__(self):
        self.n = self.head
        return self

    def __next__(self):
        if self.n is not None:
            value = self.n.value
            self.n = self.n.next
            return value
        else:
            raise StopIteration

    def push(self, value):
        """push a node with value on to the top of the stack"""
        node = Node(value)
        old_head = self.head
        self.head = node
        self.head.next = old_head

    def pop(self):
        "pop a node off the top of the stack"
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        """return the value of the top node in the stack"""
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        """returns the size of the stack"""
        current = self.head
        index = 0
        while current is not None:
            index += 1
            current = current.next
        return index

    def is_empty(self):
        """returns boolean for whether the stack is empty or not"""
        if self.head is None:
            return True
        return False


def reverse_string(string):
    stack = Stack()
    for letter in string:
        stack.push(letter)
    new_string = ""
    for letter in stack:
        new_string += stack.pop()
    # for letter in stack:
    #     new_string += letter
    return new_string


if __name__ == "__main__":
    print("Stack methods: ")
    stack = Stack()
    print(stack.is_empty())  # True
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(8)
    stack.push(10)
    print(stack)
    print(stack.is_empty())  # False
    print(stack.size())  # 5
    print(stack.pop())  # 10
    print(stack.peek())  # 8

    print("Reverse string function: ")
    print(reverse_string("hello world"))
    print(reverse_string("My coding skills are mighty and awesome"))
