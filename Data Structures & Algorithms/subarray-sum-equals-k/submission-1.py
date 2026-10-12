"""
- compute prefix_sum
- do hash map to ease finding teh index necessary for going into K
"""
# k = 12
# [1, 2, 3, 1, 5, 6, 6, 8]
# [1, 3, 6, 7, 12, 18, 24, 32]

# hash_map[6] = 2

from bisect import bisect_left
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 1. prefix sums: a new list, starting with 0 for the empty prefix
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        # 2. prefix value -> every index where it occurs (sorted, since i only grows)
        positions = defaultdict(list)
        for i, p in enumerate(prefix):
            positions[p].append(i)

        # 3. for each end j, count starts i < j with prefix[i] == prefix[j] - k
        count = 0
        for j, p in enumerate(prefix):
            starts = positions.get(p - k, [])
            count_curr = 0
            for num in starts:
                if num < j:
                    count_curr += 1
            count += count_curr
        
        return count