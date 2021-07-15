n = int(input())
s = list()
for i in range(0, n):
    st = input()
    s.append(st)

for i in range(0, len(s)):
    st = s[i]
    while 'u' in st:
        st = st.replace("u", "oo")
    while "kh" in st:
        st = st.replace("kh", "h")
    s[i] = st

wds = set(s)
print(len(wds))

