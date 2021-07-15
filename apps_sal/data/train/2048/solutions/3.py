import sys

inp = sys.stdin.read().splitlines()
n,k = list(map(int,inp[0].split()))
lst = list(map(int,inp[1].split()))
lst.sort()
total = sum(lst)
lower = int(total/n)
nupper = total%n

if nupper == 0:
	upper = lower;
else:
	upper = lower+1;
nlower = n - nupper;

i = 0;
while i<n and lst[i]<lower:
	i+=1
low1st = i; 

i = n-1;
while i>=0 and lst[i]>upper:
	i-=1
uplast = i;

lowerfill = low1st*lower - sum(lst[:low1st]) 

upperfill = sum(lst[uplast+1:]) - (n-uplast-1)*upper

totalsteps = (lowerfill+upperfill)/2

def filllower():
	kk = k
	cur = lst[0]
	i = 0
	while (kk>0):
		while (lst[i]==cur):
			i+=1
		diff = lst[i] - lst[i-1]
		kk -= i*diff
		if kk == 0:
			cur = lst[i]
			break
		elif kk<0:
			cur = lst[i]-int(-kk/i)-1
			if (-kk%i) ==0:
				cur += 1
			break
		cur = lst[i]
	return cur

def fillupper():
	kk = k
	i = n-1
	cur = lst[i]
	while (kk>0):
		while (lst[i]==cur):
			i-=1
		diff = lst[i+1] - lst[i]
		kk -= (n-i-1)*diff
		if kk == 0:
			cur = lst[i-1]
			break
		elif kk<0:
			cur = lst[i]+int(-kk/(n-i-1))
			if (-kk%(n-i-1)!=0):
				cur += 1;
			break
		cur = lst[i]
	return cur

if totalsteps>=k:
	print(fillupper()-filllower())
else:
	print(upper-lower)

