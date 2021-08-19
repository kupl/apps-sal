# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
num_str_ar = input().strip().split()

num_ar = list(map(int, num_str_ar))
set_tmp = set(num_ar)
final_ar = list(set_tmp)
final_ar.sort()
print((final_ar[-2]))
