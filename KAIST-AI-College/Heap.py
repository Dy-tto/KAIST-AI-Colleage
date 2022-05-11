import heapq
from random import *

class Heap:
    def __init__(self):
        self.queue = []

    def swap(self, i, j):
        tmp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = tmp

    def insert(self, key):
        # 일단 마지막에 삽입
        # 반복을 합니다. 언제까지? 높이
        # root에 도착할 때까지.
        # index가 0일 때까지 (0 <. 0==)
            # parent = self.parent
            # 부모가 자식보다 작을 때까지 타고 올라가면서 교환
        self.queue.append(key) # 마지막에 삽입.
        i = len(self.queue) - 1 # i=마지막 인덱스.
        while i > 0: # root에 도착하지 않았으면.
            parent = self.parent(i) # p 소환.
            if self.queue[i] < self.queue[parent]:
                # i < p.
                self.swap(i, parent)
                i = parent
            else:
                # heap order가 맞다.
                break

    def top(self):
        return self.queue[0]

    def pop(self):
        top = self.queue[0] # 최소값.
        self.swap(0, len(self.queue) - 1) # root,마지막 스왑.
        self.queue.pop() # 마지막을 제거.
        # 맨 마지막 노드가 루트에 와있는 상태.
        # 부모가 자식보다 항상 작아질 때까지
        self.heapify(0)
        return top

    def heapify(self, i):
        # root가 비었으니까 그 자리에 누군가 와야죠.
        # 누군가 온 다음에, heap order를 만족하도록
        # insert처럼 node를 내리거나 올려주는 것.
        # 재귀로 짜셔야 합니다.
        left = self.left(i)
        right = self.right(i)
        smallest = i
        if left < len(self.queue) and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right < len(self.queue) and self.queue[right] < self.queue[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def parent(self, idx):
        return (idx-1) // 2
    
    def left(self, idx):
        # left child of node
        return idx * 2 + 1

    def right(self, idx):
        # right child of node
        return idx * 2 + 2

num_samples = 100
limit = 100000000
samples = []
for i in range(num_samples):
    samples.append(randint(1, limit))

heap = [] # heapq
my_heap = Heap()

for i in range(num_samples):
    heapq.heappush(heap, samples[i]) # min heap
    my_heap.insert(samples[i])

all_pass = True
for i in range(num_samples):
    if heapq.heappop(heap) != my_heap.pop():
        all_pass = False

if all_pass:
    print("pass")
else:
    print("fail")
