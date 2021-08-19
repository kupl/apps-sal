# cook your dish here
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
