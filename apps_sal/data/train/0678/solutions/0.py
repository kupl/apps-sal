# cook your dish here
test_case = int(input())
while test_case :
 n_people = int(input())
 array = list(map(int, input().strip().split()))
 sums =[0 for i in range(n_people)]
 
 sums[0] = array[0]
 
 for i in range(1, n_people) :
  sums[i] = sums[i-1] + array[i]
  
 # print(sums)

 k = 1 
 count = 0
 i = 0 
 while(k < n_people) :
  k = k + sums[i]
  # print(k)
  i = i + sums[i]
  count = count + 1
 print(count)
 
 
 test_case -= 1
 
  #  2  1  1  5   5   5   5
 # [2, 3, 4, 9, 14, 19, 24]
 #  0  1  2  3  4   5   6 
 
 
 
 
 
 
 
 

