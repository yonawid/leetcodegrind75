#lowest common ancestor
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity: O(h) where h is the height of the tree.
        - In a balanced tree, this is O(log n). We only walk down one single path.
        
        Space Complexity: O(1)
        - We just update the 'root' pointer. We didn't use recursion or arrays, 
          so it takes zero extra memory!
        """
        while root:
            # If both targets are greater, they are down the Right branch
            if p.val > root.val and q.val > root.val:
                root = root.right
                
            # If both targets are smaller, they are down the Left branch
            elif p.val < root.val and q.val < root.val:
                root = root.left
                
            # If they split (one is greater, one is smaller) 
            # OR one of them is equal to the current root, we found the ancestor!
            else:
                return root
