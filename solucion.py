class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

from collections import deque

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def topView(root):
    if root is None:
        return

    # Cola para el recorrido BFS
    queue = deque()

    # Distancia horizontal -> valor del nodo
    top_nodes = {}

    # (nodo, distancia_horizontal)
    queue.append((root, 0))

    while queue:
        node, hd = queue.popleft()

        # Solo guardar el primer nodo visto
        if hd not in top_nodes:
            top_nodes[hd] = node.info

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))

    # Imprimir de izquierda a derecha
    for hd in sorted(top_nodes):
        print(top_nodes[hd], end=" ")



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)