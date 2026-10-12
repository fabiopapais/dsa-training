"""
1. Brute force solution:
- For each number, look for other 2 possible candidates to make = 0
- Not feasible because it takes O(n^3).

2. First intuition
- Build an invert index for each number
- Slide two pointers from each end and sum each pair
- Find complement to 0 for each pair
- think onedge cases later:
    - the two pointers don't validate all possible triplets

3. Second intuition (buildup on last one)
Maybe use pointers but on a sorted array, 
think on pointers movement conditions
- Build an invert index for each number
- sort array
- slide two pointers, move the largest
- Find complement to 0 for each pair
- insert sorted triplet

4. Solution
- sort the list
- for each value, do:
    - put two pointers, one after the current value and other in the end
    - if a = 0, skip
    - if sum == 0, add to triplet (skip repetitions)
    - if sum > 0, decrease r. else increase l

"""

from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array
        nums = sorted(nums)
        nums_len = len(nums) - 1
        
        triplets = []
        for i, value in enumerate(nums):
            if nums[i] > 0:
                break

            l, r = i + 1, nums_len
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    triplet = sorted([nums[i], nums[l], nums[r]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                
                if threeSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return triplets

            