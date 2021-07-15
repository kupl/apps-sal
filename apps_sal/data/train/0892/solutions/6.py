# cook your dish here
#2

for t in range(int(input())):
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if k > n:
        print(1)
        continue
    #even 
    curr = -1
    i = 0
    temp_even_place = -1
    ans_of_even = 0
    while curr + k < n: #need to find a stop 
        while i-curr <= k:
            if A[i]%2 == 0:
                temp_even_place = i
            i+=1
        if temp_even_place == curr: #no new stop found
            ans_of_even = -1
            break
        else:
            ans_of_even += 1
            curr = temp_even_place
    if ans_of_even != -1:
        ans_of_even += 1

    #odd 
    curr = -1
    i = 0
    temp_odd_place = -1
    ans_of_odd = 0
    while curr + k < n: #need to find a stop 
        while i-curr <= k:
            if A[i]%2 == 1:
                temp_odd_place = i
            i+=1
        if temp_odd_place == curr: #no new stop found
            ans_of_odd = -1
            break
        else:
            ans_of_odd += 1
            curr = temp_odd_place
    if ans_of_odd != -1:
        ans_of_odd += 1

    if ans_of_even == -1 and ans_of_odd == -1:
        print(-1)
    elif ans_of_odd == -1 and ans_of_even != -1:
        print(ans_of_even)
    elif ans_of_odd != -1 and ans_of_even == -1:
        print(ans_of_odd)
    elif ans_of_odd != -1 and ans_of_even != -1:
        print(min(ans_of_even,ans_of_odd) )
    
    

