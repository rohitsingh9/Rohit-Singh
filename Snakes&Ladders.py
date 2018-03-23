import random #import the random function to generate random no.s for the game
count=0 #position of the dice starts from zero
r=0 #random number before the game is played 
while count <= 100: #the value of count can be less than or equal to zero
    roll = input("Press r to roll the dice:\n") #input function for rolling the dice
    if roll == 'r': #assigning roll variable the value r
        r = random.randint(1,6) #r can generate value from 1 to 6
        count = count+r #value of count is count+random number(r)
        print ("Your random number is",r) #print the random number
        print ("Your count is",count) #print the count
        print (input ("Press any key to exit"))

        #checking_for_snakes_and_ladders

        if count == 38:
               count = 9
               print ("You've bitten by snake")
               print ("Your count is",count)
        elif count == 8:
               count = 37
               print ("Climb up the ladder")
               print ("Your count is",count)
        elif count == 25:
               count = 4
               print ("You've bitten by snake")
               print ("Your count is",count)
        elif count == 3:
               count = 34
               print ("Climb up the ladder")
               print ("Your count is",count)
        elif count == 11:
               count = 2
               print ("You've bitten by snake")
               print ("Your count is",count)
        elif count == 40:
               count = 68
               print ("Climb up the ladder")
               print ("Your count is",count)
        elif count == 65:
               count = 46
               print ("You've bitten by snake")
               print ("Your count is",count)
        elif count == 52:
               count = 81
               print ("Climb up the ladder")
               print ("Your count is",count)
        elif count == 93:
               count = 64
               print ("You've bitten by snake")
               print ("Your count is",count)
        elif count == 76:
               count = 97
               print ("Climb up the ladder")
               print ("Your count is",count)
        elif count == 89:
               count = 70
               print ("You've bitten by snake")
               print ("Your count is",count)
        elif count =100:
            print ("You've won the game)
        
        
               
               
