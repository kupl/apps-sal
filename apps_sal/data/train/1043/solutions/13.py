# cook your dish here
T = int(input())

for t in range(T):
    phrases = []
    numword, numphrases = input().split()
    words = input().split()
    for phrase in range(int(numphrases)):
        phrase = input().split()
        phrase = phrase[1:]
        for word in phrase:
            phrases.append(word)
    for count in range(len(words)):
        if words[count] in phrases:
            print("YES", end=" ")
        else:
            print("NO", end=" ")
    print("\n", end="")
