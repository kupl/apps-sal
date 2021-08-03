class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        arr = []
        for x in transactions:
            n, a, t, p = x.split(',')
            arr.append([n, a, t, p])

        inv = []
        for i in range(len(arr)):
            n, t, a, p = arr[i]
            added = False
            if int(a) > 1000:
                inv.append(arr[i])
                added = True
            for j in range(i + 1, len(arr)):

                nn, tt, aa, pp = arr[j]

                if abs(int(t) - int(tt)) <= 60 and n == nn and p != pp:
                    if not added:
                        inv.append(arr[i])
                        added = True
                    inv.append(arr[j])

        inv = [','.join(x) for x in inv]
        inv = list(set(inv))
        return (inv)
