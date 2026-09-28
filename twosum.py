class Solution:
    def twoSum(self, nums, target):
        #array of nums given 
        #return indices that add up to the target 
        #cant use the same element twice and order doesnot matter 
        store={}
        for i,v in enumerate(nums):
            diff=target-v
            print(f"current number: {i}, complement needed: {diff}, store so far: {store}")
            if diff in store:
                return f"[{store[diff],i}]"
            store[v]=i


    #sorting way to do this using two pointers 
    def twoSumSort(self, nums, target):
        store={}
        for i,v in enumerate(nums):
            if v not in store:
                store[v]=[]
            store[v].append(i)
        nums.sort()
        left=0
        right=len(nums)-1
        while left < right:
            summ=nums[left] + nums[right]
            if summ == target:
                return[store[nums[left]],]
            elif summ<target:
                left+=1
            else:
                right-=1

    def twoSum2(self,nums,target):
        store={}
        for i,v in enumerate(nums):
            store[v]=i
        
        for p in nums:
            val=target-nums[p]
            if val in store:
                return [p,store[val]]
        return []
            
        
        
    

sol = Solution()

# Test 1 - basic
print(sol.twoSum([2, 7, 11, 15], 9))


