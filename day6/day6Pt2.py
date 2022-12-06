index = 0
found = False

with open('input.txt') as inputFile:
  dataStream = inputFile.read()
  n = 14
  setsOfCodes = [dataStream[i:i+n] for i in range(len(dataStream)-n+1)]
  for code in setsOfCodes:
    index += 1
    correct = True
    for char in set(code):
      count = code.count(char)
      if count > 1: 
        correct = False
    if correct and found == False:
      found = True
      print(index + (n-1)) 
      