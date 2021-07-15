_,*A=map(int,open(0).read().split());s=A[0]
for a in A[1:]:s^=a
print(*[a^s for a in A])
