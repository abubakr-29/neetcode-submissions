class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        r = abs(n)
        res = x * self.myPow(x, r - 1)
        
        return res if n >= 0 else 1 / res