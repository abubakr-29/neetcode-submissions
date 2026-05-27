class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []

        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                res *= nums[j]
            prod.append(res)
        return prod