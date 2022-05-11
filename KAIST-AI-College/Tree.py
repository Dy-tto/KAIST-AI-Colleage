class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def height(node, depth):
    if node == None:
        return depth - 1

    left_h = height(node.left, depth + 1)
    right_h = height(node.right, depth + 1)
    return max(left_h, right_h)

def num_node(node):
    if node is None:
        return 0
    return 1 + num_node(node.left) + num_node(node.right)

def preorder(node):
    print(node.key, end=' ')
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)

def inorder(node):
    if node.left is not None:
        inorder(node.left)
    print(node.key, end=' ')
    if node.right is not None:
        inorder(node.right)

def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.key, end=' ')

def levelorder(node):
    q = [node]
    while q:
        iter = q.pop(0)
        print(iter.key, end=' ')
        if iter.left:
            q.append(iter.left)
        if iter.right:
            q.append(iter.right)

root = Node('8',\
    Node('3',\
        Node('1'),\
        Node('6',\
            Node('4'),\
            Node('7'))),\
    Node('10',\
        None,\
        Node('14',\
            Node('13'),\
            None)))

#print(height(root, 0))
#print(num_node(root))
levelorder(root)
