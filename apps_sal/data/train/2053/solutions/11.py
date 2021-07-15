from sys import stdin, stdout

def take_input():
	return [int(x) for x in stdin.readline().rstrip().split()]

def min_sweets(b, g, b_sweet, g_sweet):
	if (len(b_sweet) == 0 or len(g_sweet) == 0):
		return -1
	total_sum = 0
	max_b = b_sweet[0]
	second_max_b = -1
	max_ind = 0
	for index, el in enumerate(b_sweet):
		if(el > max_b):
			max_b = el
			max_ind = index
		total_sum += (el*g)
	for index, el in enumerate(b_sweet):
		if(el <= max_b and el > second_max_b and max_ind != index):
			second_max_b = el

	min_g = g_sweet[0]
	for i in g_sweet:
		if i < min_g:
			min_g = i
		total_sum += i
	if (max_b > min_g):
		return -1
	if max_b == min_g:
		total_sum -= (max_b * g)
	if max_b < min_g:
		total_sum = total_sum - (max_b * (g-1))
		total_sum = total_sum - second_max_b
	return total_sum
	

b, g = take_input()
b_sweet = take_input()
g_sweet = take_input()
stdout.write(str(min_sweets(b, g, b_sweet, g_sweet)) + "\n")

# stdout.write( str(b*g) + "\n" )
# stdout.write( str(b_sweet[0]) + "\n" )

