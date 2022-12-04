no game new = False 
accumulator = 0
highScore = 0

with open('input.txt') as inputFile:
  for line in inputFile:
    if line != '\n': # a line with a value
      if new == True: # previous line was blank, need to reset 
        if accumulator > highScore: # save new high score before reset 
          highScore = accumulator 
        accumulator = 0
        new = False  
      accumulator += int(line)
    else: # a blank line
      new = True 

print(highScore)