class CircularQueue:
    def __init__(self, size=0):
        self.items = []
        self.size = size
        for i in range(size):
            self.items.append(None)
        self.front = 0
        self.rear = 0

    def enqueue(self, value):
        if self.items[self.rear] is None:
            self.items[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True
        else:
            return False

    def dequeue(self):
        if self.items[self.front] is not None:
            res = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.size
            return res
        else:
            return False
    
    def is_empty(self):
        return self.front == self.rear and self.items[self.front] is None
    
    def is_full(self):
        return self.front == self.rear and self.items[self.front] is not None

queue = CircularQueue(5)
for i in range(6):
    res = queue.enqueue(i)
    if res:
        print("push: ", i)
    else:
        print("push failed")

print(queue.is_empty())
print(queue.is_full())
while not queue.is_empty():
    print("pop: ", queue.dequeue())
