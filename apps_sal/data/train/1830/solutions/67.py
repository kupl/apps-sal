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

        # 1,0 ,1, 0,1
        # [1,2,0,0,2,1]
        # (1: 2, 2: 2, 0:2)

        # [1,2,0,1,2]
        # (1: 2, 2: 2, 0:1) (4 - 2) > 1

        # O(n) space
        # keep queue of indexes which represents days where there is no rain
        # keep a set of values of n that have been rained on
        # for each entry in the array (O(n))
        #       If value is zero:
        #           add current index to end of queue
        #       elif: Whenever we encounter value that is in the set and nonzero-
        #           if queue is empty, return empty array
        #           pop from the queue and emplace encountered value in output array at popped index (O(1))
        #       else:
        #           add encountered value to set
        #       add -1 to output array if value is not 0, else 999
        #

    # rains = [1, 0 ,1, 0]
    # rains = [1, 1, 0]
    # rains = [1, 0, 1, 0, 1]
    # rains = [0, 1, 0, 1, 0, 1]
    # rains = [0 , 0, 0... , 1, 0, 1]
    # rains = [1, 0, 2, 0 , 2, 1]
