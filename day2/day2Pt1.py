# 1st column - A rock, B paper, C scissors
# 2nd column - X rock, Y paper, Z scissors
# Shape scores - 1 rock, 2 paper, 3 scissors
# Outcome scores - 0 lose, 3 draw, 6 win 
# Score = shape you selected + score for the outcome of the round 

shapes = {
  'rock':  {
    'beats': 'scissors',
    'score': 1
  },
  'paper':  {
    'beats': 'rock',
    'score': 2
  },
  'scissors': {
    'beats': 'paper',
    'score': 3
  } 
}

opponentShapes = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors'
}

myShapes = {
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
}

score = 0

with open('input.txt') as inputFile:
  for line in inputFile:
    # what is our shape? 
    # did we win or lose?
    opponentShape = line[0]
    myShape = line[2]
    myShapeData =  shapes[myShapes[myShape]]
    print(myShape)
    print(myShapeData)
    
    if myShapeData['beats'] == opponentShapes[opponentShape]:
      # win - 6 points
      roundScore = 6
    elif myShapes[myShape] == opponentShapes[opponentShape]:
      # draw - 3 points  
      roundScore = 3
    else: 
      # lose - 0 points
      roundScore = 0

    # add the shape score and the round score to the score accumulator
    score += (myShapeData['score'] + roundScore)
    
print(score)  