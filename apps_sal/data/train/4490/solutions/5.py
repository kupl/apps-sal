def max_collatz_length(n):
    if type(n) != int:
        return []
    if n == 0:
        return []
    if n == 1:
        return [1, 1]
    try:
        results = [0 for i in range(n + 1)]
        results[0] = 1
        results[1] = 1

        for num in range(2, n + 1):
            col = num
            ctr = 0
            shortCut = 0

            while(shortCut == 0):

                if col % 2 == 0:
                    ctr += 1
                    col = col >> 1
                else:
                    ctr += 2
                    col = (3 * col + 1) >> 1
                if col < n:
                    shortCut = results[col]
            results[num] = results[col] + ctr

        return [results.index(max(results[1:])), max(results[1:])]
    except:
        return []
