import json
import os
import bs4 as bs
import urllib.request
import time

BF_POINTER_RIGHT = ">"
BF_POINTER_LEFT = "<"
BF_ADD = "+"
BF_SUBTRACT = "-"
BF_PRINT = "."
BF_READ = ","
BF_WHILE = "["
BF_WHILE_END = "]"
BF_CLEAN_CELL = "[-]>"

In_Loop = False

# Returns a list of the console log
def ConsoleLog(consoleLog: str):
    asciiBF = []
    printBF = []
    a = consoleLog.split("(")[1]
    a = a.replace(")", "")
    a = a.replace("\"", "")
    a = a.replace("'", "")
    a = a.replace("`", "")
    a = a.replace(";", "")
    
    # Convert to ascii
    count = 0
    while len(a) > count:
        if a[count] == "\\" and a[count+1] == "n":
            asciiBF.append(int("10"))
        else:
            asciiBF.append(ord(a[count]))

        count = count + 1

    # Turn into to brainfuckery
    for x in asciiBF:
        for y in range(x):
            printBF.append(BF_ADD)
            if (y+1) == x:
                printBF.append(BF_PRINT)
                printBF.append(BF_CLEAN_CELL)
    return printBF

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1

brainPrint = []
# Lets start with console.log
with open("js.js", "rt") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    if stripped_line.find("console.log") != -1:
        console = ConsoleLog(stripped_line)
        brainPrint.append(listToString(console))



fileName = "compiled.b"
createFile = open(fileName, "w")
createFile.write(listToString(brainPrint))
print(f'All done, made file: {fileName}')
