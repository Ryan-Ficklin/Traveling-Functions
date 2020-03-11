global name
global FREEWILL
def intro():
    global name
    global FREEWILL
    name = input("What is your name? ")
    print("And thus our story begins.")
    FREEWILL = 5
    twoDoors()

def twoDoors():
    global name
    global FREEWILL
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
            twoDoors()
    else:
        print(f"{name}'s independence overtook them and they went through the door on the right.")
        rightDoor()

def leftDoor():
    global name
    global FREEWILL
    print(f"As they knew they should, {name} took the left door, and felt good for doing so.")
    print(f"After walking for some time, high on good decisions, {name} came across three branching paths, and continues along the middle path")
    print("1 - Take the left path")
    print("2 - Take the middle path")
    print("3 - Take the right path")
    choice = int(input())
    if(choice == 1):
        FREEWILL+=1
        wrongPath()
    elif(choice == 2):
        FREEWILL-=1
        correctPath()
    elif(choice == 3):
        FREEWILL+=1
        wrongPath()
    else:
        print(f"Funny, {name}, but please pick a choice you actually have access to.")
        FREEWILL+=1
        leftDoor()
        
def rightDoor():
    global name
    print(f"Despite their better judgement, {name} went through the door on their right.")

def wrongPath():
    global name
    print(f"Despite {name}'s previous inclination to making good choices, they took the wrong path.")

def correctPath():
    global name
    global FREEWILL
    print(f"{name} made the right decision and went along the middle path.")

intro()
    
