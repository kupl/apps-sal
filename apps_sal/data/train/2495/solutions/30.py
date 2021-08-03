class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        differences_dict = {}
        for i in range(len(target)):
            differences_dict[target[i]] = differences_dict.get(target[i], 0) + 1

            differences_dict[arr[i]] = differences_dict.get(arr[i], 0) - 1

            if not differences_dict[target[i]]:
                differences_dict.pop(target[i])

            if arr[i] != target[i] and not differences_dict[arr[i]]:
                differences_dict.pop(arr[i])

        return False if differences_dict else True
