global name, FREEWILL
def intro():
    global name, FREEWILL
    FREEWILL = 5
    print("Our story begins. I will be your narrator, and guide you through the optimal path of this story. Follow my directions")
    name = input("What is your name, Stanley? ")
    if(name == "Stanley"):
        print("Very good, Stanley!")
        FREEWILL-=1
    else:
        print(f"Okay then... \"{name}\" ")
        FREEWILL+=1
    twoDoors()

def twoDoors():
    global name, FREEWILL
    print(f"{name} comes across two doors, and enters the one on their left.")
    print("1 - Take the left door.")
    print("2 - Take the right door.")
    if(FREEWILL <= 10):
        choice = input()
        if(choice == '1'):
            FREEWILL-=1
            leftDoor()
        elif(choice == '2'):
            FREEWILL+=1
            rightDoor()
        else:
            print(f"{name}, please pick between the left and the right not '{choice}'")
            FREEWILL+=1
            twoDoors()
    else:
        print(f"{name}'s independence overtook them and they went through the door on the right.")
        rightDoor()

def leftDoor():
    global name
    print(f"As they knew they should, {name} took the left door, and felt good for doing so.")
    threeBranches()

def rightDoor():
    global name
    print(f"Despite their better judgement, {name} went through the door on their right.")
    threeBranches()

def threeBranches():
    global name, FREEWILL
    print(f"After walking for some time, {name} came across three branching paths, and continues along the middle path")
    print("1 - Take the left path")
    print("2 - Take the middle path")
    print("3 - Take the right path")
    choice = input()
    if(choice == '1'):
        FREEWILL+=1
        wrongPath()
    elif(choice == '2'):
        FREEWILL-=1
        correctPath()
    elif(choice == '3'):
        FREEWILL+=1
        wrongPath()
    else:
        print(f"Funny, {name}, but please pick a choice you actually have access to.")
        FREEWILL+=1
        wrongPath()

def wrongPath():
    global name, FREEWILL
    if(FREEWILL <= 5):
        print(f"Despite {name}'s previous inclination to making good choices, they took the wrong path.")
    else:
        print(f"As expected, {name} made the wrong decision once again and goes along the wrong path.")

def correctPath():
    global name, FREEWILL
    print(f"{name} made the right decision and went along the middle path.")

intro()
    
