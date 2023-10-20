from node import Node


class LinkedList2:
    """Implements linked list by adding node to front of linked list"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Returns true if linked list is empty, else false"""
        if self.head is None:
            return True
        return False

    def view_list(self):
        """prints each value in the linked list"""
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def size(self):
        """Returns size of linked list"""
        index = 0
        current = self.head
        while current is not None:
            index += 1
            current = current.next
        return index

    def insert(self, value):
        """Inserts new node with value at beginning of linked list"""
        node = Node(value)
        old_node = self.head
        self.head = node
        self.head.next = old_node

    def search(self, value):
        """Returns index of node with value"""
        current = self.head
        index = 0
        while current != None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def remove_by_value(self, value, all=False):
        """Removes a node by its value, will remove all nodes with value if second parameter is set to True"""
        if self.head is not None and self.head.value == value:
            self.head = self.head.next
            if not all:
                return
        current = self.head
        while current is not None and current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                if not all:
                    return
            current = current.next
        return -1

    def remove_by_index(self, index):
        """Removes a node by its index"""
        if self.head is not None and index == 0:
            node_value = self.head.value
            self.head = self.head.next
            return node_value
        current = self.head
        idx = 1
        while current is not None:
            if idx == index:
                node_value = current.next.value
                current.next = current.next.next
                return node_value
            current = current.next
            idx += 1
        return -1


if __name__ == "__main__":
    print("\nAdd new node to front")
    front_list = LinkedList2()
    print(front_list.is_empty())  # True
    front_list.insert(1)
    front_list.insert(3)
    front_list.insert(5)
    front_list.insert(6)
    front_list.insert(8)
    front_list.insert(10)
    front_list.insert(-5)
    print(front_list.is_empty())  # False
    print(front_list.size())  # 7
    print(front_list.search(8))  # 2
    print(front_list.search(2))  # -1

    print()
    front_list.view_list()  # -5, 10, 8, 6, 5, 3, 1
    print()

    print(front_list.remove_by_index(1))  # 10

    front_list.remove_by_value(1)

    print()
    front_list.view_list()  # -5, 8, 6, 5, 3
    print()
