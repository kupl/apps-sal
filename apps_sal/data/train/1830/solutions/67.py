class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        queue = []
        lakes = dict()
        days = []
        for i in range(len(rains)):
            if rains[i] == 0:
                queue.append(i)
            elif rains[i] in lakes:
                if not queue:
                    return []
                for queue_index in range(len(queue)):
                    if queue[queue_index] < lakes[rains[i]]:
                        if queue_index == len(queue) - 1:
                            return []
                        continue
                    else:
                        days[queue.pop(queue_index)] = rains[i]
                        break
                lakes[rains[i]] = i
            else:
                lakes[rains[i]] = i
            days.append(-1 if rains[i] != 0 else 999)
        return days
