import re

#Here Put your file name
YourFileName = "test.jsi"
'''needs to be in .JSI format'''
YourOutputFileName = "result.js"
'''needs to be in .JS format'''

#main script
if __name__ == "__main__":

    #open the source file JSI
    try :
        JSfile = open(YourFileName,"r")
    except FileNotFoundError :
        print("File Not Found Error")
        exit(1)

    #getting your lines of code
    code = JSfile.readlines()

    #stack of indentations works like a counter for closing
    stack = []
    result=""

    #Compiler
    for line in code :
        #test if a close is needed before to proceed
        while len(stack)>0 and (len(re.findall(" {4}",line))<len(stack)):
                result += "\t"*(len(stack)-1) + stack.pop() + "\n"
        #verify if a line has a scope after
        if re.match(".*:\n",line) :
            line = line.replace(":\n","{\n")
            result += line
            stack.append("}")
        else :
            #add a normal line or a line in a scope
            result += line

    #closing the left scopes at the end of lecture
    while len(stack) > 0 :
        result += "\n" + "\t"*(len(stack)-1) + stack.pop()

    #opening the output JS file
    try :
        resultFile = open(YourOutputFileName,"w")
    except FileExistsError :
        print("this file exists do you want to overwrite it ? (Y/N) : ", end="")
        answer = input()
        if answer == "N" or answer =="n":
            exit(1)

    #writing in the new file
    print(result,file=resultFile)
    #succesfully operation console /**message can be deleted**/
    print("Compilation succesfully done ! Find your JS code in "+YourOutputFileName)

pass

