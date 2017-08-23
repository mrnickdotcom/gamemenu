from random import randint 


#player dictionaries
player = {'location':'NYC',
          'name': 'The Agent',
          'class':'SPY',
          'startcity': 'NYC',
          'movement': 0,
          'rolledmove': False}

# the 2d6 roll for movement
def roll_movement():
    return randint(1,6)+randint(1,6)

#check to verify only one movement roll per turn
def movement_check():
    if player["rolledmove"]==False:
        player["movement"]=roll_movement()
        player["rolledmove"]= True
        print("You rolled a " + str(player["movement"]))
    else:
        print("You have rolled this turn. Your current movement is "
              + str(player["movement"]))

#LGM game main turn menu
menu = True
while menu:
    print("""
    1. Where am I?
    2. Roll 2D6 for movement
    3. What is my name?
    4. What is my class?

    Press enter to QUIT
    """)
    menu=input("Please select your turn.")
    if menu =="1":
        print(player["location"])
    elif menu =="2":
        movement_check()
        
    elif menu =="3":
        print(player["name"])
    elif menu =="4":
        print(player["class"])
    elif menu !="":
        print("Select a valid turn number.")
