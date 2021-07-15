def snap(flash,bot):
    face_up,c,turn = [],0,1
    while bot:
        face_up.append(flash.pop(0) if turn else bot.pop(0))
        turn ^= 1
        if len(face_up)>1 and face_up[-1] == face_up[-2]:
            flash.extend(face_up) ; face_up = [] ; c += 1 ; turn = 1
    return c
