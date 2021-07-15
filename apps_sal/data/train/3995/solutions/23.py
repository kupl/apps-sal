dating_range = lambda age : str (age // 2 + 7) + "-" + str ((age - 7) * 2) if (age > 14) else str (int (age - 0.10 * age)) + "-" + str (int (age + 0.10 * age));
