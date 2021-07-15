for _ in range(int(input())):
    string=str(input())
    target="abc"
    while(target in string):
        start=string.find(target)
        string=string[:start]+string[start+3:]

    print(string)

