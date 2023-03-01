import re



text = input("enter a floating point constant\n")
x = re.search("[-|+]?(([1-9][0-9]*)|0)(\.[0-9]+)?([eE][-+]?[0-9]+)?[fFlL]?$", text)

if x:
  print("matches")
else:
  print("no match")
