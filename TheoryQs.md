# CFG Degree 

## Software Assessment 

---

### Section 1: Theory Questions

**1.1 The deque module is part of which python library?**

Deque is part of the _collections_ library

**1.2 What are 2 differences that distinguish a tree from a graph?**

Two difference are:
- A tree always has a root node, where a graph does not necessarily have a root node
- Graphs can have loops or be cyclic, trees have direction (parent/child node) and are acyclic

**1.3 Give the definitions of time complexity and space complexity**

Time Complexity is a measure of how much time an algorithm takes to run.

Space Complexity is a measures of how much memory is taken to run an algorithm.

**1.4 Describe the bubble sort algorithm and its complexity. What is guaranteed at the end of the first pass?**

The bubble sort algorithm sorts by repeatedly swapping adjacent elements until they are in the correct/intended order. 
At the end of the first pass, the largest value is placed in its correct position, the end of an array
if it is the largest value.

The time-space complexity of bubble sort is O(n<sup>2</sup>). This sorting algorithm must iterate through the array multiple times
giving it a worst-case scenario time complexity of O(n<sup>2</sup>) and a best-case of O(n) if the array is already sorted. 
Due to this, it is not suitable for large data sets.

**1.5 Explain what LIFO and FIFO are and how each works in practice with a named data structure**

FIFO, or _First In First Out_, is much like a real life queue that takes data as it comes in. 
All data is processed in the order it comes into the queue. An example of FIFO is the _Queue_ data structure. 
The operation to add something to the end of the queue is called _Enqueue_, while the operation to remove the front element 
from the queue is all called _Dequeue_ (not to be confused with deque).

LIFO, or _Last In First Out_, is like stacking books onto one another. If you want to take a book, 
you need to take the one on top before you can get to the book below. Data is processed in the same way, 
the last piece of data to be added is the first to be taken out. When adding an element to a stack it is called _Push_, 
this adds an element to the top of the stack, while removing the most recent element of the stack is called _Pop_.

**1.6 What is a Balanced Binary Tree and what would be the best root? Walkthrough how you search using this structure.**

It is a type of binary tree in which the difference between height of the left and right subtrees is no more
than one. For each node, the left subtree is a balanced binary tree as well as the right subtree. 
The best root for this type of tree is the median element of the sorted data; 
this allows for relatively balanced left and right subtrees.

Searching a balanced binary tree begins at the root node. The value being searching for is compared 
to the value of the current node. If the value is: 
- **equal** to the current node, the search is successful
- **less than** the current node, the search will move to the left child node of the current node and compare values
- **greater than** the current node, the search will move to the right child node of the current node and compare values

The values will move through the tree and be compared to the left or right child nodes until the search is successful. 

Values that are less than the current node move to the left because, in a balanced binary tree, 
values less than the parent node are stored in the left subtree. Similarly, values greater than the parent node 
are stored in the right subtree.