def big_primefac_div(n):
    n = abs(n)
    maxi = 0
    if n % 1 == 0:
        listy = [num for num in range(2, int(n ** 0.5 + 1)) if n % num == 0]
        fancy_list = list(listy)
        for number in listy:
            temp_numb = n // number
            fancy_list.append(int(temp_numb))
        for numb in sorted(fancy_list, reverse=True):
            for i in range(2, int(numb ** 0.5 + 1)):
                if numb % i == 0:
                    break
            else:
                maxi = numb
                break
        if fancy_list:
            return [maxi, max(set(fancy_list))]
        else:
            return []
    else:
        return 'The number has a decimal part. No Results'
