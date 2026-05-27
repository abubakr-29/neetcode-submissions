class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        topr, botr = 0, m - 1

        while topr <= botr:
            row = (topr + botr) // 2
            if target > matrix[row][-1]:
                topr = row + 1
            elif target < matrix[row][0]:
                botr = row - 1
            else:
                break
        
        if not (topr <= botr):
            return False
        
        row = (topr + botr) // 2
        left, right = 0, n - 1
        while left <= right:
            m = (left + right) // 2
            if target > matrix[row][m]:
                left = m + 1
            elif target < matrix[row][m]:
                right = m - 1
            else:
                return True
        return False