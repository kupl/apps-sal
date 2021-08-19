# cook your dish here
# For each test case, output a single line containing N tokens (space-separated):     if the ith word of the dictionary exists in at least one phrase in modern     languages, then you should output YES as the ith token, otherwise NO.
# Constraints
# 1 ≤ T ≤ 20
# 1 ≤ N ≤ 100
# 1 ≤ K, L ≤ 50
# 1 ≤ length of any string in the input ≤ 5
# Example
# Input:
# 2
# 3 2
# piygu ezyfo rzotm
# 1 piygu
# 6 tefwz tefwz piygu ezyfo tefwz piygu
# 4 1
# kssdy tjzhy ljzym kegqz
# 4 kegqz kegqz kegqz vxvyj

# Output:
# YES YES NO
# O NO NO YES


test = int(input())

for _ in range(0, test):
    words, phrases = map(int, input().split())
    listOfPhrases = set()
    words = list(input().split())
    for _ in range(0, phrases):
        newset = set(input().split())
        listOfPhrases = listOfPhrases.union(newset)
    for x in words:
        if x in listOfPhrases:
            print('YES', end=' ')
        else:
            print('NO', end=' ')
    print()
