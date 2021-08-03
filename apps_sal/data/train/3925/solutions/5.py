def is_john_lying(a, b, s): return s >= abs(a) + abs(b) and -~s + a + b & 1
