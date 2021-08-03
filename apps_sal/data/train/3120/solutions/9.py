def meeting(rooms, number):
    if number == 0:
        return "Game On"
    chairs = [room[1] - room[0].count('X') for room in rooms]
    chairs = [0 if chair < 0 else chair for chair in chairs]
    ans = []
    i = 0
    while sum(ans) < number and i < len(chairs):
        ans.append(min(chairs[i], number - sum(ans)))
        i += 1
    return ans if sum(ans) >= number else "Not enough!"
