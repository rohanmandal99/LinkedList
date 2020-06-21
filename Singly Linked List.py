class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        counter = 1
        temp = self.head
        while temp.next is not None:
            counter += 1
            temp = temp.next
        print(counter)

    def printList(self):
        li = []
        temp = self.head
        while temp:
            li.append(temp.data)
            temp = temp.next
        print(li)

    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self, pos):
        temp = self.head
        counter = 1
        while counter != pos:
            temp = temp.next
            counter += 1
        return temp

    def insert(self, index, new_data):
        if index == 0:
            self.prepend(new_data)
            return

        new_node = Node(new_data)
        leader = self.traverse(index - 1)
        holding_pointer = leader.next
        new_node.next = holding_pointer
        leader.next = new_node

    def delete(self, index):
        leader = self.traverse(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next


ll = LinkedList()
ll.head = Node(10)
second = Node(5)
third = Node(16)

ll.head.next = second
second.next = third

ll.prepend(1)
ll.append(2)
ll.insert(4, 99)
ll.printList()
ll.length()
ll.delete(4)
ll.printList()
ll.length()
# https://github.com/theja-m/Data-Structures-and-Algorithms
