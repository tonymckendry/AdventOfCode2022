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

outcomes = {
  'X': 'lose',
  'Y': 'draw',
  'Z': 'win'
}

score = 0

with open('input.txt') as inputFile:
  for line in inputFile:
    intendedOutcome = outcomes[line[2]]
    opponentShape = opponentShapes[line[0]]
    
    # I wanted to use a match/switch here but it would not work
    if intendedOutcome == 'win':
      # win - 6 points
      roundScore = 6
      for key in shapes:
        # loop the 3 shapes and figure out which one we need to win
        if shapes[key]['beats'] == opponentShape:
          shapeScore = shapes[key]['score']
          
    elif intendedOutcome == 'draw':
      # draw - 3 points 
      shapeScore = shapes[opponentShape]['score'] # same score as opponent's shape since we drew
      roundScore = 3
      
    else : 
      # lose - 0 points
      myShape = shapes[opponentShape]['beats'] # pick the shape that my opponent's shape beats
      shapeScore = shapes[myShape]['score']
      roundScore = 0

    # add the shape score and the round score to the score accumulator
    score += (shapeScore + roundScore)
    
print(score)  