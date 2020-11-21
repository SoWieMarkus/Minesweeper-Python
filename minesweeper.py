import random
import os

height = 10;
width = 10;
fields = []
cover = []

def main():

    global height
    global width

    errorMessage = "Please enter a number between 1 and 9!";

    height = enterNumber(1,9, "Heigth (1-9): \n > ", errorMessage)
    width = enterNumber(1,9, "Width (1-9): \n > ", errorMessage)

    fillList(height ,width)

    while True:
        os.system("cls") # Windows
        printField()
        txt = input( "F<x><y> ... Mark field with coordinates x and y as unsafe (example: F12)\nC<x><y> ... Uncover field with coordinates x and y (example: C12) \n > ")
        if list(txt)[0] == "F":
            cover[int(list(txt)[1])][int(list(txt)[2])] = 2
        if list(txt)[0] == "C":
            cover[int(list(txt)[1])][int(list(txt)[2])] = 0
            if fields[int(list(txt)[1])][int(list(txt)[2])] == 9:
                os.system("cls") # Windows
                printField()
                print("Verloren")
                break
            if fields[int(list(txt)[1])][int(list(txt)[2])] == 0:
                check(int(list(txt)[1]), int(list(txt)[2]))
               
            if checkWin():
                os.system("cls") # Windows
                printField()
                print("Gewonnen")
                break
            
def checkWin():
    amount = height * width
    amount_correct = 0
    amount_unfound_bombs = 0
    for i in range (0, height):
        for j in range (0, width):
            if cover[i][j] == 0:
                amount_correct = amount_correct + 1
            if cover[i][j] == 2 and fields[i][j] == 9:
                amount_correct = amount_correct + 1
            elif fields[i][j] == 9:
                amount_unfound_bombs = amount_unfound_bombs + 1
    if amount_correct == amount:
        return True
    if amount_correct+amount_unfound_bombs == amount:
        return True
    else:
        return False

def fillList(height, width):
    global fields
    for i in range (0, height):
        row = []
        row2 = []
        for j in range (0, width):
            row2.append(-1)
            row.append(0)
        fields.append(row)
        cover.append(row2)
    setBombs(10)

def setBombs(mode):
    global height
    global width
    global fields

    amount = int((height*width)/mode)
    for i in range (0, amount):
        while True:
            x = random.randrange(height)
            y = random.randrange(width)
            if fields[x][y] == 0:
                fields[x][y] = 9
                break
    countFields()

def countFields():
    for i in range (0, height):
        for j in range (0, width):
            amount = 0
            if fields[i][j] < 9:
                amount = amount + isBomb(i-1,j)
                amount = amount + isBomb(i-1,j-1)
                amount = amount + isBomb(i-1,j+1)
                amount = amount + isBomb(i,j-1)
                amount = amount + isBomb(i,j+1)
                amount = amount + isBomb(i+1,j-1)
                amount = amount + isBomb(i+1,j)
                amount = amount + isBomb(i+1,j+1)
                fields[i][j] = amount

def check(i,j):
    if uncover(i-1,j-1):
        check(i-1,j-1)
    if uncover(i-1,j):
        check(i-1,j)
    if uncover(i-1,j+1):
        check(i-1,j+1)
    if uncover(i,j-1):
        check(i,j-1)
    if uncover(i,j+1):
        check(i,j+1)
    if uncover(i+1,j-1):
        check(i+1,j-1)
    if uncover(i+1,j+1):
        check(i+1,j+1)
    if uncover(i+1,j):
        check(i+1,j)
   

def uncover(i, j):
    if i < 0:
        return False
    if j < 0:
        return False
    if i >= height:
        return False
    if j >= width:
        return False
    if cover[i][j] == 0:
        return False
    cover[i][j] = 0
    if fields[i][j] == 0:
        return True
    else:
        return False
    
def isBomb(i,j):
    if i < 0:
        return 0
    if j < 0:
        return 0
    if i >= height:
        return 0
    if j >= width:
        return 0
    if fields[i][j] == 9:
        return 1
    else:
        return 0
                    
def printField():
    global width
    global height

    header = " ║"
    line = "═╬"

    for i in range (0, width):
        header = header + str(i)
        line = line + "═"
    print(header)
    print(line)

    for i in range(0, height):
        line = str(i) + "║"
        for j in range (0, width):
            line = line + getValue(i,j)
        print(line)


def getValue(i, j):
    if cover[i][j] == -1:
        return "X"
    elif cover[i][j] == 1:
        return "Ö"
    elif cover[i][j] == 2:
        return "#"

    value = fields[i][j]
    if value == 0:
        return " "
    elif value == 9:
        return "Ö"
    elif value == 10:
        return "#"
    else:
        return str(value)

def enterNumber(min, max, message, errorMessage):
    number = 0
    while True:
        try:
            number = int(input(message))
            if number >= min and number <= max:
                return number
            print(errorMessage)
        except ValueError:
            print("Please enter a number!")


if __name__ == "__main__":
    main();