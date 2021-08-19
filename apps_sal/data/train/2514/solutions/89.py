class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        counter = 0
        if 1 <= len(arr1) <= 500 and 1 <= len(arr2) <= 500:
            for i in range(len(arr1)):
                val = 1
                for j in range(len(arr2)):
                    if pow(-10, 3) <= arr1[i] <= pow(10, 3) and pow(-10, 3) <= arr2[j] <= pow(10, 3):
                        if 0 <= d <= 100:
                            check_value = (abs(arr1[i] - arr2[j]))
                            if check_value <= d:
                                val = 0
                                break
                if val == 1:
                    counter += 1
            # print(counter)
            return counter
