class Solution:

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = collections.defaultdict(list)
        tickets.sort(key=operator.itemgetter(1))
        for (src, dst) in tickets:
            d[src].append([dst, False])
        ans = []

        def DFS(src):
            ans.append(src)
            if len(ans) == len(tickets) + 1:
                return True
            for (i, a) in enumerate(d[src]):
                if not a[1]:
                    d[src][i][1] = True
                    if DFS(a[0]):
                        return True
                    d[src][i][1] = False
            ans.pop()
            return False
        DFS('JFK')
        return ans
