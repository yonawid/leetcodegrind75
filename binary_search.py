#Binary search 
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value in a sorted array using Binary Search.
        
        Time Complexity: O(log n)
        - We cut the search space in half with every iteration of the loop.
        
        Space Complexity: O(1)
        - We only use a few integer variables (l, r, mid) regardless of how 
          large the input array is. No extra memory is allocated.
        """
        # Set pointers for the left and right edges of our search space
        l, r = 0, len(nums) - 1
        
        # Keep searching as long as the search space is valid
        while l <= r:
            # Find the middle index of the current search space
            mid = (l + r) // 2
            
            # If the middle value is our target, we found it! Return its index
            if nums[mid] == target:
                return mid
                
            # If the middle value is too big, the target must be in the left half. 
            # We can safely discard the right half.
            elif nums[mid] > target:
                r = mid - 1
                
            # If the middle value is too small, the target must be in the right half.
            # We can safely discard the left half.
            elif nums[mid] < target:
                l = mid + 1
                
        # If the loop finishes, the target wasn't in the array
        return -1
    

    def search2(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value using Recursive Binary Search.
        
        Time Complexity: O(log n)
        - We cut the search space in half with every recursive call.
        
        Space Complexity: O(log n)
        - Unlike the while loop, recursion uses "Call Stack" memory. 
          Because we divide the array in half each time, we make at most 
          log(n) recursive calls, so the stack grows to a depth of log(n).
        """
        
        def helper(l, r):
            # BASE CASE: Our pointers crossed, which means our search space 
            # is empty and the target isn't here.
            if l > r:
                return -1
                
            # Find the middle index of the current search space
            mid = (l + r) // 2
            
            # If the middle value is our target, we found it!
            if nums[mid] == target:
                return mid
                
            # If the middle value is too big, delegate the left half to a clone
            # and RETURN whatever answer that clone eventually finds.
            elif nums[mid] > target:
                return helper(l, mid - 1)
                
            # If the middle value is too small, delegate the right half to a clone
            # and RETURN whatever answer that clone eventually finds.
            elif nums[mid] < target:
                return helper(mid + 1, r)

        # Kick off the very first recursive call with the full array boundaries
        return helper(0, len(nums) - 1)

    def search3(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value using Upper Bound Binary Search.
        Instead of looking for the target directly, we look for the exact 
        boundary where numbers become STRICTLY GREATER than the target.
        """
        # Right boundary is out-of-bounds (len(nums)) instead of len(nums) - 1
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid is greater, the upper bound is at or before mid
            if nums[mid] > target:
                r = mid
            # If mid is <= target, the upper bound must be strictly after mid
            else:
                l = mid + 1
                
        # When the loop breaks, 'l' is the index of the first number GREATER than target.
        # This means the target, if it exists, MUST be exactly at 'l - 1'.
        
        # Check if l > 0 (to avoid index -1) AND if the number at l - 1 is our target
        if l > 0 and target == nums[l - 1]:
            return l - 1
            
        # Target was not in the array
        return -1
