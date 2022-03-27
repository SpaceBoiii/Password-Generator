import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?,.@#$%^&*'

length = input('Password length?')
length = int(length)
passnumber = input('How many passwords?')
passnumber = int(passnumber)
for p in range(passnumber):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)