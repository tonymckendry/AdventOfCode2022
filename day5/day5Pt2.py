import re
# row 1-8 has the starting arrangement
# row 11-end has the moves

# index 1 is where the first crate letter is, the next is on index 5 and the next is on index 9, the last is index 35
crateLayout = []

with open('input.txt') as inputFile:
  rows = inputFile.read()
  crateRows = rows.splitlines(
  )[:8][::-1]  # reversed so we can build arrays in the correct order
  for rowI in range(len(crateRows)):
    for letterI in range(0, 9):
      # loops through each crate in the row
      # crate index pattern: 1, 5, 9, 13...35
      if rowI == 0:
        crateLayout.append([])
      crateLetter = crateRows[rowI][1 + (letterI * 4)]
      if crateLetter != ' ':
        crateLayout[letterI].append(crateLetter)
  # crateLayout index are representative of each stack in the original layout with the last item in each array being on top 
  moves = rows.splitlines()[10:]
  
  for moveRow in moves:
    move = re.sub("[^0-9\s]", "", moveRow).split(' ') # filter out everything but numbers and spaces (to keep the number separated)
    while "" in move:
      # clean up the empty strings leftover
      move.remove("")
    liftedCrates = crateLayout[int(move[1]) - 1][-int(move[0]):] # items picked up 
    crateLayout[int(move[1]) - 1] = crateLayout[int(move[1]) - 1][:-int(move[0])] # items remaining in stack
    crateLayout[int(move[2]) - 1] += liftedCrates # add lifted items onto designated stack

for crate in crateLayout:
  print(crate)