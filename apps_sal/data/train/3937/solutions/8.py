def max_sumDig(nMax, maxSum):
    count=0
    nums=[]
    if len(str(nMax)) == 4:
        for i in range(1000, nMax+1):
            if ( (i%10) + ( (i//10) % 10 ) + ( (i//100) % 10 ) + ( (i//1000) % 10 )) <= maxSum:
                nums.append(i)
                count+=1
    elif len(str(nMax)) == 5:
        for i in range(1000, nMax+1):
            if ( (i%10) + ( (i//10) % 10 ) + ( (i//100) % 10 ) + ( (i//1000) % 10 )) <= maxSum and (( (i//10) % 10 ) + ( (i//100) % 10 ) + ( (i//1000) % 10 ) + ( (i//10000) % 10 )) <= maxSum:
                nums.append(i)
                count+=1
    elif len(str(nMax)) == 6:
        for i in range(1000, nMax+1):
            if ( (i%10) + ( (i//10) % 10 ) + ( (i//100) % 10 ) + ( (i//1000) % 10 )) <= maxSum and (( (i//10) % 10 ) + ( (i//100) % 10 ) + ( (i//1000) % 10 ) + ( (i//10000) % 10 )) <= maxSum and (( (i//100) % 10 ) + ( (i//1000) % 10 ) + ( (i//10000) % 10 ) + ( (i//100000) % 10 )) <= maxSum:
                nums.append(i)
                count+=1
    media=sum(nums)/len(nums)
    for n in nums:
        if media <= n:
            if (n - media) > (media - nums[nums.index(n)-1]):
                media=nums[nums.index(n)-1]
                break
            else:
                media=n
                break
    suma=sum(nums)
    return [count, media, suma]
