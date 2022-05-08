class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_key(self.root, key)

    def _insert_key(self, node, key):
        if node is None:
            node = Node(key)
        else:
            if key <= node.key:
                node.left = self._insert_key(node.left, key)
            else:
                node.right = self._insert_key(node.right, key)
        return node
    
    def find(self, key):
        return self._find_key(self.root, key)
    
    def _find_key(self, node, key):
        if node is None:
            return False
        
        if node.key == key:
            return True

        if key < node.key:
            return self._find_key(node.left, key)
        else:
            return self._find_key(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_key(self.root, key)
        return deleted

    def _delete_key(self, node, key):
        if node is None:
            return node, False
        
        deleted = False
        if key == node.key:
            deleted = True
            if node.left and node.right: # 자식 2명
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
                
            elif node.left or node.right: # 자식 1명
                if node.left:
                    node = node.left
                else:
                    node = node.right
                    
            else: # 자식 x
                node = None
        elif key < node.key:
            node.left, deleted = self._delete_key(node.left, key)
        else:
            node.right, deleted = self._delete_key(node.right, key)
        
        return node, deleted

def levelorder(node):
    q = [node]
    while q:
        iter = q.pop(0)
        print(iter.key, end=' ')
        if iter.left:
            q.append(iter.left)
        if iter.right:
            q.append(iter.right)

bst = BinarySearchTree()
arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 8, 9]
for i in arr:
    bst.insert(i)

bst.delete(5)
levelorder(bst.root)
