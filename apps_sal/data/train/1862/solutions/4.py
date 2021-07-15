class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def pancake_flip(to_flip, index):
            print(\"flipping \" + str(to_flip) + \" with index \" + str(index))
            middle = index // 2
            for i in range(middle):
                to_flip[i], to_flip[index - i - 1] = to_flip[index - i - 1], to_flip[i]
            print(\"flipped: \" + str(to_flip))
            return to_flip
        
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return []
        
        result = []
        print(\"starting with: \" + str(arr))
        current_element = 1
        while current_element < len(arr):
            print(\"current element: \" + str(current_element))
            index = arr.index(current_element) + 1
            print(\"found element \" + str(current_element) + \" at \" + str(index))
            if index != len(arr) - current_element + 1:
                if index != 1:
                    result.append(index)
                    arr = pancake_flip(arr, index)
                index = len(arr) - current_element + 1
                result.append(index)
                arr = pancake_flip(arr, index)
            current_element += 1
        result.append(len(arr))
        return result

