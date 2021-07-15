#D    高橋君と見えざる手 / An Invisible Hand
N,T = [int(i) for i in input().split(" ")]
A=[int(i) for i in input().split(" ")]
Max = 0
count = 1
Min = A[0]
for i in range(N):
    if A[i] <= Min :
        Min = A[i]
    else :
        temp = A[i]-Min
        if temp > Max:
            Max = temp 
            count = 1
        elif temp == Max :
            count += 1
print(count)
