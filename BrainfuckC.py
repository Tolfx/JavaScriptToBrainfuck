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

Variables = []
Cells = []

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
            count = count+1
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
                Cells.append(0)
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
    if stripped_line.find("console.log") != -1 and not In_Loop:
        brainPrint.append(listToString(ConsoleLog(stripped_line)))
    if stripped_line.find("while") != 1:
        In_Loop = True

    if stripped_line.find("}") != 1 and In_Loop:
        In_Loop = False

    if stripped_line.find("const" or "let" or "var") != -1:
        itd = stripped_line.replace("const" or "let" or "var", "")
        itd = itd.split("=")
        name = itd[0].strip()
        value = itd[1].strip()
        whichCell = len(Cells)
        Variables.append({
            "cell": whichCell,
            "value": value,
            "name": name
        })
        temp = []
        temp2 = []
        count = 0
        while len(value) > count:
            temp.append(ord(value[count]))

            count = count + 1
        # Turn into to brainfuckery
        for x in temp:
            for y in range(x):
                temp2.append(BF_ADD)

        temp2.append(BF_POINTER_RIGHT)
        Cells.append(0)
        brainPrint.append(listToString(temp2))

fileName = "compiled.b"
createFile = open(fileName, "w")
createFile.write(listToString(brainPrint))
print(f'All done, made file: {fileName}')
