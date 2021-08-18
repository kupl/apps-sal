class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.hasmap = {}
        for ticket in tickets:
            self.hasmap.setdefault(ticket[0], []).append(ticket[1])
        self.route = ['JFK']
        return self.dfs('JFK', tickets)

    def dfs(self, start_airport, tickets):
        if len(self.route) == len(tickets) + 1:
            return self.route

        dests = self.hasmap.get(start_airport)
        if dests is not None:
            for dest in sorted(dests):
                self.hasmap[start_airport].remove(dest)
                self.route.append(dest)
                work = self.dfs(dest, tickets)
                if work:
                    return self.route
                self.route.pop()
                self.hasmap[start_airport].append(dest)
