index = 0
found = False

with open('input.txt') as inputFile:
  dataStream = inputFile.read()
  n = 4
  setsOf4 = [dataStream[i:i+n] for i in range(len(dataStream)-n+1)]
  for code in setsOf4:
    index += 1
    correct = True
    for char in set(code):
      count = code.count(char)
      if count > 1: 
        correct = False
    if correct and found == False:
      found = True
      print(index + 3) # answer wants the character that makes the 4 character string appear as you iterate through
      