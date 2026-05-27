class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = 0

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for bananas in piles:
                totalTime += math.ceil(bananas / mid)
            if totalTime <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1        
        return k