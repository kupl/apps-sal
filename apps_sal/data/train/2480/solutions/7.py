class Solution:

    def minCostToMoveChips(self, position: List[int]) -> int:
        record = {}
        for i in range(len(position)):
            if position[i] not in record:
                record[position[i]] = 1
            else:
                record[position[i]] += 1
        max_freq = 0
        odd_freq = 0
        even_freq = 0
        odd_max_freq = 0
        even_max_freq = 0
        odd_rec = 0
        even_rec = 0
        for i in record:
            if i % 2 != 0:
                odd_freq += record[i]
                if record[i] >= odd_max_freq:
                    odd_max_freq = record[i]
                    odd_rec = i
            else:
                even_freq += record[i]
                if record[i] >= even_max_freq:
                    even_max_freq = record[i]
                    even_rec = i
        if odd_freq > even_freq:
            rec = odd_rec
        else:
            rec = even_rec
        cost = 0
        for i in position:
            if (rec - i) % 2 == 0 or (i - rec) % 2 == 0:
                continue
            elif rec == i:
                continue
            else:
                cost += 1
        return cost
