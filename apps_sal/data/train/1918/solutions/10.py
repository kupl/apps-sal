class Solution(object):

    def __init__(self):
        self.res = []

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if tickets is None or len(tickets) == 0:
            return []

        dic = {}
        dic_city = {}
        for t in tickets:
            if (t[0], t[1]) not in dic:
                dic[(t[0], t[1])] = 0
            dic[(t[0], t[1])] += 1
            if t[0] not in dic_city:
                dic_city[t[0]] = []
            dic_city[t[0]].append(t[1])
        for k in dic_city.keys():
            dic_city[k] = set(dic_city[k])
            dic_city[k] = list(dic_city[k])
            dic_city[k].sort()
        self.res = []
        self.dfs("JFK", dic, dic_city, ["JFK"], len(tickets) + 1)
        return self.res

    def dfs(self, city, dic, dic_city, cur, tar):
        if len(cur) == tar:
            if not self.res:
                self.res = list(cur)

            return True
        if city in dic_city:
            citys = dic_city[city]
            for c in citys:
                if (city, c) in dic and dic[(city, c)] > 0:
                    dic[(city, c)] -= 1
                    cur.append(c)
                    if self.dfs(c, dic, dic_city, cur, tar):
                        return True
                    cur.pop()
                    dic[(city, c)] += 1
        return False
