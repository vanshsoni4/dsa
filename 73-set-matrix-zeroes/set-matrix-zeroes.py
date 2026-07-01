class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        first_col = False

        # Step 1: Use first row and column as markers
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Update the matrix using markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle the first row
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Step 4: Handle the first column
        if first_col:
            for i in range(m):
                matrix[i][0] = 0