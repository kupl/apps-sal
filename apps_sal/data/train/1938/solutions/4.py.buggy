class Solution:
    # line-sweep , so hard
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        print(xs)
        print(x_i)
        count = [0] * len(x_i)
        L = []
        # review, kind of like sweep-line issue
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        # print(L)
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            # print(\"zip\")
            # print(count)
            # for x1, x2, c in zip(xs, xs[1:], count):
            # print(x1,x2,c)
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)

    # heap
    # similiar: skyline-problem-218
    def rectangleArea(self, recs):
        \"\"\"
        :type rectangles: List[List[int]]
        :rtype: int
        \"\"\"
        x = set()
        pq = []
        for rec in recs:
            x.add(rec[0])
            x.add(rec[2])
            heapq.heappush(pq, (rec[1], rec[0], rec[2], 1))
            heapq.heappush(pq, (rec[3], rec[0], rec[2], -1))

        x = sorted(list(x))
        xi = {v: i for i, v in enumerate(x)}
        count = [0] * len(x)

        res = 0
        last_l =  pq[0][0]

        while pq:
            cur_l = pq[0][0]

            for i in range(len(x)):
                if count[i] > 0:
                    res += (x[i + 1] - x[i]) * (cur_l - last_l)
                    res = res % (10 ** 9 + 7)

            while pq and pq[0][0] == cur_l:
                cur_l, x1, x2, bound = heapq.heappop(pq)
                for i in range(xi[x1], xi[x2]):
                    count[i] += bound

            last_l = cur_l
        return res


