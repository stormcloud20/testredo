import re



text = input("enter an email\n")
x = re.search("^[^.][a-zA-Z0-9._#!%$‘&+*–/=?^`.{|}~]+@^[^-][a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", text)

if x:
  print("matches")
else:
  print("no match")
