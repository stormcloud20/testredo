import re



text = input("enter a java variable,class,or method name\n")
x = re.search("^[a-zA-Z_$][a-zA-Z0-9_$]*$", text)

if x:
  print("matches")
else:
  print("no match")
