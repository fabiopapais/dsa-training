"""
1. sort
O(n log n + m log m)

2. dictionary of frequencies
O(n + m + t)
t: the number of single chars in both strings

3. hash map of dictionaries
string -> ASCII number -> module operator -> hash function
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        appeared = {}
        for char in s:
            if char in appeared:
                appeared[char] += 1
            else:
                appeared[char] = 1
        
        for char in t:
            if char in appeared:
                appeared[char] -= 1
                if appeared[char] < 0:
                    return False
                if appeared[char] == 0:
                    appeared.pop(char, None)  
            else:
                return False
        
        if appeared != {}:
            return False

        return True 