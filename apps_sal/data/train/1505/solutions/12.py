n = int(input())

a = [int(i) for i in input().split()]

md = 0
mr = 0
st1 = []
st2 = []
dno = 0
rno = 0

for i in range(1, n + 1):
    if a[i - 1] == 1:
        st1.append(i)
        st2.append(i)
    elif a[i - 1] == 2:
        if len(st1) > md:
            md = len(st1)
            dno = st1[-1]

        if len(st1) == 1:
            if len(st2) + 1 > mr:
                mr = len(st2) + 1
                rno = st2[0]
            st2 = []
        else:
            st2.append(i)
        st1.pop()
print(md, dno, mr, rno)
