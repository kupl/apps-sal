m = int(input())
st = list()
for i in range (0, m):
	s = input()
	st.append(s)

for i in range (0, len(st)):
	s=st[i]
	while 'u' in s:
		s = s.replace("u","oo")
	while "kh" in s:
		s = s.replace("kh","h")
	st[i] = s
		
wds = set(st)

print (len(wds))
