class Solution:

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for (a, b) in sorted(tickets, reverse=True):
            targets[a] += [b]
        (route, stack) = ([], ['JFK'])
        while stack:
            while targets[stack[-1]]:
                stack += [targets[stack[-1]].pop()]
            route += [stack.pop()]
        return route[::-1]
