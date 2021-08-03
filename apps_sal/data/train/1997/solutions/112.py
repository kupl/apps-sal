class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        leftsorted = sorted(intervals, key=lambda x: (x[0], x[1]))
        i = 0
        while i < len(leftsorted) - 1:
            if leftsorted[i][0] == leftsorted[i + 1][0]:
                intervals.remove(leftsorted[i])

            i += 1

        rightsorted = sorted(intervals, key=lambda x: (x[1], x[0]))
        i = 0
        while i < len(rightsorted) - 1:
            if rightsorted[i][1] == rightsorted[i + 1][1]:
                intervals.remove(rightsorted[i + 1])

            i += 1

        leftsorted = sorted(intervals, key=lambda x: (x[0], x[1]))
        rightsorted = sorted(intervals, key=lambda x: (x[1], x[0]))

        lremain = len(leftsorted)
        i, j = 0, 0

        removed = []
        while i < lremain and j < lremain:
            # if leftsorted[i] in removed:
            if leftsorted[i] not in intervals:
                i += 1
            elif leftsorted[i] != rightsorted[j]:
                intervals.remove(rightsorted[j])
                # removed.append(rightsorted[j])
                j += 1
            else:
                i += 1
                j += 1
                # while leftsorted[i] not in intervals:
                #     i += 1
                #     if i == lremain:
                #         break


#         removed = []
#         for i in range(len(leftsorted)):
#             if leftsorted[i] not in intervals:
#                 continue
#             if leftsorted[i] != rightsorted[i]:
#                 intervals.remove(rightsorted[i])
        print(intervals)
        return len(intervals)
