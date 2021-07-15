def i_tri(s):
    out = 'Starting Line... Good Luck!'
    if s>0.0    and s<=2.4   : out = {'Swim': f'{140.6 - s:.2f} to go!'}
    if s>2.4    and s<=114.4 : out = {'Bike': f'{140.6 - s:.2f} to go!'}
    if s>114.4  and s<130.6  : out = {'Run' : f'{140.6 - s:.2f} to go!'}
    if s>=130.6 and s<140.6  : out = {'Run' : 'Nearly there!'}
    if s>140.6               : out = "You're done! Stop running!"
    return out
    

