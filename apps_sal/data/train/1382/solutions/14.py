def pos(lst):
 return [x for x in lst if x < 0]
N=int(input())
List1=[int(x) for x in input().split()]
X=int(input())
Sum=0
List=pos(List1)
List.sort()
if(len(List)>X):
 Sum+=(-1*List[X])*X
 for i in range(X):
  Sum+=(-1*List[i])+List[X]
else:
 Sum+=(-1*sum(List))
print(Sum)
  

