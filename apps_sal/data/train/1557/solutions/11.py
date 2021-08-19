# cook your dish here
for _ in range(int(input())):
    n = int(input())
    fr = list(input())
    gr = list(input())
    fr.sort()
    gr.sort()
    if(fr == gr):
        print("YES")
    else:
        print("NO")
