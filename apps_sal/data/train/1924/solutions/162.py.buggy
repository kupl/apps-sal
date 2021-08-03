class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # brute force
        invalid = set()
        arr = [trans.split(',') for trans in transactions] 
        arr.sort(key = lambda t: int(t[1]))
        print(arr)
        for i in range(len(arr)):
            if int(arr[i][2]) > 1000: invalid.add(','.join(arr[i]))
            for j in range(i, len(transactions)):
                if arr[j][0] == arr[i][0] and int(arr[j][1]) - int(arr[i][1]) <= 60 and arr[i][3] != arr[j][3]:
                    print(\"together: \", ','.join(arr[j]), ','.join(arr[i]))
                    invalid.add(','.join(arr[j]))
                    invalid.add(','.join(arr[i]))
        
        return invalid
            
