# ##plot a line of y = ax + b and then count number of triangles formed by lines of same colour
# ##then remove max possible lines (while not k <= 0) K - Vi
# ##print min possible triangles after (max lines are removed, but not necessarily)
# #>>>first, use y = ax + b to find line by taking x = 0 and y = 0 in two turns
# #>>>then count all triangles with all three sides of same colour
# #>>>remove as many lines as required, such that triangles formed are minimum
# # __CONSTRAINTS__
# # 1≤T≤10
# # 1≤C≤N≤3,000
# # 0≤K≤3,000
# # 0≤ai,bi≤109 for each valid i
# # 1≤ci≤C for each valid i
# # 0≤Vi≤K for each valid i
# # no two lines coincide, regardless of their colours
# # no three lines are concurrent
# # __SUBTASKS__
# # Subtask #1 (10 points):
# # # N≤10
# # # K≤100
# # Subtask #2 (15 points):
# # # V1=V2=…=VC
# # # no two lines are parallel
# # Subtask #3 (25 points):
# # # no two lines are parallel
# # Subtask #4 (50 points):
# # #original constraints
# ###>>> clearly, brute force cannot be used....ANTS
# ###APPROACH:
# #>>> count the number of triangles for each different colour (using formula)
# #>>> get sum of all triangles formed
# #>>> remove lines to get minimum triangles!!!....how?
# #>>> to get formula: try cummulative frequency of points of intersection and triangles...or nC3
# #>>> consider all lines to be non-parallel and non-coincident of course....aim is subtask 2
# # 1 --> 0, 0
# # 2 --> 0 + 0 = 0, 1
# # 3 --> 0 + 1 = 1, 3
# # 4 --> 1 + 3 = 4, 6
# # 5 --> 4 + 6 = 10, 10
# # 6 --> 10 + 10 = 20, 15 ...
# def f(n):
#     factorial = 1
#     for i in range(1,n + 1):
#         factorial = factorial*i
#     return factorial
# for _ in range(int(input())):
# 	n,C,k = map(int , input().split())
# 	for _ in range(n):
# 		a,b,c = map(int , input().split())
# 		freq = {}
# 		if(c in freq): freq[c] += 1;
# 		else: freq[c] = 1;
# 	V = list(map(int , input().split()))
# 	triangles,trianglelist,turns = 0,[],0
# 	for i in range(1,C + 1):
# 		trianglelist.append(f(i)//(f(i - 3)*6))
# 	# while(k >= 0 and k > min(V)):
# 	# 	i = max(freq, key = freq.get)
# 	# 	triangles += f(i - 1)//(f(i - 4)*6) - f(i)//(f(i - 3)*6)
# 	# 	k -= V[i] #min(V)
# 	while(k >= 0 and k > min(V)):
# 		i = max(freq, key = freq.get)
# 		freq[i] -= 1
# 		k -= V[i - 1]
# 		turns += 1
# 	trianglelist.remove(max(trianglelist))
# 	triangles = sum(trianglelist) + f(i - turns - 1)//(f(i - turns - 4)*6) + f(i)//(f(i - 3)*6)
# 	print(triangles) #TLE avoided, but WA
# import math
# from collections import defaultdict
# T=int(input())
# for i in range(T):
#     N,C,K=map(int,input().split())
#     D=defaultdict(int)
#     ans='Hello'
#     for j in range(N):
#         a,b,c=map(int,input().split())
#         D[c]+=1

#     v=list(map(int,input().split()))
#     q=0
#     num=K//v[0]
#     d=0
#     while(num>0):
#         P=list(D.keys())[list(D.values()).index(max(D.values()))]
#         D[P]-=1
#         num-=1
#     temp=0
#     for i,j in D.items():
#         if(j>=3):
#             temp+=(math.factorial(j)/(math.factorial(3)*math.factorial(j-3)))
#     print(int(temp)) #i was so close to the correct answer
# ^^^^^^^^^^^^^^^^noob answer, lines wasted. but AC [15 pts]
for _ in range(int(eval(input()))):
    N, C, K = list(map(int, input().split()))
    poss, lines, res = [0] * (K + 1), {}, 0
    for _ in range(N):
        a, b, c = list(map(int, input().split()))
        if c - 1 not in lines:
            lines[c - 1] = {a: 1}
        else:
            lines[c - 1][a] = lines[c - 1].get(a, 0) + 1
    era = list(map(int, input().split()))
    for c in range(C):
        if era[c] == 0:
            lines.pop(c, None)
    for c, mp in list(lines.items()):
        vals = list(mp.values())
        if len(vals) >= 3:
            vals.sort()
            s1, s2, s3 = sum(vals), sum(a**2 for a in vals), sum(a**3 for a in vals)
            full = (s1**3 - 3 * s1 * s2 + 2 * s3) // 6
            res += full
            gain = {0: 0}
            idx = 0
            for j in range(era[c], K + 1, era[c]):
                vals[idx] -= 1
                old = vals[idx] + 1
                nw = vals[idx]
                if vals[idx] == 0:
                    idx += 1
                    if idx == len(vals):
                        break
                s1 -= 1
                s2 += nw**2 - old**2
                s3 += nw**3 - old**3
                gain[j] = full - (s1**3 - 3 * s1 * s2 + 2 * s3) // 6
            prev = poss
            poss = [max(prev[i - j] + gain[j] for j in list(gain.keys()) if j <= i) for i in range(K + 1)]
    print(res - max(poss))
