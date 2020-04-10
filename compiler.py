import re

#open the file and put it into a string
JSfile = open("test.jsi","r")
text = JSfile.readlines()
resultFile = open("resulat.js","w")

#stack of indentations works like a counter for closing
stack = []
result=""

#Compiler
for line in text :
    while len(stack)>0 and (len(re.findall(" {4}",line))<len(stack)):
            result += "\t"*(len(stack)-1) + stack.pop() + "\n"
    if re.match(".*:\n",line) :
        line = line.replace(":","{")
        result += line
        stack.append("}")
    else :
        result += line

#for last line exception
while len(stack) > 0 :
    result += "\n" + "\t"*(len(stack)-1) + stack.pop()

#writing in the file
print(result,file=resultFile)

