import sys


inp = sys.stdin.read().splitlines()

n, k = list(map(int, inp[0].split()))

lst = list(map(int, inp[1].split()))

lst.sort()

total = sum(lst)

lower = int(total / n)

nupper = total % n


if nupper == 0:

    upper = lower

else:

    upper = lower + 1

nlower = n - nupper


i = 0

while i < n and lst[i] < lower:

    i += 1

low1st = i


i = n - 1

while i >= 0 and lst[i] > upper:

    i -= 1

uplast = i


lowerfill = low1st * lower - sum(lst[:low1st])


upperfill = sum(lst[uplast + 1:]) - (n - uplast - 1) * upper


totalsteps = (lowerfill + upperfill) / 2

'''

print("nlower = %d"%nlower)

print("nupper = %d"%nupper)

print("lower = %d"%lower)

print("upper = %d"%upper)

print("lowerfill = %d"%lowerfill)

print("upperfill = %d"%upperfill)

print("totalsteps = %f"%totalsteps)

'''


def filllower():

    kk = k

    cur = lst[0]

    i = 0

    while (kk > 0):

        while (lst[i] == cur):

            i += 1

            # print("i=%d,lst[i]=%d"%(i,lst[i]))

        diff = lst[i] - lst[i - 1]

        kk -= i * diff

        #print("lower kk = %d",kk)

        if kk == 0:

            cur = lst[i]

            break

        elif kk < 0:

            cur = lst[i] - int(-kk / i) - 1

            #print("-kk/i = %d",int(-kk/i))

            if (-kk % i) == 0:

                cur += 1

            break

        cur = lst[i]

    #print("min = ",cur)

    return cur


def fillupper():

    kk = k

    i = n - 1

    cur = lst[i]

    while (kk > 0):

        while (lst[i] == cur):

            i -= 1

            # print("i=%d,lst[i]=%d"%(i,lst[i]))

        diff = lst[i + 1] - lst[i]

        kk -= (n - i - 1) * diff

        #print("upper kk = ",kk)

        if kk == 0:

            cur = lst[i - 1]

            break

        elif kk < 0:

            cur = lst[i] + int(-kk / (n - i - 1))

            if (-kk % (n - i - 1) != 0):

                cur += 1

            break

        cur = lst[i]

    #print("max = ",cur)

    return cur


if totalsteps >= k:

    print(fillupper() - filllower())

else:

    print(upper - lower)


'''





def sortmax():

	v = lst[-1]

	i = n-2

	while(i>=0):

		if lst[i]<=v:

			lst[-1]=lst[i+1]

			lst[i+1]=v

			return

		i-=1

	lst[-1]=lst[0]

	lst[0]=v



def sortmin():

	v = lst[0]

	i = 1

	while(i<n):

		if lst[i]>=v:

			lst[0]=lst[i-1]

			lst[i-1]=v

			return

		i+=1

	lst[0]=lst[-1]

	lst[-1]=v





lst.sort()

while k:

	lst[-1]-=1

	sortmax()

	#print(lst)

	lst[0]+=1

	sortmin()

	if (lst[-1]-lst[0])<=1:

		break

	#print(lst)

	k-=1





print(lst[-1]-lst[0])





'''


# Made By Mostafa_Khaled
