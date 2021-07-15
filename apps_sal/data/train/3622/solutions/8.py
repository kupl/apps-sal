def validate_usr(user):
  return 3 < len(user) < 17 and all(c in 'abcdefghijklmnopqrstuvwxyz_0123456789' for c in user)
