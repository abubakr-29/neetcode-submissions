class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        res = 0

        while left < right:
            cap = 0
            if heights[left] <= heights[right]:
                cap = heights[left] * (right - left)
                left += 1
            else:
                cap = heights[right] * (right - left)
                right -= 1
            res = max(res, cap)

        return res