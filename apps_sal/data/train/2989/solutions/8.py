bits_battle=lambda a:{"0":"tie","-":"odds win"}.get(str(sum((-1)**(x%2)*bin(x)[2:].count(str(x%2))for x in a if x))[0],"evens win")
