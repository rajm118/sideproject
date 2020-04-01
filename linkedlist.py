class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    # Start with the empty list
    linkedlist = LinkedList()

    linkedlist.head = Node(1)
    second = Node(2)
    third = Node(3)
    linkedlist.head.next = second
    second.next = third
