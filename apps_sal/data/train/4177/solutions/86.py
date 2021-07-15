def men_from_boys(arr):
    unique = [arr[i] for i in range(len(arr)) if arr[i] not in set(arr[i+1:])]
    evenL = [n for n in unique if n % 2 == 0];evenL.sort()
    oddL = [n for n in unique if n not in evenL];oddL.sort();oddL.reverse()
    return evenL + oddL
