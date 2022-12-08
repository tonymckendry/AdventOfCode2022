# a directory will contain zero or more other directories and zero or more files

# since we can use objects, we can basically create a JSON-like layout of the directories
# each layer could have a "files" key that contains an array of files and their sizes
# nested folders would simply be keys labeled with their names that contained a similar structure
# we could then loop through these objects and add them up simply.

# we will need to develop a way to parse the data in the input file
# in order to build the map of the file structure that we will need to add up

def deep_access(d, path, newValue='?'):
  keys = path.split(".")
  if keys[0] != '':
    for k in keys:
      if not k in d: d[k] = {'files': [], 'fileSize': 0}
      d = d[k]
  # after the loop is done running, d will be the specified path
  if newValue != '?':
    size = newValue.split(' ')[0]
    d['files'].append(newValue)
    d['fileSize'] += int(size)

def encode(dirPathArray):
  dirPathString = ''
  for path in dirPathArray:
    if len(dirPathString) > 0:
      dirPathString += '.'
    dirPathString += path
  return dirPathString

calculatedSizes = []
def calculateTotalDirSize(dirKey, dir):
  totalDirSize = 0 
  for key in dir.keys():
    if key == 'fileSize':
      totalDirSize += dir[key]
    elif key != 'files':
      if len(dirKey) == 0:
        newKey = key
      else: 
        newKey = dirKey + '.' + key
      totalDirSize += calculateTotalDirSize(newKey, dir[key])
  calculatedSizes.append({'path': dirKey, 'size': totalDirSize})
  return totalDirSize

def checkSizeLimit(sizeItem):
  print(sizeItem)
  if sizeItem['size'] > 100000:
    return False
  else: 
    return True

with open('input.txt') as inputFile:
  rows = inputFile.read()
  commands = rows.splitlines()
  currentDir = []
  fs = {'files': [], 'fileSize': 0}
  for command in commands:
    if command[0] == '$':
    # user input command
    # cd and ls are the only options...for now
      usrCmd = command[2:4]
      if usrCmd == 'cd':
        dirPath = command [5:]
        if dirPath == '/':
          # back to root
          currentDir = []
        elif dirPath == '..':
          # up a level 
          currentDir.pop()
        else: 
          # add a new directory to the path  
          currentDir.append(dirPath)
      # elif usrCmd == 'ls': # not sure if we need to do anything here 
    elif command[0:3] == 'dir':
      # directory
      deep_access(fs, encode(currentDir + [command[4:]])) # passing a path to a directory that does not exist causes it to be created 
    else:
      # file
      deep_access(fs, encode(currentDir), command)
  
  fileSystemSize = calculateTotalDirSize('', fs)

  totalSystemSize = 70000000
  updateSize = 30000000
  neededSize = updateSize - (totalSystemSize - fileSystemSize) 

  sortedSizes = sorted(calculatedSizes, key=lambda d: d['size'])
  answer = 0
  for s in sortedSizes:
    print(s['size'])
    if s['size'] >= neededSize and answer == 0:
      answer = s['size']

  print(answer)
