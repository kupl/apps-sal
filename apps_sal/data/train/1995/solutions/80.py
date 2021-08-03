class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        p_list = list()
        for p, s, e in trips:
            if len(p_list) < e:
                p_list += [0] * (e - len(p_list))
            for i in range(s, e):
                p_list[i] += p
                if p_list[i] > capacity:
                    return False

        return True
