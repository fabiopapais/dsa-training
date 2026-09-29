"""
1. First intuition
- Generate signature (frequency map) of each word
- Compare each signature with each one
- Group equal signatures

generate the frequency for each word requires 10**5 (N) in worst case
compare each signature requires N in worst case (no groups)

possible optimization -> group equal size groups
possible optimization -> create a raw signature other than tuple and ordered stuff (hsash function)

"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        signatures = defaultdict(list)
        for string in strs:
            signature = {}
            for char in string:
                if char in signature:
                    signature[char] += 1
                else:
                    signature[char] = 1
            
            tuple_signature = tuple(sorted(signature.items())) # make it hashable
            
            signatures[tuple_signature] += [string]

        return list(signatures.values())

        