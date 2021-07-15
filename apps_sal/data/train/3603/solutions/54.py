def lovefunc( flower1, flower2 ):
    count1 =0
    count2 = 0
    for i in range(flower1):
        count1+=1
    for j in range(flower2):
        count2+=1
    if count1 % 2 == 1 and count2 % 2 == 0 or count1 % 2 == 0 and count2 % 2 == 1:
        return True
    else:
        return False
    

