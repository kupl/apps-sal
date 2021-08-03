class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n = len(folder)
        folder = sorted(folder)
        first = folder[0]
        ans = set()
        # print((first.split('/')))
        ans.add(folder[0])
        for i in range(1, n):
            flag = True
            second = folder[i]
            # print(first,second)
            first1 = first.split('/')
            second1 = second.split('/')
            for j in range(len(first1)):
                if first1[j] != second1[j]:
                    ans.add(second)
                    first = second
                    flag = False
                    break

            # if flag:
            #     ans.add(first)

#         if not flag:
#             ans.add(folder[n-1])

        return list(ans)
