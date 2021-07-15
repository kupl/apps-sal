m = int(input())
s = input().strip()

sa = [0] * len(s)
for i in range(len(s)):
	sa[i] = ord(s[i]) - ord('a')

sa = [-1] + sa + [-1]

def check_value(sa, m, threshold):
	prev_ind = 0
	for i in range(len(sa)):
		if sa[i] <= threshold:
			if i - prev_ind <= m:
				prev_ind = i
			else:
				return False
	return True

def get_indexes(sa, threshold):
	seq = [i for i in range(len(sa)) if sa[i] <= threshold]
	# seq = []
	# for i in range(len(sa)):
	# 	if sa[i] < threshold:
	# 		seq[i].append(sa[i], i)
	return seq

def filter_indexes(sa, seq, el, m):
	new_seq = [0]
	for i in range(1, len(seq) - 1):
		if sa[seq[i]] != el or (sa[seq[i]] == el and seq[i+1] - new_seq[-1] > m):
			new_seq.append(seq[i])
	return new_seq[1:]


threshold = -1
while (not check_value(sa, m, threshold)):
	# print(threshold, get_indexes(sa, threshold))
	threshold += 1
# print(threshold, get_indexes(sa, threshold), sa)

seq = get_indexes(sa, threshold)
seq = filter_indexes(sa, seq, threshold, m)

s = ''.join(sorted([chr(ord('a') + sa[x]) for x in seq]))
print(s)
