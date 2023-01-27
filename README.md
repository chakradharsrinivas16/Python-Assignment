# Python-Assignment
The Solution to the above problem is as follows - 
We have made two appraches to the problem as the entries in the board need to be traversed we followed both the below approaches and code to the below approaches are added as .py files.
- Breadth First Search
- Depth First Search

## 1. Breadth First Search

We have traversed the board's borders and applied BFS to all of the "O" entries there to identify those that are connected to it because one of its sides is already occupied by "O." We then mark all of these types of entries as "Y" and transform them to "O," whereas other entries were made to "X" because they can be captured.

#### Implementation of BFS

In order to build the BFS, we employed queues. Each time we removed an entry from the queue, we traversed its surrounded elements and added them to the queue and the process repeats.

## 2. Depth First Search

In order to determine which "O" entries are connected to it and therefore cannot be captured by "X" because one of its sides is occupied by "O," we traversed the board's borders and performed DFS to all of the "O" entries in the borders. We then marked all of these types of entries to "Y" and transformed them to "O," whereas other entries were made to "X" because they could be captured.

Please note that a hardcoded input was taken inorder to run them.
