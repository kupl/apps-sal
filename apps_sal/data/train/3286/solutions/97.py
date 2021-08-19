exec('\ndef enough(cap, on, wait):\n    a = on + wait\n    b = cap - a \n    if b >= 0:\n        return 0\n    else:\n        return abs(b)\n')
