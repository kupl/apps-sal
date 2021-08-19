import heapq
from copy import deepcopy
from typing import List


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        person_bits = self.calculatePersonBits(req_skills, people)
        n = len(req_skills)
        dp = {0: set()}
        q = []
        heapq.heappush(q, 0)
        while len(q) > 0:
            index = heapq.heappop(q)
            for i in range(len(people)):
                if i not in dp[index]:
                    new_index = index | person_bits[i]
                    if new_index not in dp:
                        heapq.heappush(q, new_index)
                        dp[new_index] = deepcopy(dp[index])
                        dp[new_index].add(i)
                    elif len(dp[new_index]) > 1 + len(dp[index]):
                        dp[new_index] = deepcopy(dp[index])
                        dp[new_index].add(i)
        return list(dp[2 ** n - 1])

    def calculatePersonBits(self, req_skills, people):
        skills = {}
        i = 0
        for skill in req_skills:
            skills[skill] = 2 ** i
            i += 1
        result = []
        for person in people:
            total = 0
            for skill in person:
                total |= skills[skill]
            result.append(total)
        return result
