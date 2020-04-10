import re

#my regular expressions
r = "function +\w+\(\w*\) +:\n"
#open the file and put it into a string
file = open("test.js","r")
text = file.readlines()

print(text)

for line in text :
    if(re.match(r,line)):
        print("function regnosized")
    else :
        print("no function")