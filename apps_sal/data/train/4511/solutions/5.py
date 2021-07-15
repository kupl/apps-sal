permute_a_palindrome=lambda s:sum(f%2for f in __import__('collections').Counter(s).values())<2
