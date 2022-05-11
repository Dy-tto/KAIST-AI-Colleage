class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None)
    
    def add_first(self, data):
        second_node = self.head.next
        new_node = Node(data)
        new_node.next = second_node
        self.head.next = new_node

    def add_last(self, data):
        node = self.head
        while not (node.next is None):
            node = node.next
        node.next = Node(data)
    
    def print_all(self):
        node = self.head.next
        while not (node is None):
            print(node.data)
            node = node.next

    def length(self):
        node = self.head.next
        my_length = 0
        while not (node is None):
            node = node.next
            my_length += 1
        return my_length

    def find_by_idx(self, idx):
        node = self.head.next
        while idx > 0:
            node = node.next
            idx -= 1
        return node.data
    
    def find_node_by_idx(self, idx):
        node = self.head.next
        while idx > 0:
            node = node.next
            idx -= 1
        return node

    def find_by_value(self, data):
        # 못 찾으면 None
        node = self.head.next
        idx = 0
        while not (node is None):
            if node.data == data:
                return idx
            
            idx += 1
            node = node.next
        return None

    def insert(self, idx, data):
        if idx == 0:
            self.add_first(data)
        elif idx == self.length():
            self.add_last(data)
        else:
            node = self.find_node_by_idx(idx - 1)
            new_node = Node(data)
            next_node = node.next
            new_node.next = next_node
            node.next = new_node

    def delete_first(self):
        next_node = self.head.next.next
        self.head.next = next_node

    def delete_by_idx(self, idx):
        if idx == 0:
            self.delete_first()

        else:
            prev_node = self.find_node_by_idx(idx-1)
            node = prev_node.next
            prev_node.next = node.next
    
    def delete_last(self):
        self.delete_by_idx(self.length()-1)
        
