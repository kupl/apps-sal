class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        START = 1
        END = 0
        MOD = 10**9 + 7
        xaxis = []

        for x1, y1, x2, y2 in rectangles:
            xaxis.append((x1, START, y1, y2))
            xaxis.append((x2, END, y1, y2))

        xaxis.sort()

        prev = 0
        area = 0
        yaxis = []
        for i in range(len(xaxis)):
            x, status, y1, y2 = xaxis[i]
            if i > 0:
                area += self.get_length(yaxis) * (x - prev)
                area %= MOD
            if status == START:
                yaxis.append((y1, y2))
                yaxis.sort()
            else:
                yaxis.remove((y1, y2))
            prev = x
        return area

    def get_length(self, yaxis):
        length = 0
        i = 0

        prev = (float('-inf'), float('-inf'))

        for i in range(len(yaxis)):
            if not self.has_overlap(prev, yaxis[i]):
                length += yaxis[i][1] - yaxis[i][0]
            else:
                if prev[1] >= yaxis[i][1]:
                    continue
                length += max(0, yaxis[i][1] - prev[1])
            prev = yaxis[i]
        return length

    def has_overlap(self, prev, cur):
        if prev[1] < cur[0] or cur[1] < prev[0]:
            return False
        return True
