import math
inputs = eval(input())
for i in range(inputs):
	inpu = input().split()
	r1 = float(inpu[0])
	h1 = float(inpu[1])
	r2 = float(inpu[2])
	h2 = float(inpu[3])
	s_r = math.pi * r2 * r2 * h2 
	f_r = 4.0 / 6.0 * math.pi * r1 * r1 * r1
	f_r += math.pi * r1 * r1 * (h1 / 3.0)
	print("%f %f" % (f_r,s_r))
