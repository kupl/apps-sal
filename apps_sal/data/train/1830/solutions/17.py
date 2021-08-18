
import heapq

'Your country has an infinite number of lakes.'
'Initially, all lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water.'
'If it rains over a full lake, there will be a flood.'
'Your goal is to avoid flood.'
'On each dry day you may choose to dry one lake.'


def drying_strategy(rains):

    last_rain = {}
    chain_rain = {}

    for time, rain in enumerate(rains):
        if rain > 0:
            if rain in last_rain:
                chain_rain[last_rain[rain]] = time
            last_rain[rain] = time

    del last_rain

    urgency = []
    filled = set()

    solution = []

    for time, rain in enumerate(rains):
        if rain > 0:
            if rain in filled:
                return []
            else:
                filled.add(rain)
                if time in chain_rain:
                    heapq.heappush(urgency, chain_rain[time])
            solution.append(-1)
        else:
            solved = False
            while not solved:
                if not urgency:
                    solution.append(1)
                    if 1 in filled:
                        filled.remove(1)
                    solved = True
                else:
                    time = heapq.heappop(urgency)
                    rain = rains[time]
                    if rain not in filled:
                        pass
                    else:
                        solution.append(rain)
                        filled.remove(rain)
                        solved = True

    return solution


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        return drying_strategy(rains)
