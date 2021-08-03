class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        ones_up_to_index_rows = [[0] for i in range(len(grid))]
        ones_up_to_index_columns = [[0] for i in range(len(grid[0]))]
        ret = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                ones_up_to_index_rows[row].append(ones_up_to_index_rows[row][-1] + grid[row][column])
                ones_up_to_index_columns[column].append(ones_up_to_index_columns[column][-1] + grid[row][column])

        for row in range(len(grid)):
            column = 0

            if (len(grid) - row > ret):
                for column in range(len(grid[0])):
                    next_column = column

                    while (next_column < len(grid[0]) and grid[row][next_column] == 1):
                        next_column += 1

                    for i in range(next_column - 1, column - 1, -1):
                        side_length = i - column + 1

                        if (side_length <= ret):
                            break

                        row_index_dp = row + side_length - 1

                        if (row_index_dp < len(grid)
                           and ones_up_to_index_columns[i][row_index_dp + 1] - ones_up_to_index_columns[i][row] == side_length
                           and ones_up_to_index_rows[row_index_dp][i + 1] - ones_up_to_index_rows[row_index_dp][column] == side_length
                           and ones_up_to_index_columns[column][row_index_dp + 1] - ones_up_to_index_columns[column][row] == side_length):
                            ret = side_length
                            break
            else:
                break

        return ret ** 2
