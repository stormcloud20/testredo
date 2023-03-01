import re



text = input("enter an even number of a's, an odd number of b's, and any number of c's OR d's (but if you add c's or d's youre lame)\n")
x = re.search("(aa|bb|(ab|ba)(aa|bb)*(ba|ab))*(b|(ab|ba)(bb|aa)*a)((c|d)*)", text)

if x:
  print("matches")
else:
  print("no match")
