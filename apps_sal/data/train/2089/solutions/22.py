import sys
n = int(sys.stdin.readline())
zero_model, one_model = 0, (1<<10)-1
commands = []
for i in range(n):
	c, k = sys.stdin.readline()[:-1].split()
	k = int(k)
	commands.append((c,k))

def process(n,commands):
	for comm in commands:
		c, k = comm
		if c=='|':
			n |= k
		elif c=='^':
			n ^= k
		elif c=='&':
			n &= k
	return n

zero_model = process(0,commands)
one_model = process((1<<10)-1,commands)

set_zero = (1<<10)-1
flip = 0
set_one = 0
for i in range(10):
	bz = zero_model&(1<<i)
	bo = one_model&(1<<i)
	if bz >= 1 and bo==0:
		flip |= 1<<i
	elif bz >= 1 and bo >= 1:
		set_one |= 1<<i
	elif bz==0 and bo==0:
		set_zero &= ~(1<<i)
ans = [("&",set_zero),("^",flip),("|",set_one)]

print(len(ans))
for comm in ans:
	print(*comm)

# for i in range(1<<10):
# 	if process(i,commands) != process(i,ans):
# 		print(bin(process(i,commands)),"vs",bin(process(i,ans)))

