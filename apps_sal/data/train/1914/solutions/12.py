class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        hashmap = collections.defaultdict(int)

        for item in costs:
            hashmap[tuple(item)] = abs(item[0] - item[1])

        print(hashmap)

        ll = sorted(hashmap, key=lambda x: -hashmap[x])

        print(ll)

        n = len(ll) // 2
        mincostA = []
        mincostB = []

        for i in range(2 * n):
            if len(mincostA) < n and len(mincostB) < n:
                if ll[i][0] < ll[i][1]:
                    mincostA.append(ll[i][0])
                else:
                    mincostB.append(ll[i][1])

            elif len(mincostA) < n:
                mincostA.append(ll[i][0])

            elif len(mincostB) < n:
                mincostB.append(ll[i][1])

        mincost = 0
        final = mincostA + mincostB
        for i in range(2 * n):
            mincost += final[i]

        return mincost
