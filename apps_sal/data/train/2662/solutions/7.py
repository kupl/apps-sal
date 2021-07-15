def shoot(arr):
    pete, phil = 0, 0
    for i in arr:
        score = 2 if i[1] == True else 1
        pete += i[0]['P1'].count('X')*score
        phil += i[0]['P2'].count('X')*score
    return "Pete Wins!" if pete > phil else "Phil Wins!" if phil > pete else "Draw!"
