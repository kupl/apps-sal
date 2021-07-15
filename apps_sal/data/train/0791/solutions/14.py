#!/usr/bin/python
# coding: utf-8

t=int(input())
for i in range(t):
 (n,d)=list(map(int,input().split(' ')))
 arr=list(map(int,input().split(' ')))
 sum=0
 for j in arr:
  sum+=j
 if((sum%n)!=0):
  print("-1")
 else:
  tmp=0
  avg=sum/n
  num=[0]*d
  cnt=[0]*d
  for j in range(n):
   num[j%d]+=arr[j]
   cnt[j%d]+=1
  for j in range(d):
   if(num[j]%cnt[j]!=0 or num[j]/cnt[j]!=avg):
    tmp=1
    break
  if(tmp):
   print("-1")
  else:
   ans=0
   for j in range(n):
    if(arr[j]<avg):
     tmp=avg-arr[j]
     ind=j+d
     if(ind<n and arr[ind]>0):
      ans+=tmp
      arr[j]=avg
      arr[ind]-=tmp
    elif(arr[j]>avg):
     tmp=arr[j]-avg
     ind=j+d
     if(ind<n):
      ans+=tmp
      arr[j]=avg
      arr[ind]+=tmp
   print(ans)


'''

Chef's dog Snuffles has so many things to play with! This time around, Snuffles     has an array A containing N integers: A1, A2, ..., AN.

Bad news: Snuffles only loves to play with an array in which all the elements     are equal.

Good news: We have a mover of size D. !

A mover of size D is a tool which helps to change arrays. Chef can pick two     existing elements Ai and Aj from the array, such that i + D = j and subtract     1 from one of these elements 
(the element should have its value at least 1), and add 1 to the other element.     In effect, a single operation of the mover, moves a value of 1 from one of     the elements to the other.

Chef wants to find the minimum number of times she needs to use the mover of     size D to make all the elements of the array A equal. Help her find this out    .

Input
The first line of the input contains an integer T, denoting the number of test     cases. The description of T test cases follows.
The first line of each test case contains two integers N and D, denoting the     number of elements in the array and the size of the mover.
The second line of each testcase contains N space-separated integers: A1, A2,     ..., AN, denoting the initial elements of the array.

Output
For each test case, output a single line containing the minimum number of uses     or -1 if it is impossible to do what Snuffles wants.

Constraints
1 ≤ T ≤ 10
2 ≤ N ≤ 10^5
1 ≤ D < N
1 ≤ Ai ≤ 10^9

Subtasks
Subtask 1 (30 points) : N ≤ 10^3
Subtask 2 (70 points) : Original constraints

Example
Input:
3
5 2
1 4 5 2 3
3 1
1 4 1
4 2
3 4 3 5

Output:
3
2
-1

Explanation
Testcase 1:
Here is a possible sequence of usages of the mover:
Move 1 from A3 to A1
Move 1 from A3 to A1
Move 1 from A2 to A4
At the end, the array becomes (3, 3, 3, 3, 3), which Snuffles likes. And you     cannot achieve this in fewer moves. Hence the answer is 3.

Testcase 2:
Here is a possible sequence of usages of the mover:
Move 1 from A2 to A1
Move 1 from A2 to A3
At the end, the array becomes (2, 2, 2), which Snuffles likes. And you cannot     achieve this in fewer moves. Hence the answer is 2.

Testcase 3:
It is impossible to make all the elements equal. Hence the answer is -1.

'''

