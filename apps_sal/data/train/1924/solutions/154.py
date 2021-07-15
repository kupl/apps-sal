class Solution:
    def invalidTransactions(self, arr: List[str]) -> List[str]:
        b = [0]*len(arr)
        a = [0]*len(arr)
        c = []
        for i in range(len(arr)):
            b[i] = arr[i].split(\",\")
            if int(b[i][2]) > 1000:
                a[i] = 1
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if b[i][0] == b[j][0] and b[i][3] != b[j][3]:
                    if abs(int(b[i][1]) - int(b[j][1])) <= 60:
                        a[i] = a[j] = 1
        for i in range(len(arr)):
            if a[i] == 1:
                c.append(arr[i])
        return(c)
        
