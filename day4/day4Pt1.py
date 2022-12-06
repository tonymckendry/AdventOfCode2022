# is one range inside of the other?
# start has to be greater than or equal
# end has to be less than or equal

# determine which of the pair has the greater start:
# does it come on or before the other's end?
# is its end it less than or equal to the other's end?

# if starts or finish are the same, one will contain the other no matter what

wastedAssignments = 0

with open('input.txt') as inputFile:
  for assignments in inputFile:
    [a, b] = assignments.split(',')
    a = list(map(int, a.split('-')))
    b = list(map(int, b.split('-')))
    if a[0] == b[0] or a[1] == b[1]:
      wastedAssignments += 1
    else:
      firstAssignment = a
      secondAssignment = b
      if a[0] > b[0]:
        firstAssignment = b
        secondAssignment = a

      firstAssignmentLength = (firstAssignment[1] - firstAssignment[0])
      secondAssignmentLength = (secondAssignment[1] - secondAssignment[0])
      startGap = secondAssignment[0] - firstAssignment[0]
      
      if (secondAssignment[0] < firstAssignment[1]) and (firstAssignmentLength - startGap >= secondAssignmentLength):
        wastedAssignments += 1

print(wastedAssignments)