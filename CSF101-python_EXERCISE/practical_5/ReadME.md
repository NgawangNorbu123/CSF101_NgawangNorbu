
# Instruction

Implementing a Binary Search Tree and graph data structure
# Binary search tree
Step 1: Define the Node Class
Step 2: Implement the Binary Search Tree Class
Step 3: Implement the Insertion Method
Step 4: Implement the Search Method
Step 5: Implement Traversal Methods
Step 6: Implement the Deletion Method
# Binary data structure
Step 1: Implement the Graph Class
Step 2: Implement Depth-First Search (DFS)
Step 3: Implement Breadth-First Search (BFS)
Step 4: Implement a Method to Find All Paths
Step 5: Implement a Method to Check if the Graph is Connected

# solution for binary search tree
# Example Usage
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

print("In-order:", bst.inorder_traversal())
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())

bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())
print(bst.search(4))
print(bst.search(9))

# output
In-order: [2, 3, 4, 5, 6, 7, 8]
Pre-order: [5, 3, 2, 4, 7, 6, 8]
Post-order: [2, 4, 3, 6, 8, 7, 5]
After deleting 3: [2, 4, 5, 6, 7, 8]
Node found: 4
Node not found: 9

# solution for graph data structure
# Example Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Graph adjacency list:")
g.print_graph()
print("DFS starting from 0:")
g.dfs(0)
print("BFS starting from 0:")
g.bfs(0)
print("All paths from 0 to 3:")
for path in g.find_all_paths(0, 3):
    print(path)
print("Is graph connected?", g.is_connected())

g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is graph connected?", g.is_connected())

# output
0: 1 2
1: 0 2
2: 0 1 3
3: 2
DFS starting from 0: 0 1 2 3
BFS starting from 0: 0 1 2 3
All paths from 0 to 3: [0, 1, 2, 3], [0, 2, 3]
Is graph connected? False
