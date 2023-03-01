import re



text = input("enter a multi line c++ comment\n")
x = re.search("^([\/][\*])+(.)+([\*][\/])", text)

if x:
  print("matches")
else:
  print("no match")
