class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        METHOD 1: Two Tally Charts (Two Hash Maps)
        Time Complexity: O(N) - We iterate through strings of length N.
        Space Complexity: O(1) - The dictionary will never hold more than 26 English letters.
        """
        # 1. Quick length check
        if len(s) != len(t):
            return False
            
        # 2. Build the first tally chart for string 's'
        store = {}
        for char in s:
            if char in store:
                store[char] += 1
            else:
                store[char] = 1
                
        # 3. Build the second tally chart for string 't'
        store2 = {}
        for char in t:
            if char in store2:
                store2[char] += 1
            else:
                store2[char] = 1
                
        # 4. If the tallies are perfectly identical, they are anagrams!
        return store == store2      

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        METHOD 2: The "Cross-Off" Method (Single Hash Map)
        Time Complexity: O(N) - We iterate through strings of length N.
        Space Complexity: O(1) - The dictionary will never hold more than 26 English letters.
        """
        # 1. Quick length check
        if len(s) != len(t):
            return False
            
        # 2. Build the tally chart for string 's'
        store = {}
        for char in s:
            if char in store:
                store[char] += 1
            else:
                store[char] = 1
                
        # 3. "Cross off" letters as we scan through string 't'
        for char in t:
            if char in store:
                store[char] -= 1
                
                # RED FLAG: If count drops below 0, 't' has too many of this letter
                if store[char] < 0:
                    return False
            else:
                # RED FLAG: If the letter isn't in our chart at all
                return False
                
        # 4. If we crossed everything off without triggering any red flags, we're good!
        return True 
