# This contains the files for reading and writing user data so we can keep track of clicks
#Data is stored like this:
#name1|clicks
#name2|clicks
#..
import os

# Adds a user to the file
def addUser(username):
  with open("userdata.txt","a") as file:
    file.write("%s|0 \n" % username)

# Returns the number of clicks a user has, given his username. Returns -1 if user was not found
def getUserClicks(username):  
  with open("userdata.txt", "r") as f:
    data = f.readlines()

    for line in data:
      words=line.split("|")
      if words[0]==username:
        return words[1]
  return -1      


# Returns the data at a line number
def getAtLine(i):
  with open("userdata.txt", "r") as f:
    return f.readLines()[i].strip().split("|")

# Increments the clicks of a user
def incrementUserClicks(username):    

  with open("userdata.txt", "r") as fin, open("userdata.txt.tmp", "w+") as fout:
    for line in fin:
      lineout = line
      words=line.split("|")
      
      name=words[0]
      clicks=words[1]
      
      if name == username:
        lineout = "%s|%s\n" %(name, int(clicks)+1)
      
      fout.write(lineout)

  os.rename("userdata.txt.tmp", "userdata.txt")

def getData(num=-1):
  dataList=[] 
  with open("userdata.txt", "r") as data:
    for fullLine in data:
      splitLine = fullLine.split("|")
      name=splitLine[0]
      numOfClicks=int(splitLine[1])
      dataList.append({"username": name, "clicks": numOfClicks})
    
    sortedData=sorted(dataList, key=lambda i: (-i["clicks"], i["username"]))
    
 
    
    if num != -1:
      returnData=[]     
      for i in range(0,num):
        returnData.append(sortedData[i])

      return returnData
    else: 
      return sortedData
    

