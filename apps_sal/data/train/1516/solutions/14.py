# cook your dish here
t=int(input())
for _ in range(t):
 n,k=map(int,input().split())
 summation=0
 last_term=k-1
 common_difference=n-1
 first_term=last_term%common_difference
 if first_term==0:
  first_term=common_difference
 no_of_terms=(last_term-first_term)//common_difference + 1
 #print(no_of_terms,first_term,last_term,common_difference)
 summation=(((no_of_terms)*(first_term+last_term))//2)%1000000007
 print(summation)
