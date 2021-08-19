# cook your dish here
for i in range(int(input())):
    l = list(input().split())
    tot = ""
    if(len(l) == 1):
        for j in l:
            print(j.capitalize())
    elif len(l) == 2:
        j = l[0]
        tot += j[0].capitalize() + ". "
        tot += l[1].capitalize()
    elif len(l) == 3:
        j = l[0]
        k = l[1]
        tot += j[0].capitalize() + ". "
        tot += k[0].capitalize() + ". "
        tot += l[2].capitalize()
    print(tot)
