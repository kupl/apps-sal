# import sys

# sys.stdin = open('cf586d.in')



def handle_test():

	n, k = [int(v) for v in input().split()]



	field = [input() for _ in range(3)]



	if field[0][0] == 's':

		cpos = [0, 0]

	elif field[1][0] == 's':

		cpos = [1, 0]

	else:

		cpos = [2, 0]



	available = [[False] * len(field[0]) for _ in range(3)]

	available[cpos[0]][cpos[1]] = True



	for i in range(n):

		for j in range(3):

			if available[j][i]:

				if i + 1 >= n:

					return True

				elif field[j][i + 1] != '.':

					continue

				for offset in (-1, 0, 1):

					if not (0 <= j + offset < 3) or field[j + offset][i + 1] != '.':

						continue

					if i + 2 >= n:

						return True

					elif field[j + offset][i + 2] != '.':

						continue

					elif i + 3 >= n:

						return True

					elif field[j + offset][i + 3] != '.':

						continue

					else:

						available[j + offset][i + 3] = True



	return False





t = int(input())

for _ in range(t):

	print(['NO', 'YES'][handle_test()])



# Made By Mostafa_Khaled

