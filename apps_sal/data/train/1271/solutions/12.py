def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


a = int(input())
while a != 0:
    b = int(input())
    mylist = list()
    (ev, od) = (0, 0)
    for i in range(b):
        c = int(input())
        fla = 0
        for j in range(len(mylist)):
            if c == mylist[j]:
                print(ev, od)
                fla = 1
                break
        if fla == 1:
            continue
        (ev, od) = (0, 0)
        for j in range(len(mylist)):
            if c != mylist[j]:
                mylist.append(c ^ mylist[j])
        mylist.append(c)
        mylist = list(set(mylist))
        for j in range(len(mylist)):
            p = countSetBits(mylist[j])
            if p % 2 == 0:
                ev += 1
            else:
                od += 1
        print(ev, od)
    a -= 1
