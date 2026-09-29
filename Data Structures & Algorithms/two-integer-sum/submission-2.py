"""
1. brute force -> check each pair of number -> O(n**2)
    1.1. sort the array + start from the number <= target
2. Sorting + Two pointers
3. dict (hash table) and complement
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for idx, number in enumerate(nums):
            possible_ind = hash_table.get(target - number, None)
            if possible_ind != None:
                if possible_ind > idx:
                    return [idx, possible_ind]
                else:
                    return [possible_ind, idx]

            hash_table[number] = idx

