def count_inversion(sequence):
    def rec(arr):
        if len(arr) <= 1: return arr, 0
        a, ai = rec(arr[:len(arr)//2])
        b, bi = rec(arr[len(arr)//2:])
        res, i, j, count = [], 0, 0, ai + bi
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
                count += len(a) - i
        return res + a[i:] + b[j:], count
    return rec(list(sequence))[1]
