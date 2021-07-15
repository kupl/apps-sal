elevator = lambda left,right,call: 'left' if abs(call-left) < abs(call-right) else 'right'
