def kadane(l):
	current_sum,best_so_far=0,-9999999999999
	for i in l:
		current_sum+=i
		if best_so_far<current_sum:
			best_so_far=current_sum
		if current_sum<0:
			current_sum=0
	return best_so_far
def max_sum(l,k):
	if k==1:
		ans=kadane(l)
		return ans
	current_prefix_sum,best_prefix_sum=0,-99999999999999
	current_postfix_sum,best_postfix_sum=0,-9999999999999
	total_sum=0
	for i in l:
		current_prefix_sum+=i
		best_prefix_sum=max(current_prefix_sum,best_prefix_sum)
	total_sum=current_prefix_sum
	for i in range(len(l)-1,-1,-1):
		current_postfix_sum+=l[i]
		best_postfix_sum=max(current_postfix_sum,best_postfix_sum)
	if total_sum<0:
		ans=max(best_prefix_sum+best_postfix_sum,kadane(l))
	else:
		ans=max(best_prefix_sum+best_postfix_sum+((k-2)*total_sum),kadane(l))
	return ans
t=int(input())
while t>0:
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	print(max_sum(l,k))
	t-=1
