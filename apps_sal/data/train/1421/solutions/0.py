def getsum(N):
	if N==1:
		return 9
	if N==2:
		return 99
	s = ""
	for i in range(0,N):
		s = s+'5'
	s = int(s)
	if N%2==0:
		s = s*pow(9,N//2-1)
	else:
		s = s*pow(9,N//2)
	return s%(pow(10,9)+7)

def main():
	t = int(input())
	for _ in range(0,t):
		N = int(input())
		result = getsum(N)
		print(result)
def __starting_point():
	main()

__starting_point()
