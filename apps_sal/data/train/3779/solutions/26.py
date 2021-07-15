def past(h, m, s):
  return hoursToMilliseconds(h) + minutesToMilliseconds(m) + secondsToMilliseconds(s);

def secondsToMilliseconds(s):
  return s * 1000;

def minutesToMilliseconds(m):
  return secondsToMilliseconds(m * 60);

def hoursToMilliseconds(h):
  return minutesToMilliseconds(h * 60);



