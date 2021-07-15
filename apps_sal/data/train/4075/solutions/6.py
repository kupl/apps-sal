def something_acci(num_digits):
    a = [1,1,2,2,3,3]
    while a[-1] < 10**(num_digits-1):
        a.append(a[-1]*a[-2]*a[-3]-a[-4]*a[-5]*a[-6])
        
    return (len(a),len(str(a[-1])))
