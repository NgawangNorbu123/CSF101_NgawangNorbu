
# Documentation
In this practical, I implemented three types of search algorithms:

1. Linear Search
Sequentially checks each element in the list until the target is found or the list ends.
Works on unsorted lists.
Time complexity: O(n).

2. Binary Search (Iterative)
Works only on sorted lists.
Repeatedly divides the search range in half and compares the middle element to the target.
Time complexity: O(log n).

3. Binary Search (Recursive)
Same logic as iterative binary search but implemented using recursion.
Recursively searches either the left or right half of the array.
Time complexity: O(log n), with extra space due to recursive call stack.

# Reflection
"I now understand the different ways to search for things in a list:

Search Techniques
Linear search is easy to do, but it's really slow when you have a lot of data.

Binary search is much, much faster than linear search, but there's a catch: the data must be sorted first.

I learned that recursion (when a function calls itself) can make the code for binary search look cleaner and easier to read.

Key Takeaways:
The most important things I learned are:

Always sort your data before you try to use binary search.

I know how to handle situations when the item I'm looking for isn't in the list by using a return value like -1."

# Challenges Faced and Solutions

"I now understand the core differences between recursion and iteration. While recursion involves a function repeatedly calling itself until a base case is reached, iteration uses loops to execute steps until a specific condition is met.

I've noted that although recursive code can be cleaner and more elegant, iteration is generally preferred for its improved speed and memory efficiency.

Furthermore, designing pseudocode and flowcharts for simple tasks like calculating a rectangle's area or converting temperatures has proven invaluable. This planning stage has not only helped me think more logically but also solidified the importance of pre-planning any programming solution.

# Conclusion
This practical provided a clear understanding of the strengths and limitations of different search algorithms.

I concluded that linear search is simple but inefficient for large datasets, whereas binary search offers superior efficiency but comes with the strict requirement of sorted data.

Furthermore, while recursion can lead to more elegant algorithms, this exercise reinforced that mastering the base cases is absolutely essential to prevent critical errors.

Overall, this work significantly improved my problem-solving skills and deepened my grasp of both iterative and recursive search techniques.
