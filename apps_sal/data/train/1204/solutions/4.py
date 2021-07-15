# P.S.: I understood the solution using the code of https://www.codechef.com    /viewsolution/33283413 
# the user's name is kush_07(thanks to him), but it took me some time to figure     it out so i
# have written some comments which might help you if you by any chance arrive at     the solution.
for _ in range(int(input())):
 s=list(input())
 r=list(input())
 l=[]
 flag=0
 eq=0
 k=0
 s_1=0
 for i in range(len(s)):
  if s[i]!=r[i]:
   # When the group/array is not the first array to have different                 characters 
   # this is identified using the flag variable
   # as we don't need the elements which were before the first                 different
   # subarray but only need the elements between the different                 subarrays after
   # the first subarray having different characters (subarrays here                 refer to 'islands' 
   # mentioned in the tutorial)
   if eq>0 and flag==1:
    l.append(eq)
    k+=1
   # we are not appending the equal elements before this as this is the                 first subarray with
   # different characters (flag==0) but we still need to count it as                 one operation so k+=1
   elif flag==0:
    k+=1
   eq=0
   flag=1
   # Number of characters that would require replacing
   s_1+=1
  else:
   # Counting the same characters 
   eq+=1
 l.sort()
 res=0
 res=k*s_1
 for i in range(len(l)):
  s_1=s_1+l[i]
  k=k-1
  res=min(res,s_1*k)
 print(res)
   
   

