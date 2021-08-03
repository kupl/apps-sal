class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(0, len(groupSizes)):
            if groupSizes[i] in groups:
                groups[groupSizes[i]].append(i)
            else:
                groups[groupSizes[i]] = [i]
        # print(groups)

        output = []
        for i in groups:
            list1 = []
            for j in groups[i]:
                list1.append(j)
                if(len(list1) == i):
                    output.append(list1)
                    list1 = []

        return output


def main():
    groupSizes = input().split()
    sol = Solution()
    output = sol.groupThePeople(groupSizes)
    print(output)


def __starting_point():
    main()


__starting_point()
