# This contains the files for reading and writing user data so we can keep track of clicks
#Data is stored like this:
#name1 clicks
#name2 clicks
#..
import os

# Adds a user to the file
def addUser(username):
  with open("userdata.txt","w") as file:
    file.write("%s 0" % username)

# Returns the number of clicks a user has, given his username. Returns -1 if user was not found
def getUserClicks(username):  
  with open("userdata.txt", "r") as f:
    data = f.readlines()

    for line in data:
      words=line.split()
      if words[0]==username:
        return words[1]
  return -1      


# Returns the data at a line number
def getAtLine(i):
  with open("userdata.txt", "r") as f:
    return f.readLines()[i].split()

# Increments the clicks of a user
def incrementUserClicks(username):    

  with open("userdata.txt", "r") as fin, open("userdata.txt.tmp", "w+") as fout:
    for line in fin:
      lineout = line
      words=line.split()
      
      name=words[0]
      clicks=words[1]
      
      if name == username:
        lineout = "%s %s\n" %(name, int(clicks)+1)
      
      fout.write(lineout)

  os.rename("userdata.txt.tmp", "userdata.txt")



