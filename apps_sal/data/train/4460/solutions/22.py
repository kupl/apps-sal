def whatday(num):
    day=['Wrong, please enter a number between 1 and 7',
          "Sunday",
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday"]
    try:
        return day[num]
    except:
        return day[0]
