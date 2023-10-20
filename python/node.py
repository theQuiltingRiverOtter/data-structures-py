class Node:
    """Node class with attributes for the value and a point to the next node"""

    def __init__(self, value):
        self.value = value
        self.next = None

    # def __str__(self):
    #     return f"{self.value}"

    def __repr__(self):
        return f"{self.value}{',' if self.next is not None else ''} {self.next if self.next is not None else ''}"
