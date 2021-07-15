# cook your dish here
try:
    for _ in range(int(input())):
        string = input()
        string = string.lower()
        stringd = ""
        t = 0
        for i in range(len(string)):
            t = 0
            if i == 0 or string[i-1] == " ":
                stringd = stringd + string[i].capitalize()
                t+=1
                a = i+1
            if " " in string[i:] and t == 1:
                stringd = stringd+"."+" "
        for i in string[a:]:
            stringd = stringd + i
        print(stringd)
except:
    pass
