class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def parition(st, end):

            lo, i, j = st, st, end
            while True:

                while i < end and arr[i][0] <= arr[lo][0]:
                    i += 1

                while j > st and arr[lo][0] <= arr[j][0]:
                    j -= 1

                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
            arr[lo], arr[j] = arr[j], arr[lo]
            return j

        def quick_select(st, end):

            if st > end:
                return

            par = parition(st, end)

            if par == K:
                return

            if par > K:
                quick_select(st, par - 1)
            else:
                quick_select(par + 1, end)
            return

        arr = []
        for pt in points:
            arr.append([math.sqrt(sum([x**2 for x in pt])), pt])
        random.shuffle(arr)
        quick_select(0, len(arr) - 1)

        return [x[1] for x in arr[:K]]
