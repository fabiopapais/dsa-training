"""
First intituiton (N log N)
1. Make a dictionary of frequencies
2. sort the dictionary
3. get top k freqs

Optimal solution (N)
1. Make a dictionary of frequencies
2. Make a list of unique frequencies in order (size of initial nums)
3. Go through it in reverse order


NÃO USAR [[]] * n

"""


from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = defaultdict(int) # default values are 0
        for item in nums:
            freqs[item] += 1
        
        unique_freqs = [[] for _ in range(len(nums) + 1)]

        for key, value in freqs.items():
            unique_freqs[int(value)].append(int(key))

        results = []
        for group in reversed(unique_freqs):
            if len(results) >= k:
                break
            results.extend(group)

        return results[:k]
    

