
# Documentation

# Main Concepts Applied
In this practical, I implemented and explored Linked Lists, a fundamental dynamic data structure.  
The key concepts used were:
- Nodes and pointers – each node contains data and a reference to the next node.
- Dynamic memory allocation – unlike arrays, linked lists grow and shrink at runtime.
- Pointer manipulation – updating node links to reverse, merge, and remove nodes efficiently.
- Two-pointer approach – used in both reversing and removing the Nth node from the end.

# Reflection

# What I Learned
- I know how to build a linked list from scratch by creating my own Node and LinkedList 'blueprints' (classes).

I can move through (or traverse) the list to look at every item.

I learned a clever trick to reverse a whole list just by changing where the pointers point—I don't need any extra storage!

I can combine two lists that are already sorted into one big sorted list by using an iterative approach (a loop) and a temporary dummy node to start the new list.

I can remove the Nth item from the end of the list really fast by using a two-pointer method.

---

# Challenges Faced
1 Infinite Loop When Reversing:
I got stuck because I forgot the most important step: telling the list to move to the next node inside my loop (current = next_node).

I fixed it by making sure the pointer that travels through the list was always correctly updated.

2. Deleting the Wrong Item:
When trying to remove the Nth item from the end, I mixed up the starting distance (offset) between my fast and slow pointers.

I solved this by using an extra dummy node at the very beginning, which made it easy to handle tricky situations like deleting the first node in the list.

3. Merging Empty Lists:
My list merging code broke when one of the lists was empty.

The fix was simple: I added a final check to see if either list still had items left and attached the remaining list to the end of the new merged list.
     ```

# Conclusion
This whole exercise really deepened my knowledge of linked lists and the tricky algorithms that use pointers. It was a huge help in sharpening my logical problem-solving and debugging skills, especially when dealing with those tough edge cases and manipulating pointers in Python.