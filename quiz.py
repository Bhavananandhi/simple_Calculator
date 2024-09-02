print("Welcome to my compuetr quiz!!")

opinion=input("Do you wanna play the game? ")
score=0
if opinion.lower()!="yes":
    quit()
print("Okay, Let's play!")
q1=input("Who is the father of computer? ")
if q1.lower()=="charles babbage":
    print("WOHOO!! CORRECT ANSWER")
    score+=1
else:
    print("INCORRECT ANSWER")
q2=input("What is the full form of CPU? ")
if q2.lower()=="central processing unit":
    print("WOHOO!! CORRECT ANSWER")
    score+=1
else:
    print("INCORRECT ANSWER")
q3=int(input("Which state in Andhra Pradesh is known as Gods own country?\n1.Tamilnadu\n2.Kerala\3\n3.Maharastra\n "))
if q3==2:
    print("\5WOHOO!! CORRECT ANSWER")
    score+=1
else:
    print("INCORRECT ANSWER")
print("You got "+str(score)+" answers correct")
print("You got "+str((score/3)*100)+"%")