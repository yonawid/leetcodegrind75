class Solution:

    # ─── APPROACH 1: Hashmap One-Pass ───────────────────────────────
    # Time: O(n)  |  Space: O(n)
    # Build and check the store in a single loop
    def twoSum(self, nums, target):
        store = {}                          # maps value → index
        for i, v in enumerate(nums):
            diff = target - v               # complement we need to find
            if diff in store:               # have we seen the complement before?
                return [store[diff], i]     # yes → return both indices
            store[v] = i                    # no → store this value for future lookups


    # ─── APPROACH 2: Sort + Two Pointers ────────────────────────────
    # Time: O(n log n)  |  Space: O(n)
    # Sort first, then close in from both ends
    def twoSumSort(self, nums, target):
        store = {}
        for i, v in enumerate(nums):        # save original indices before sorting
            if v not in store:
                store[v] = []
            store[v].append(i)              # handle duplicates: store list of indices
        nums.sort()                         # sort values (original indices now in store)
        left = 0
        right = len(nums) - 1
        while left < right:
            summ = nums[left] + nums[right] # sum the values at both pointers
            if summ == target:
                # look up original indices from the store
                if nums[left] == nums[right]:               # duplicate values
                    return [store[nums[left]][0], store[nums[left]][1]]
                else:
                    return [store[nums[left]][0], store[nums[right]][0]]
            elif summ < target:
                left += 1                   # sum too small → move left pointer right
            else:
                right -= 1                  # sum too big  → move right pointer left


    # ─── APPROACH 3: Hashmap Two-Pass ───────────────────────────────
    # Time: O(n)  |  Space: O(n)
    # First build the full store, then search for complements
    def twoSum2(self, nums, target):
        store = {}
        for i, v in enumerate(nums):        # PASS 1: store all values → indices
            store[v] = i

        for i, p in enumerate(nums):        # PASS 2: look for each complement
            val = target - p
            if val in store and store[val] != i:  # found AND not the same element
                return [i, store[val]]
        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))       # [0, 1]
print(sol.twoSumSort([3, 2, 4], 6))        # [1, 2]
print(sol.twoSum2([3, 3], 6))              # [0, 1]


