from node import Node


class LinkedList:
    """Linked List implementation with new node appended to end"""

    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert node with value at end of linked list"""
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = node

    def is_empty(self):
        """ "Returns True if the linked list is empty, else False"""
        if self.head is None:
            return True
        return False

    def search(self, value):
        """Returns the index of a value in the linked list"""
        index = 0
        current = self.head
        while current != None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def view_list(self):
        """prints each value in the linked list"""
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

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

    def size(self):
        """Returns the size of a list"""
        index = 0
        current = self.head
        while current != None:
            index += 1
            current = current.next
        return index


if __name__ == "__main__":
    print("Add new node to back")
    new_list = LinkedList()
    print(new_list.is_empty())  # True
    new_list.insert(5)
    print(new_list.is_empty())  # False
    new_list.insert(10)
    new_list.insert(15)
    new_list.insert(25)
    new_list.insert(35)
    new_list.insert(25)
    new_list.view_list()  # print numbers 5, 10, 15, 25, 35, 25
    print()
    print(new_list.remove_by_index(2))  # 15
    print()
    new_list.view_list()  # print numbers 5, 10, 25, 35, 25
    print()
    print(new_list.search(25))  # 2
    print(new_list.search(40))  # -1
    print()
    new_list.remove_by_value(25, all=True)
    new_list.view_list()  # print numbers 5, 10, 35
    print(new_list.size())  # 3
    print(new_list.remove_by_value(50))  # -1
    print(new_list.remove_by_index(10))  # -1
