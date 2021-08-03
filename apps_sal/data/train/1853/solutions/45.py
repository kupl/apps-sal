from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        city_dist_threshold = [float('inf')] * n
        dist_matrix = []

        for index in range(n):
            dist_matrix.append([float('inf')] * n)
        for i in range(n):
            dist_matrix[i][i] = 0

        for i, j, weight in edges:
            dist_matrix[i][j] = weight
            dist_matrix[j][i] = weight

        for k_index in range(n):
            for i_index in range(n):
                for j_index in range(n):
                    dist_matrix[i_index][j_index] = min(dist_matrix[i_index][j_index], dist_matrix[i_index][k_index] + dist_matrix[k_index][j_index])

        for i_index in range(n):
            for j_index in range(n):
                if dist_matrix[i_index][j_index] <= distanceThreshold:
                    if city_dist_threshold[i_index] == float('inf'):
                        city_dist_threshold[i_index] = 0
                    city_dist_threshold[i_index] += 1

        min_cities, city = min(city_dist_threshold), None
        for index in range(len(city_dist_threshold)):
            if city_dist_threshold[index] == min_cities:
                city = index

        return city
