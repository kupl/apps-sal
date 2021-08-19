class Solution:

    def findLucky(self, arr: List[int]) -> int:
        adict = {}
        i = 0
        j = len(arr)
        while i < j:
            if arr[i] in adict:
                print(arr[i], adict.get(arr[i]))
                adict[arr[i]] += 1
                print(arr[i], adict.get(arr[i]))
            else:
                adict[arr[i]] = 1
            i += 1
            output = -1
        for key in adict:
            if adict.get(key) == key:
                if adict.get(key) > output:
                    output = adict.get(key)
        return output
