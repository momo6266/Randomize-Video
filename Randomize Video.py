import os, random
from os import startfile

print ("Welcome!")

loop = 0

while loop == 0:
    print ("\n")
    a = (random.choice(os.listdir("C:\\Your directory")))
    b = "C:\\Your directory" + a
    print ("Video selected: " + a)
    ans = input("Are you confirm with the video: (Y)es (N)o\n")
    
    allowed_access = ["yes", "Y", "Yes", "y", "YES"]
    
    if ans in allowed_access :
        startfile(b)
        loop = 1
    else:
        loop = 0
        
