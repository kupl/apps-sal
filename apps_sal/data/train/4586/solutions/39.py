def tv_remote(word): #there are more efficient ways to do it, but I want to try it manually
    keyboard = ["abcde123","fghij456","klmno789","pqrst.@0","uvwxyz_/"]
    x = 0
    y = 0
    steps = 0
    for c in word:
        while keyboard[y][x] != c:
            steps += 1
            print(keyboard[y][x])
            if c in keyboard[y]: #if you're at the right row
                if keyboard[y].find(c) < x: #if c is to the left of the current position
                    x -= 1 #press left
                else:
                    x += 1 #press right
            else:
                if "".join(keyboard).find(c) < y*8+x: #this was the shortest way I could think of if you include numbers and chars
                    y -= 1 #press up
                else:
                    y += 1 #press down
        steps += 1 #press ok
    return steps
