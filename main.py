print("welcome to my computer quiz!")

playing=input("do you want to play? ")

if playing.lower()!="yes":
    quit()

print("okay! let's play :)")
score=0

answer=input("What is the Capital of India? ")
if answer.lower()=="delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("What does W.H.O stands for? ")
if answer.lower()=="world health organization":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("Who is the First Prime Minister of India? ")
if answer.lower()=="jawaharlal nehru":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("Who invented Computer? ")
if answer.lower()=="charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("Who is known as Father of Indian Constitution? ")
if answer.lower()=="dr.b.r.ambedkar":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got "+ str(score)+ " questions correct!")
print("You got "+ str((score/5)*100)+" %.")