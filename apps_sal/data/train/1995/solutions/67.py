class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        last_dest = max([x[2] for x in trips])
        curr_pos = 0

        cap_ls = [0] * last_dest
        for i in range(len(trips)):
            for j in range(trips[i][1], trips[i][2]):
                cap_ls[j] += trips[i][0]

        return max(cap_ls) <= capacity
