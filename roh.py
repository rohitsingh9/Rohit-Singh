
import os
import time
WIDTH = 79
message = "rohit!".upper()

printedMessage = [ "","","","","","","" ]

characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "R" : [ "*****",
                       "*   *",
                       "*   *",
                       "*****",
                       "**   ",
                       "* *  ",
                       "*  * " ],
               
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "T" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],
               
               "I" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "*****" ],
               
               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]

               
               }
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

offset = WIDTH
while True:
    os.system("cls")
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    offset -=1
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    
    time.sleep(0.05)
