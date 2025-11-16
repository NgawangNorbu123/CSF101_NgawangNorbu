
# Documentation

# Main Concepts Applied
# Binary Search Tree (BST):
  - Node-based data structure where left child < parent < right child.
  - Operations: insertion, search, deletion, and traversal (inorder, preorder, postorder).

# Graph Data Structure:
  - Represented using adjacency lists.
  - Operations: DFS, BFS, find all paths, connectivity check.
  - Explored both recursive and iterative traversal approaches.

# Reflection

# What I Learned
- BST is efficient for ordered data storage and retrieval.
- Traversal methods allow different orderings for processing nodes.
- Graph representation using adjacency lists is memory efficient for sparse graphs.
- DFS and BFS are fundamental graph traversal algorithms.
- Recursive DFS helps with path finding and connectivity checking.

# Challenges Faced
1. BST Deletion Edge Cases:
   - Deleting nodes with two children required careful replacement using in-order successor.
   - Solved by implementing a `_min_value()` helper function.

2. Graph DFS and Connectivity Check:
   - Initially visited nodes were not tracked properly, causing infinite recursion.
   - Resolved by maintaining a `visited` set.

3. Finding All Paths in Graph:
   - Avoiding cycles required keeping a copy of the path for each recursive call.
