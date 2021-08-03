class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        # median = 0

        # if len(arr)%2 == 0:
        #     median = arr[int((len(arr)-1)/2)]
        # else:
        median = arr[int((len(arr) - 1) / 2)]
        strong = {}
        # print(median)

        for x in arr:
            val = abs(x - median)
            if val not in list(strong.keys()):
                strong[abs(x - median)] = [x]
            else:
                strong[abs(x - median)].append(x)

        strong = sorted(list(strong.items()), reverse=True)
        # print(strong)
        strongest = []
        for x in strong:
            # if len(strongest) == k:
            #     break
            # else:
            # print(x)
            for val in sorted(x[1], reverse=True):
                if len(strongest) == k:
                    break
                # print(val)
                strongest.append(val)
                # if len(strongest) == k:
                #     break

        return strongest
