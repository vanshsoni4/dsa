class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):

        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val):

        newNode = Node(val)

        newNode.next = self.head
        self.head = newNode

        self.size += 1

    def addAtTail(self, val):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.size += 1
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode
        self.size += 1

    def addAtIndex(self, index, val):

        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        newNode = Node(val)

        current = self.head

        for _ in range(index - 1):
            current = current.next

        newNode.next = current.next
        current.next = newNode

        self.size += 1

    def deleteAtIndex(self, index):

        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head

        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next

        self.size -= 1