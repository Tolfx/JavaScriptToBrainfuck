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

# Function to convert  
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
        a = stripped_line.split("(")[1]
        a = a.replace(")", "")
        a = a.replace("\"", "")
        a = a.replace("'", "")
        a = a.replace("`", "")
        a = a.replace(";", "")
        
        # Convert to ascii
        asciiBF = []
        for letter in a:
            asciiBF.append(ord(letter))

        # Turn into to brainfuckery
        for x in asciiBF:
            for y in range(x):
                # Issue.. will continue, so need to break and make sure the cell doesnt go over 255
                brainPrint.append(BF_ADD)
                if (y+1) == x:
                    brainPrint.append(BF_PRINT)
                    brainPrint.append(BF_POINTER_RIGHT)

fileName = "compiled.b"
createFile = open(fileName, "w")
createFile.write(listToString(brainPrint))
print(f'All done, made file: {fileName}')
