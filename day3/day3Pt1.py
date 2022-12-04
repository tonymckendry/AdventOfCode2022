# each line in input file is one "rucksack"
# each "rucksack" has two "compartments" of equal size
# the items in the rucksack are represented by the individual characters in the strings
# exactly half of the characters in the line are in the first compartment and so on
# A and a are different items
# items have priorities - lowercase are 1-26 and uppercase are 27-52

# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?

# ord A = 65
# ord a = 97
# ord C = 67
# ord c = 99

# print(ord('a') - 96) # gives us a 1-index value for lowercase
# print(ord('A') - 38) # gives us a 27-index value for uppercase

prioritySum = 0

with open('input.txt') as inputFile:
  for rucksack in inputFile:
    c1, c2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:] # compartments
    sharedItem = set(c1).intersection(c2).pop() # get common items between compartments
    subtractor = 96 if sharedItem.islower() else 38 # makes a = 1 and A = 27
    itemPriority = ord(sharedItem) - subtractor 
    prioritySum += itemPriority 

print(prioritySum)