def decode(message):
    res=""
    c=0
    for i in range(0, len(message)):
        if message[i]=="a":
            res+="z"
        elif message[i]=="z":
            res+="a"
        elif message[i]=="b":
            res+="y"
        elif message[i]=="y":
            res+="b"
        elif message[i]=="c":
            res+="x"
        elif message[i]=="x":
            res+="c"
        elif message[i]=="d":
            res+="w"
        elif message[i]=="w":
            res+="d"
        elif message[i]=="e":
            res+="v"
        elif message[i]=="v":
            res+="e"
        elif message[i]=="f":
            res+="u"
        elif message[i]=="u":
            res+="f"
        elif message[i]=="g":
            res+="t"
        elif message[i]=="t":
            res+="g"
        elif message[i]=="h":
            res+="s"
        elif message[i]=="s":
            res+="h"
        elif message[i]=="i":
            res+="r"
        elif message[i]=="r":
            res+="i"
        elif message[i]=="j":
            res+="q"
        elif message[i]=="q":
            res+="j"
        elif message[i]=="k":
            res+="p"
        elif message[i]=="p":
            res+="k"
        elif message[i]=="l":
            res+="o"
        elif message[i]=="o":
            res+="l"
        elif message[i]=="m":
            res+="n"
        elif message[i]=="n":
            res+="m"
        else:
            res+=" "
    return res
