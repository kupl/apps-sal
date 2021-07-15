def decompose_single_strand(single_strand):
    frame1= "Frame 1:"
    frame2= "Frame 2:"
    frame3= "Frame 3:"
    i=0
    while i in range(len(single_strand)):
        frame1+= " "+(single_strand[i:i+3])
        i+=3
    i=1
    frame2+= " " +(single_strand[0])
    while i in range(len(single_strand)):
        frame2+= " "+(single_strand[i:i+3])
        i+=3
    i=2
    frame3+= " "+(single_strand[0:2])
    while i in range(len(single_strand)):
        frame3+= " "+ (single_strand[i:i+3])
        i+=3
    frames = (frame1+'\n'+frame2+'\n'+frame3)
    return frames
