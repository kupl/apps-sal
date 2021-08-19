class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def hamin(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        # dist_list = []
        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         dist_list.append([hamin(points[i], points[j]), i, j])
        # dist_list = sorted(dist_list, key=lambda x:(x[0]))
        # group_set_list = [set()]
        # answer = 0
        # for dis, x, y in dist_list:
        #     if x not in group_set_list[0] or y not in group_set_list[0]:
        #         answer += dis
        #         group_set_list.append(set([x, y]))
        #     new_group_set_list = [group_set_list[0]]
        #     for i in range(1, len(group_set_list)):
        #         if new_group_set_list[0] & group_set_list[i]:
        #             new_group_set_list[0] |= group_set_list[i]
        #         else:
        #             new_group_set_list.append(group_set_list[i])
        #     group_set_list = new_group_set_list
        #     if len(group_set_list[0]) == len(points):
        #         break
        # return answer
        dist_list = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist_list.append([hamin(points[i], points[j]), i, j])
        dist_list = sorted(dist_list, key=lambda x: (x[0]))
        # print(dist_list)
        group_set = set()
        group_set.add(0)
        answer = 0
        while(True):
            i = 0
            while(i < len(dist_list)):
                [dis, x, y] = dist_list[i]
                if x in group_set and y in group_set:
                    dist_list.pop(i)
                    continue
                if x in group_set:
                    group_set.add(y)
                    answer += dis
                    break
                if y in group_set:
                    group_set.add(x)
                    answer += dis
                    break
                i += 1
            if len(group_set) == len(points):
                break
        return answer
