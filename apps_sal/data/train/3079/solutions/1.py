
def big_primefac_div(n):
    #We need only absolute values
    n = abs(n)
    maxi = 0
    #Checking if the number has a decimal part
    if n % 1 == 0:
        #Loop for finding Biggest Divisor
        listy = [num for num in range(2, int(n**.5 + 1)) if n % num == 0]
        fancy_list = list(listy)
        for number in listy:
            temp_numb = n // number
            fancy_list.append(int(temp_numb))
        #Loop for finding Biggest Prime Factor
        for numb in sorted(fancy_list, reverse=True):            
            for i in range(2, int(numb**.5 + 1)):
                if numb % i == 0:
                    break
            else:
                maxi = numb
                break
        if fancy_list:
            return [maxi, max(set(fancy_list))]
        #In case we gonna have one number as prime factor itself
        else:
            return []
    else:
        return ("The number has a decimal part. No Results")
