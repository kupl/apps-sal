# 1488. Avoid Flood in The City

import heapq

'Your country has an infinite number of lakes.'
'Initially, all lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water.'
'If it rains over a full lake, there will be a flood.'
'Your goal is to avoid flood.'
'On each dry day you may choose to dry one lake.'


def drying_strategy(rains):
    # Idea: greedy method
    # Always dry the lake which is most urgent.
    # Never dry already-dry lakes, unless no lakes are full.

    # Alternate method: orthogonal.
    # Consider each lake and how many times you should dry it.
    # Ignore any lake that is only filled once.

    # Maintain a heap of (lake, urgency) for filled lakes.
    # Whenever a lake is filled, its urgency is pushed into the heap.
    # Whenever we can dry a lake, we take the most urgent task on the top of the heap.

    last_rain = {}  # updating
    chain_rain = {}  # persistent, link from one rain to next

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
                # flooded
                return []
            else:
                filled.add(rain)
                if time in chain_rain:  # has next rain
                    heapq.heappush(urgency, chain_rain[time])
                    # add next rain
            solution.append(-1)  # wait
        else:
            # clear day. find the next urgent and dry.
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
                        pass  # nothing to worry about
                    else:
                        solution.append(rain)
                        filled.remove(rain)
                        solved = True

    return solution


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        return drying_strategy(rains)
