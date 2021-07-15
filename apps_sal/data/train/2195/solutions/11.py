def solution(n, num_array):

	# If there is only one element in the list, return 0.
	# import pdb; pdb.set_trace
	if (len(num_array) == 1):
		return 0
	

	# sort the array first
	num_array.sort()
	idx1 = 0
	idx2 = 1
	res = 0
	while (idx2 < len(num_array)):
		num1 = num_array[idx1]
		num2 = num_array[idx2]

		if (num1 < num2):
			# swap the numbers
			res += 1
			idx1 += 1
			idx2 += 1

		else:
			idx2 += 1

	# print(sorted_arr)
	return res




n = input()
num_array = list(map(int, input().split()))

print(solution(n, num_array))



