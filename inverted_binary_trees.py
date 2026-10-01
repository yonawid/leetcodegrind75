#Inverted binary trees
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time Complexity: O(N) where N is the total number of nodes in the tree.
        Why? Because we have to visit every single node exactly once to swap its children.
        
        Space Complexity: O(H) where H is the height of the tree (worst case O(N)).
        Why? This comes from the "Call Stack". If you dive down 3 levels deep, you have 
        3 "paused" clones waiting. In the worst-case scenario (a tree that looks like a 
        straight line), you could have N clones paused at the same time!
        """
        # BASE CASE: If we hit an empty spot (like the bottom of the tree), stop and return
        if root == None:
            return None
            
        # 1. SWAP: Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # 2. PAUSE & DIVE LEFT: Tell a "clone" to go do this exact process to the new left child
        self.invertTree(root.left)
        
        # 3. UNPAUSE & DIVE RIGHT: Once the left side is totally done, do the same on the right child
        self.invertTree(root.right)
        
        # 4. FINISH: Hand back the completely inverted tree from this point downwards
        return root






    def bfsinvertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time Complexity: O(N) where N is the total number of nodes in the tree.
        Why? Because we still have to visit every single node exactly once to swap its children.
        
        Space Complexity: O(W) where W is the maximum width of the tree (worst case O(N)).
        Why? The queue holds exactly one "level" of the tree at a time. In the worst-case 
        scenario (a perfectly balanced, full tree), the bottom level holds exactly half of 
        all the nodes in the tree (N/2). In big-O notation, we simplify O(N/2) to just O(N).
        """
        # BASE CASE: If the tree is empty, there is nothing to invert.
        if root is None:
            return None
            
        # SETUP: Create a queue (our "To-Do list") and add the top node to start.
        store = deque([root])
        
        # ENGINE: Keep processing as long as there are nodes on our To-Do list.
        while store:
            # 1. GRAB: Take the next node off the *front* of the line.
            front = store.popleft()
            
            # 2. WORK: Swap the entire left and right branches of this specific node.
            front.right, front.left = front.left, front.right
            
            # 3. SCHEDULE: If this node has children, they need their own children swapped too!
            # We add them to the *back* of the line so we process them strictly level-by-level (BFS).
            if front.left is not None:
                store.append(front.left)
            if front.right is not None:
                store.append(front.right)
                
        # FINISH: The original 'root' variable still points to the top node of the tree, 
        # which now has all of its branches completely inverted underneath it.
        return root



        

    def iter_dfs_invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time Complexity: O(N) where N is the total number of nodes in the tree.
        Why? Because we still have to visit every single node exactly once to swap its children.
        
        Space Complexity: O(H) where H is the height of the tree.
        Why? The stack only ever holds the nodes along a single deep path from the top 
        down to the bottom. In a worst-case scenario (a tree shaped like a straight line), 
        the height is N, so it becomes O(N).
        """
        # BASE CASE: If the tree is empty, there is nothing to invert.
        if root is None:
            return None
            
        # SETUP: Create a Stack (our "To-Do list") and add the top node to start.
        # A standard Python list [] works perfectly as a Stack.
        store = [root]
        
        # ENGINE: Keep processing as long as there are nodes on our To-Do list.
        while store:
            # 1. GRAB: Take the next node off the *top/back* of the stack.
            # Using .pop() instead of .popleft() is what forces the algorithm 
            # to dive deep (DFS) instead of scanning wide (BFS).
            front = store.pop()
            
            # 2. WORK: Swap the entire left and right branches of this specific node.
            front.right, front.left = front.left, front.right
            
            # 3. SCHEDULE: If this node has children, they need their own children swapped too!
            # We add them to the top of the stack to be processed next.
            if front.left is not None:
                store.append(front.left)
            if front.right is not None:
                store.append(front.right)
                
        # FINISH: The original 'root' variable still points to the top node of the tree, 
        # which now has all of its branches completely inverted underneath it.
        return root
