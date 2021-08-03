class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) <= 0:
            return False

        trips.sort(key=lambda x: x[1])  # Sorting array by start time
        stack = []  # maintaing list to store indexes so that we can compare start time of previous and with current end time
        if trips[0][0] > capacity:
            return False
        else:
            stack.append(0)
            capacity -= trips[0][0]

        for i in range(1, len(trips)):
            n = 0
            # if current start time >= any one of previous indices start time--> inc capacity
            while stack and n < len(stack):
                if trips[i][1] >= trips[stack[n]][2]:
                    capacity += trips[stack[n]][0]
                    stack.pop(n)
                else:
                    n += 1

            if trips[i][0] <= capacity:
                capacity -= trips[i][0]
            elif trips[i][0] > capacity:
                return False
            stack.append(i)
        return True
