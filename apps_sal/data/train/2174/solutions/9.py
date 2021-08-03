n = int(input())
a = list(map(int, input().split()))

s1, s2 = set(), set()

for each in a:
    st = set()
    st.add(each)
    for i in s1:
        st.add(each | i)
    s1 = st
    s2.update(s1)

print(len(s2))
