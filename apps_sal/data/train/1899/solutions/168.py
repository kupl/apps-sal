class Solution:

    def mark_island(self, A, row, column, marker, border_coordinates):
        if 0 <= row < len(A) and 0 <= column < len(A[0]) and (A[row][column] != marker):
            if A[row][column] == 0:
                return True
            else:
                A[row][column] = marker
                rets = [self.mark_island(A, row + 1, column, marker, border_coordinates), self.mark_island(A, row - 1, column, marker, border_coordinates), self.mark_island(A, row, column + 1, marker, border_coordinates), self.mark_island(A, row, column - 1, marker, border_coordinates)]
                if True in rets:
                    border_coordinates.append((row, column))
        return False

    def shortestBridge(self, A: List[List[int]]) -> int:
        border_coordinates = [[], []]
        marker = 2
        smallest_distance = len(A) * len(A[0])
        for row in range(len(A)):
            for column in range(len(A[0])):
                if A[row][column] == 1:
                    self.mark_island(A, row, column, marker, border_coordinates[marker - 2])
                    marker += 1
        for coordinates1 in border_coordinates[0]:
            for coordinates2 in border_coordinates[1]:
                distance = abs(coordinates1[0] - coordinates2[0]) + abs(coordinates1[1] - coordinates2[1]) - 1
                if distance < smallest_distance:
                    smallest_distance = distance
        return smallest_distance
