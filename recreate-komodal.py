# rebuilds a repository from the downloaded code text files
# please install js-beautify and run the command at the end of the script

import os
import errno
import sys

if len(sys.argv) < 2:
  print("Usage python3 recreate-komodal.py repoName")
  exit()

repoName = sys.argv[1]
ignoreFileNames = '.idea'

def makePath(filename):
  if not os.path.exists(os.path.dirname(filename)):
      try:
          os.makedirs(os.path.dirname(filename))
      except OSError as exc: # Guard against race condition
          print("had issue")

def main():
  with open('raw/' + repoName + '.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

  firstLine = True
  curFile = 0
  curFilename = 0
  for line in lines:
    if not firstLine:
      if repoName + "\xa0/\xa0" in line and ignoreFileNames not in line:
        file = line.replace("\xa0", "")
        lastFileName = file.split('/')[-1]
        if '.' in file[-5:] or lastFileName.startswith('.'):
          os.makedirs(os.path.dirname(file), exist_ok=True)
          if not os.path.isdir(file):
            curFile = open(file,"w")
            curFilename = file
            print(file)
      else:
        if curFile != 0:
          curFile.write(line + '\n')
    firstLine = False
main()

print('After running, execute the following: \n find . -type f -name "*" -exec js-beautify -r {} \; ')