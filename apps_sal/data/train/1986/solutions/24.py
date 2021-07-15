class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return self.generateGrayArrWithCondition(n, start)
    
    def generateGrayArrWithCondition(self, n, start):
        arr = []

        arr.append(\"0\") 
        arr.append(\"1\") 

        i = 2
        j = 0
        while(True): 
            if i >= 1 << n: 
                break

            for j in range(i - 1, -1, -1): 
                arr.append(arr[j]) 

            for j in range(i): 
                arr[j] = \"0\" + arr[j] 

            for j in range(i, 2 * i): 
                arr[j] = \"1\" + arr[j] 
            i = i << 1

        for index, element in enumerate(arr):
            arr[index] = int(element, 2)
            if arr[index] == start:
                break_at = index
            
        return arr[break_at:] + arr[:break_at]
