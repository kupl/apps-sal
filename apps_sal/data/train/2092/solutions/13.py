n = int(input())
code = input()

lines = []
for i in range(n):
    lines.append(input())
    
went = 0
came = 0
for line in lines:
    if line.startswith(code):
        went += 1
    else:
        came += 1
        
if went > came:
    print("contest")
else:
    print("home")
