for _ in range(int(input())):
    n = int(input())
    statement = list(map(int, input().split()))
    fine = 0
    for i, v in enumerate(statement):
        if v == 0:
            fine = (n-i)*100    
            break
                
    total = fine + 1000*statement.count(0)
    print(total)
            
