class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cumArr = []
        resultArr = []
        for index in range(len(arr)):
            if index == 0:
                cumArr.insert(index, arr[index])
            else:
                cumArr.insert(index, arr[index] ^ cumArr[index - 1])
        for query in queries:
            left = query[0]
            right = query[1]
            if left is not 0:
                resultArr.append(cumArr[right] ^ cumArr[left - 1])
            else:
                resultArr.append(cumArr[right])
        return resultArr
