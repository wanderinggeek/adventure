from sys import exit

def bat_country():
    print "You walk up the creaking, old stairs and are greeted by eerie silence upon your arrival."
    print "As you start to explore the upper floor you see a bat fly by. Then another. Then 15."
    print "Before long there are so many bats it is hard to see anything in front of you and"
    print "impossible to see anything out of the windows up here."
    
    print "What do you do?"
    windows_open = False
    
    while True:
        choice = raw_input(">")
        
        if choice == "open windows" and not windows_open:
            print "The bats all fly out of the windows and it reveals a door in front of you."
            print "What now?"
            windows_open = True
        elif choice == "run":
            start()
        elif choice == "open door" and windows_open:
            win("You find that this door leads you back to the outside world.")
        else:
            dead("You get lost in the swarm of bats and can't find your way out. You eventually die.")
            
            

def garden():
    print "You walk into a small, dark garden that has only dead plants." 
    print "There are two doors in front of you. Which do you choose?"
    
    door = raw_input(">")
    
    if "1" in door:
        tiger_room()
    elif "2" in door:
        snake_room()
    else:
        dead("While wandering around the garden a singing plant comes out of the wall and eats you. You are dead!")

def snake_room():
    print "As you open the door, you hear something that faintly sound like water running."
    print "As you step into the room the sound becomes clearer. It is actually the sounds of snakes hissing. You are now standing right by a pile of about 50 snakes."
    print "There is a door on the other side of the room over the snake pile and a ladder in the middle."
    print "What do you do?"
    print "1. Jump over snakes to door"
    print "2. Climb the ladder."
    print "3. Run."
    
    choice = raw_input(">")
    
    if choice == "1":
        dead("You run and jump higher than you ever have before! As you are almost to the other side a giant snake springs from the pile and drags you down.\n You are quickly bitten by all of the other snakes who are pissed that you landed on their heads. Luckily for you, your death only takes a couple of minutes.")
    elif choice == "2":
        win("You jump onto the ladder and start climbing. As you are half-way up a snake starts to strike at you but you quickly throw your cheeseburger into it's mouth and it falls down choking.\n You climb up the ladder to safety. Upon reaching the next room, you realize that you have found a secret exit out of here.")
    elif choice == "3":
        start()
    else:
        dead("While you are overtaken with indecision the snakes come out of the pile and start biting you. You are dead.")
        

def tiger_room():
    print "You go through the door into a small room. On the other side is another door."
    print "Unfortuntely there is a tiger between you and that door."
    print "He can smell your cheeseburger and he looks hungry."
    print "What do you do?"
    
    choice = raw_input(">")
    
    if choice == "cheeseburger":
        win("The tiger thanks you and eats the cheeseburger. You walk past him and through the door.")
    elif choice == "run":
        start()
    else:
        dead("The tiger jumps on top of you and mauls you to death.")
      
def win(won):
    print won, "You safely made it through the castle and to freedom. You win!"
    exit(0)

def front_door():
    print "You go inside of the giant wooden door and come into the main hall."
    print "There is a huge stairway in front of you that goes up to the second floor."
    print "Do you want to go upstairs or explore the ground floor?"
    
    choice = raw_input(">")
    
    if "floor" in choice:
        kitchen()
    elif choice == "upstairs":
        bat_country()
    else:
        dead("You wander around until you starve to death.")
        
def dead(why):
    print why, "Good job!"
    exit(0)
    
    
def kitchen():
    print "You explore the ground floor and eventually come into the kitchen. You hear maniacal laughter and a man in a chef's outfit starts running toward you with a knife."
    print "You see a frying pan and some flour in front of you. There is a door just past the chef, across the kitchen."
    print "How do you get past him?"
    distracted = False
    
    while True:
        choice = raw_input(">")
        
        if choice == "run":
            start()
        elif choice == "flour" or "pan" and not distracted:
            print "He is distracted and you can go through the door."
            distracted = True
        elif choice == "open door" and distracted:
            win("You run past him and through the door. Lucky for you it leads outside.")
        else:
            print "That didn't work. Do something else before he stabs you!"
            
    
    
    
    
def start():
    print "You are stranded at an old castle and need to find a way to get through it and\n to the highway on the other side. All you have to help you is a cheeseburger." 
    print "There is no way other than to go through the castle property." 
    print "You can either go through the front door, or around the back to what looks like a garden."
    print "Which way do you go?"
    
    way = raw_input(">")
    
    if way == "garden":
        garden()
    elif "door" or "front" in way:
        front_door()
    else:
        dead("You get lost in the castle and eventually starve to death.")
        

    
            

        
start()
        
        
