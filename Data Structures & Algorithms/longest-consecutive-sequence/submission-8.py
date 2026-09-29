"""
First intuition:
- make a hash map of all elements
- try to make consecutive lists for each number
- drop/save list when there is none +1 greater
does not work because trakcing each consecutive list is O(n**2)

Actually first intuition was correct, but the catch was:
- when to execute findList ?
we know that a number is the start of a sequence if 
hash_index[num - 1] does not exist, so we call findLIst only for them

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create hash map
        hash_index = {}
        for idx, num in enumerate(nums):
            hash_index[num] = False

        # find biggest consecutive list
        def findList(current_number: int):
            list_here = [current_number]
            index = 1
            while True:
                if hash_index.get(num + index) == False:
                    list_here.append(num + index)
                    index += 1
                elif hash_index.get(num + index) == None:
                    return list_here
                else:
                    return list_here

        # create biggest_list for each number
        big_list = []

        for num in nums:
            if hash_index.get(num - 1) != None:
                continue

            hash_index[num] = True
            list_here = findList(num)

            if len(list_here) > len(big_list):
                big_list = list_here
        
        return len(big_list)