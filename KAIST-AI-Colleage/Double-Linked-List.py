class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail

    def add_first(self, data):
        second_node = self.head.next
        new_node = Node(data, self.head, second_node)
        second_node.prev = new_node
        self.head.next = new_node
    
    def add_last(self, data):
        node = Node(data, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node

    def length(self):
        node = self.head.next
        my_length = 0
        while not (node is self.tail):
            node = node.next
            my_length += 1
        return my_length

    def print_all(self):
        node = self.head.next
        while not (node is None) and not (node is self.tail):
            print(node.data)
            node = node.next

    def find_node_by_idx(self, idx):
        node = self.head.next
        while idx > 0:
            node = node.next
            idx -= 1
        return node

    def insert(self, idx, data):
        # TODO
        next_node = self.find_node_by_idx(idx)
        prev_node = next_node.prev
        new_node = Node(data, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node

    def delete(self, idx):
        # TODO
        node = self.find_node_by_idx(idx)
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
