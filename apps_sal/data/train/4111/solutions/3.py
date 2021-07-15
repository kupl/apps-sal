def sabb(s, value, happiness):
      return "Sabbatical! Boom!" if sum([sum(1 for i in s if i in "sabbatical"), value, happiness]) > 22 else "Back to your desk, boy."


