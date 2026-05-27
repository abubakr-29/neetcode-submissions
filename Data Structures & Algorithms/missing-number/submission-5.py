class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        sum1 = (n * (n + 1)) // 2
        sum2 = sum(nums)
        res = sum1 - sum2
        return res