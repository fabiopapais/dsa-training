class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        for item in nums:
            if item in appeared and appeared[item] == True:
                return True
            else:
                appeared[item] = True
        return False