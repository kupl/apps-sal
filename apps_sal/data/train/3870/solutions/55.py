def solve(s):
    L = [i for i, letter in enumerate (s) if letter == " "]
    print (L)
    l_s = list(''.join(s.split()))
    reversed = l_s[::-1]
    for number in L:
        reversed.insert(number, " ")
    return ''.join(reversed)
