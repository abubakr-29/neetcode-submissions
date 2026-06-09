class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Since python has min heap only so we make all the weights negative to simulate max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # first weight will always be the heaviest but we're using negative weights, therefore second > first
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])                