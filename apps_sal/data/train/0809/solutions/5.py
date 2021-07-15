def isPossibleTriangle (arr , N , tri , alltri):  
	arr.sort(reverse = True) 
	flag = 0
	for i in range(N - 2):  
		if arr[i] + arr[i + 1] > arr[i + 2] and arr[i] + arr[i + 2] > arr[i + 1] and arr[i + 1] + arr[i + 2] > arr[i]:
			flag = 1
			tri.append(arr[i])
			tri.append(arr[i + 1])
			tri.append(arr[i + 2])
			alltri.append(tri)
			break

	if flag == 0:
		return ("NO")
	else:
		return ("YES")

N = int(input())
arr = list(map(int , input().split()))
tri = []
alltri = []
if isPossibleTriangle(arr , N , tri , alltri) == "YES":
	alltri.sort()
	print("YES")
	print(*alltri[0])
else:
	print("NO")
