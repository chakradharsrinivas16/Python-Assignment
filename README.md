# Python-Assignment
The Solution to the above problem is as follows - 
We have made two appraches to the problem as the entries in the board need to be traversed we followed both the below approaches and code to the below approaches are added as .py files.
- Breadth First Search
- Depth First Search

## 1. Breadth First Search
The Breadth-first search or BFS algorithm is used to search a data structure for an element. It begins at a certain element and investigates all nodes at the current depth level before moving on to entries at the next depth level.

#### Implementation of BFS

We have traversed the board's borders and applied BFS to all of the "O" entries there to identify those that are connected to it because one of its sides is already occupied by "O." We then mark all of these types of entries as "Y" and transform them to "O," whereas other entries were made to "X" because they can be captured.

In order to build the BFS, we employed queues. Each time we removed an entry from the queue, we traversed its surrounded elements and added them to the queue and the process repeats.

## 2. Depth First Search
Depth-first search is an algorithm for searching in data structures. The algorithm starts at the some arbitrary node and explores as far as possible along each branch before backtracking. 
#### Implementation of DFS
In order to determine which "O" entries are connected to it and therefore cannot be captured by "X" because one of its sides is occupied by "O," we traversed the board's borders and performed DFS to all of the "O" entries in the borders. We then marked all of these types of entries to "Y" and transformed them to "O," whereas other entries were made to "X" because they could be captured.

## Time and Space Complexity - 
### 1. Breadth First Search
- Time Complexity : O(m*n)
- Space Complexity : O(m*n)


### 2. Depth First Search
- Time Complexity : O(m*n)
- Space Complexity : O(m*n)

where m,n are rows and columns in board.


## Test run
### 1. Breadth First Search
![image](https://user-images.githubusercontent.com/123494344/215087989-57db998a-d301-476f-9bea-dddb19b036d4.png)

### 2. Depth First Search
![image](https://user-images.githubusercontent.com/123494344/215088085-43afd18a-7d27-4ccb-9360-c327fa937675.png)


Please note that a hardcoded input was taken inorder to run them.
