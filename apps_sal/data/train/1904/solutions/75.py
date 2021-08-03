class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        point_distance = dict()
        distance_list = []

        for x, y in points:
            distance = -sqrt(x**2 + y**2)
            if len(distance_list) < K:
                heappush(distance_list, distance)
                if distance in list(point_distance.keys()):
                    point_distance[distance].append([x, y])
                else:
                    point_distance[distance] = [[x, y]]
            else:
                if distance_list[0] < distance:
                    to_remove = distance_list[0]
                    if len(point_distance[to_remove]) == 1:
                        del point_distance[to_remove]
                    else:
                        point_distance[to_remove].pop()
                    heappop(distance_list)
                    heappush(distance_list, distance)
                    if distance in list(point_distance.keys()):
                        point_distance[distance].append([x, y])
                    else:
                        point_distance[distance] = [[x, y]]

        result = []
        while K > 0:
            tmp = point_distance[heappop(distance_list)]
            K -= len(tmp)
            result = result + tmp

        return result
