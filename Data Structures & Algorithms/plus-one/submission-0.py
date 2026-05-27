class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plusone = []
        num = ""

        for digit in digits:
            num += str(digit)
        num = int(num)
        num += 1
        num = str(num)
        for digit in num:
            plusone.append(int(digit))
        return plusone
        