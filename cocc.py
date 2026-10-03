# Time Complexity: O(log n) - We cut the search space in half every iteration (Binary Search).
# Space Complexity: O(1) - We only use two variables (left and right), no extra memory needed.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Set search boundaries. left is first version (1), right is last version (n).
        left, right = 1, n
        
        # Keep looping until left and right meet (meaning we found the exact version).
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version is either mid or something before it.
                right = mid
            else:
                # If mid is good, the first bad version MUST be strictly after mid.
                left = mid + 1
                
        # When left == right, we have pinpointed the exact first bad version.
        return left
