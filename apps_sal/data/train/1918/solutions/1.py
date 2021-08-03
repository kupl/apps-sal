class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dict = collections.defaultdict(list)
        for flight in sorted(tickets)[::-1]:
            dict[flight[0]].append(flight[1])
        res = collections.deque()

        def visit(s):
            while dict[s]:
                visit(dict[s].pop())
            res.appendleft(s)
        visit("JFK")
        return list(res)
