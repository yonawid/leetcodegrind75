# Valid palindrome
class Solution:
    # Approach 1: Cleaning the string, then using Two Pointers
    # Time Complexity: O(n) | Space Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        store="" # Create an empty string to hold our cleaned letters/numbers
        for i in s: # Look at every character in the original string
            if i.isalnum(): # Check if the character is a letter or a number
                store+=i.lower() # Make it lowercase and add it to our clean string
            else:
                continue # Skip spaces and punctuation
        
        l=0 # Set the left pointer to the very beginning (index 0)
        r=len(store)-1 # Set the right pointer to the very end
        
        while l < r: # Keep checking as long as the pointers haven't crossed
            if store[l] == store[r]: # Do the characters at both ends match?
                l+=1 # Move the left pointer one step inward
                r-=1 # Move the right pointer one step inward
            else:
                return False # If they ever don't match, it's not a palindrome!
        
        return True # If the loop finishes with no mismatches, it is a palindrome!


    # Approach 2: Cleaning the string, then reversing it (Neetcode's 1st way)
    # Time Complexity: O(n) | Space Complexity: O(n)
    def isPalindrome2(self, s: str) -> bool:
        store="" # Create an empty string
        for i in s: # Look at every character
            if i.isalnum(): # If it's a letter or number
                store+=i.lower() # Make it lowercase and save it
            else:
                continue # Ignore junk characters
        
        # [::-1] creates a reversed copy of the string
        # If the string is exactly the same forward and backward, it's a palindrome!
        return store == store[::-1] 


    # Approach 3: Two Pointers in-place (Neetcode's optimal way)
    # Time Complexity: O(n) | Space Complexity: O(1) - NO extra memory used!
    def isPalindrome3(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # Start pointers at the very beginning and very end of the original string
        
        while l < r: # Keep going until the two pointers meet in the middle
            
            # If the left pointer is looking at junk (space/comma), keep moving it right
            while l < r and not s[l].isalnum():
                l+=1
                
            # If the right pointer is looking at junk, keep moving it left
            while l < r and not s[r].isalnum():
                r-=1
                
            # Now both pointers are definitely on letters/numbers. Let's compare them!
            # We convert both to lowercase just in case one is Capitalized
            if s[l].lower() != s[r].lower():
                return False # If they don't match, it fails immediately
            
            # If they matched, take one step inward to check the next characters
            l, r = l + 1, r - 1
            
        # If the pointers meet in the middle without any mismatches, we win!
        return True