class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                num = int(board[r][c]) - 1
                mask = 1 << num
                grid = (r // 3) * 3 + (c // 3)

                if rows[r] & mask or cols[c] & mask or squares[grid] & mask:
                    return False

                rows[r] |= mask
                cols[c] |= mask
                squares[grid] |= mask
        return True

