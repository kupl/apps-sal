t = int(input())
for test in range(t):
    expression = list(input())
    available_left_arrow = 0
    streak = 0
    max_streak = 0
    for exp in expression:
        if exp == '<':
            available_left_arrow += 1
        else:
            if available_left_arrow <= 0:
                break
            available_left_arrow -= 1
            if available_left_arrow == 0:
                max_streak = max_streak + 2 + streak
                streak = 0
            else:
                streak += 2
            
    print(max_streak)
    
