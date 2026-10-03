# Time Complexity: O(n) - We use a single loop that runs n-1 times. 
# Space Complexity: O(1) - We only store two variables, so no extra memory is needed!

class Solution:
    def climbStairs(self, n: int) -> int:
        # 'one' holds the number of ways to reach the current step.
        # 'two' holds the number of ways to reach the step right behind it.
        # We start both at 1 (the answers for 1 step and 0 steps).
        one = 1
        two = 1
        
        # We already have the answer for step 1, so we only need to loop n-1 times.
        for i in range(n - 1):
            
            # To get to the next step, we add the previous two steps together (one + two).
            # Then, we shift our variables forward to get ready for the next loop.
            # 'one' becomes the new sum, and 'two' becomes the old value of 'one'.
            one, two = one + two, one
            
        # When the loop finishes, 'one' has successfully reached step n!
        return one

# Time Complexity: O(2^n) - The recursion tree branches into 2 paths at every step, creating exponential work.
# Space Complexity: O(n) - The "call stack" goes exactly n levels deep before it starts returning answers.

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 'i' represents the current step we are standing on
        def dfs(i):
            
            # Base Case 1: We landed exactly on step n! 
            # This is a valid path, so we count it as 1 way.
            if i == n:
                return 1
            
            # Base Case 2: We accidentally jumped past step n.
            # This path is invalid, so we count it as 0 ways.
            if i > n:
                return 0

            # Recursive Step: Try taking 1 step, and also try taking 2 steps.
            # Add the winning paths from both choices together and return them.
            return dfs(i + 1) + dfs(i + 2)
            
        # Start our journey from the very bottom of the stairs (step 0)
        return dfs(0)
#dp solutions 


# TOP-DOWN DYNAMIC PROGRAMMING (Memoization)
# 
# Time Complexity: O(n)
#   - Without memory, the recursion would branch exponentially: O(2^n).
#   - With memory, we only calculate the answer for each step exactly ONE time.
#   - If there are 'n' steps, we do 'n' calculations. Looking up a saved answer 
#     in our dictionary takes O(1) instant time. Therefore, Total Time = O(n).
#
# Space Complexity: O(n)
#   - We use O(n) space for our 'storage' dictionary to hold the answer for each step.
#   - We also use O(n) space for the "call stack" (the maximum depth the recursion 
#     has to dive before it hits the base case).

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # This dictionary acts as our memory. 
        # Key: The step we are currently standing on (i)
        # Value: The total distinct ways to reach the top from this step
        storage = {}

        # i represents the step we are currently standing on
        def dfs(i):
            
            # --- BASE CASES (When to stop recursing) ---
            
            # 1. We landed exactly on the top step! 
            # This counts as 1 valid path to the top.
            if i == n:
                return 1
                
            # 2. We jumped too far and overshot the top step. 
            # This is an invalid path, so it contributes 0 ways.
            if i > n:
                return 0
                
            # --- DYNAMIC PROGRAMMING (Memoization Check) ---
            
            # If we have already calculated the number of ways to reach the top 
            # from step 'i', do NOT calculate it again. Just return the saved answer.
            if i in storage:
                return storage[i]
                
            # --- RECURSIVE CALCULATION ---
            
            # We haven't calculated this step yet.
            # We can either take a 1-step jump or a 2-step jump.
            # The total ways to reach the top is the sum of both choices.
            else:
                val = dfs(i + 1) + dfs(i + 2)
                
                # IMPORTANT: Save the calculated answer into our memory BEFORE returning!
                # This ensures we never have to do this math for step 'i' ever again.
                storage[i] = val
                
                return val

        # Start our recursive journey at the very bottom of the stairs (step 0)
        return dfs(0)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: 1 step = 1 way, 2 steps = 2 ways
        if n == 1 or n == 2:
            return n
        
        # Create an array of size n+1, filled with 0s. 
        # (We use n+1 so index 3 naturally matches step 3).
        dp = [0] * (n + 1)
        
        # Manually fill in the first two steps that we already know.
        dp[1] = 1
        dp[2] = 2
        
        # Start calculating from step 3 all the way up to step n.
        for i in range(3, n + 1):
            
            # The ways to reach the current step is the sum of the two steps below it.
            dp[i] = dp[i - 1] + dp[i - 2]
            
        # The final answer for step n is at the very end of our array!
        return dp[n]
