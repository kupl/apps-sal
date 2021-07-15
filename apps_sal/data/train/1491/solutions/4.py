import sys

a, b, c, d = list(map(float, input().split()))

if a/b == c/d:
 print("Possible")
 return

if a/b == d/c:
 print("Possible")
 return

if a/c == b/d:
 print("Possible")
 return

if a/c == d/b:
 print("Possible")
 return

if a/d == c/b:
 print("Possible")
 return

if a/d == b/c:
 print("Possible")
 return

if a/b == c/d:
 print("Possible")
 return

if a/b == c/d:
 print("Possible")
 return

print("Impossible")
