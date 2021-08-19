class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        unique_tables = []
        unique_dishes = []
        ans = [['Table']]
        for i in orders:
            if int(i[1]) not in unique_tables:
                unique_tables.append(int(i[1]))
            if i[2] not in unique_dishes:
                unique_dishes.append(i[2])
        unique_tables.sort()
        unique_dishes.sort()
        ans[0].extend(unique_dishes)
        for i in range(len(unique_tables)):
            listt = [unique_tables[i]]
            listt.extend([0] * len(unique_dishes))
            ans.append(listt)
        for i in orders:
            ans[unique_tables.index(int(i[1])) + 1][unique_dishes.index(i[2]) + 1] += 1
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                ans[i][j] = str(ans[i][j])
        return ans
