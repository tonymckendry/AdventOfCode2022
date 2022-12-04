# Every Elf carries a badge that identifies their group
# the badge is the only item type carried by all three Elves.
# If a group's badge is item B, then all three Elves will have item B in their rucksack
# and at most two of the Elves will be carrying any other item type.

# Every set of 3 lines is one group
# identify the badges and sum up their item priorities

# print(ord('a') - 96) # gives us a 1-index value for lowercase
# print(ord('A') - 38) # gives us a 27-index value for uppercase

prioritySum = 0

with open('input.txt') as inputFile:
  lines = inputFile.read().splitlines()
  
  # split elves into groups of 3 
  groupSize = 3
  elfGroups = [lines[i:i + groupSize] for i in range(0, len(lines), groupSize)] 
  
  for group in elfGroups:
    badgeItem = set(group[0]).intersection(group[1], group[2]).pop() # find the common item between the 3 elves 
    subtractor = 96 if badgeItem.islower() else 38  # makes a = 1 and A = 27
    itemPriority = ord(badgeItem) - subtractor
    prioritySum += itemPriority

print(prioritySum)
