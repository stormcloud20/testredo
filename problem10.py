import re



text = input("enter a integer. can be hex octal or decimal\n")
x = re.search("(0|[1-9]|[0-9]*|0[xX][0-9a-fA-F]+|0[1-7]*)", text)

if x:
  print("matches")
else:
  print("no match")

#number of lexemes is 31