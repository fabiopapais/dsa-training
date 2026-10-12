"""
1. Brute force solution
- scan every possible pair
- compute amount and record highest
not feasible because O(n^2) and height.length > 10^3

2. First intuition (solution also)
- start pointers in both ends
- compute amount and record highest
- move end where the bar is lower

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        highest = 0
        while l < r:
            amount = (r - l) * min(heights[l], heights[r])
            if amount > highest:
                highest = amount
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return highest