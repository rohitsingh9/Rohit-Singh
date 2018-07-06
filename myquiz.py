
import random


my_dict =   {
                "My birthdate" : "9-11-1998",
                "My favourite color" : "blue",
                "My height" : "5'10",
                "My weight" : "56",
                "My eye-glasses power" : "-2.5,-2.7",
                "My favourite anime" : "one punch man",
                "My favourite sport" : "football",
                "My age" : "19",
                "My surname" : "singh",
                "My nickname" : "goli",
                "My iris color" : "black"
            }

#welcome message
print("HOW MUCH YOU KNOW ME ??")
print("=======================")
playing = True
while playing == True:
    score = 0
    num = int(input("\nHow many questions would you like: "))
    for i in range(num):

        question = (random.choice( list(my_dict.keys())))
        answer = my_dict[question]
        print("\nQuestion " + str(i+1) )
        print(question  + "?")
        guess = input("> ")
        if guess.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Nope!")
    print("\nYour final score was " + str(score))

    
    again = input("Enter any key to play again, or 'q' to quit.")

    
    if again.lower() == 'q':
        playing = False
