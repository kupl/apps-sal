class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count_pass = trips[len(trips)-1][2]*[0]
        for i in trips:
            if len(count_pass)< i[2]:
                count_pass += [0]*(i[2]-len(count_pass))
            for j in range(i[1],i[2]):
                count_pass[j] += i[0] 
                if count_pass[j]> capacity:
                    return False
        return True

