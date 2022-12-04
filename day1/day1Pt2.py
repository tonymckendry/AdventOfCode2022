new = False 
accumulator = 0
highScore = 0

elves = []

with open('input.txt') as inputFile:
  for line in inputFile:
    if line != '\n': # a line with a value
      if new == True: # previous line was blank, need to reset 
        elves.append(accumulator) # finished accumulating elf, add to array 
        accumulator = 0
        new = False  
      accumulator += int(line)
    else: # a blank line
      new = True 

elves.sort()

print(sum(elves[-3:]))
