class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        lp = 0
        rp = 0
        m = (nums[0], 0)

        while rp < k:
            if nums[rp] >= m[0]:
                m = (nums[rp], rp)
            rp += 1

        ans.append(m[0])
        while rp < len(nums):
            if m[1] != lp:
                if nums[rp] >= m[0]:
                    m = (nums[rp], rp)
            else:
                i = lp + 1
                m = (nums[i], i)
                while i <= rp:
                    if nums[i] > m[0]:
                        m = (nums[i], i)
                    i += 1
            ans.append(m[0])
            lp += 1
            rp += 1
        return ans

                

        