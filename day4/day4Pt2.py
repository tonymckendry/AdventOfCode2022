overlappingAssignments = 0

with open('input.txt') as inputFile:
  for assignments in inputFile:
    [a, b] = assignments.split(',')
    a = list(map(int, a.split('-')))
    b = list(map(int, b.split('-')))
    
    firstAssignment = a
    secondAssignment = b 
    if a[0] > b[0]:
      firstAssignment = b
      secondAssignment = a

    # if the start OR end of the 2nd assignment falls within the first assignment, they overlap
    if (
      secondAssignment[0] >= firstAssignment[0] and 
      secondAssignment[0] <= firstAssignment[1]
    ) or (
      secondAssignment[1] >= firstAssignment[0] and 
      secondAssignment[1] <= firstAssignment[1]
    ):
      overlappingAssignments += 1

print(overlappingAssignments)
