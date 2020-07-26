command = ""
started = False
while True:
    command=input("> ").lower()
    if command == "start":
        if started:
            print("car already started!")
        else:
            started= True
            print("car started...")
    elif command == "stop":
        if not started:
            print("car already stoped!")
        else:
            started= False
            print("car started...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
help - for guidlines
quit to exit
              """)
    elif command == "quit":
         break
    else:
        print("Sorry i don't unterstand that")
