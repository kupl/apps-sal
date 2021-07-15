def parse_float(ts):
    try:
      float(ts)
      return float(ts)
    except:
      return None
