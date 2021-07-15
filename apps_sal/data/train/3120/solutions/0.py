def meeting(rooms, need):
    if need == 0: return "Game On"
    
    result = []
    for people, chairs in rooms:
        taken = min(max(chairs - len(people), 0), need)
        result.append(taken)
        need -= taken
        if need == 0: return result
        
    return "Not enough!"
