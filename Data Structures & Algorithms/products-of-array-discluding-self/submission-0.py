class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_without_zero = 1
        product_with_zero = 1
        number_of_zeros = 0

        for num in nums:
            product_with_zero *= num
            if num != 0:
                product_without_zero *= num
            else:
                number_of_zeros += 1
        
        if number_of_zeros > 1:
            product_without_zero = 0

        output = [product_with_zero] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                output[i] = product_without_zero
            else:
                output[i] = int(product_with_zero / nums[i])

        return output