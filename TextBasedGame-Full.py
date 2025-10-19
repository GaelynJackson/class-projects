#Text Based Game: Boo-siness Not So Casual
#Gaelyn Jackson

def main():
    #Room directory to show which rooms are in which direction from the room the player is in.
    rooms = {
        'Entrance': {'East': 'Lobby'},
        'Lobby': {
            'West': 'Entrance',
            'North': 'First Office',
            'East': 'Break Room',
            'South': 'Second Office'
        },
        'First Office': {'South': 'Lobby', 'East': 'Manager Office'},
        'Manager Office': {'West': 'First Office'},
        'Break Room': {'West': 'Lobby', 'North': 'Restroom'},
        'Restroom': {'South': 'Break Room'},
        'Second Office': {'North': 'Lobby', 'East': 'Janitor Closet'},
        'Janitor Closet': {'West': 'Second Office'}
    }

    #Room items to show which items are in which rooms.
    room_items = {
        'First Office': 'glass jar',
        'Manager Office': 'desk toy',
        'Break Room': 'saltshaker',
        'Restroom': 'candle',
        'Second Office': 'chalk',
        'Janitor Closet': 'vacuum'
    }

    # Items that transform into something new when picked up
    item_changes = {
        'desk toy': 'iron',
        'saltshaker': 'salt'
    }

    #The player will get these messages whenever they enter a room for the first time.
    room_messages = {
        'Lobby': "It smells like mildew and dirt.  Some of the floor tiles are broken, but there's an area big enough to set a trap.",
        'First Office': "One of the desks has an old glass candy jar.  It still has old candy inside it and you're not brave enough to eat it.",
        'Manager Office': "There are some old papers scattered everywhere and an old desk chair is on its side.  On the desk is an old magnetic desk toy; if you break it open you might find some iron shavings.",
        'Break Room': "You couldn't be paid enough to eat any food that would've gotten left behind.  An old saltshaker is sitting on the counter, and luckily it has some salt still inside it.",
        'Restroom': "Someone was really thoughtful and put a candle in here.  It doesn't have much of a scent anymore, but a candle is a candle.",
        'Second Office': "There's an old chalkboard on the wall and a used chalk stick on the worn floor.  You're pretty sure it hasn't been touched in years.",
        'Janitor Closet': "There's an old handheld vacuum on a shelf, and surprisingly it still works.  You can't afford to be picky with what's available,so you can maybe figure out a use for it."
    }

    #These are messages the player will get once they grab an item.
    item_messages = {
        'glass jar': "You take the lid off the jar and tip it over, and the old candy falls onto the floor.",
        'desk toy': "You slam the toy into the desk, which breaks the toy open.  You scoop some of the iron shavings into the glass jar.",
        'saltshaker': "You screw the top off the saltshaker and pour the leftover salt into the glass jar with the iron shavings.",
        'candle': "Apparently it's supposed to be lavender scented.  Your pockets are deep enough you can slide it into your pocket.",
        'chalk': "There's an old chalkboard on the wall with a couple of chalk sticks laying around.  You grab one of the chalk sticks and put it in your other pocket.",
        'vacuum': "The fact that this still works boggles your mind.  You look at it with confusion, but stuff it under your arm."
    }

    #This is the setup
    inventory = []
    visited_rooms = set()
    current_room = 'Lobby'
    total_items = len(room_items)

    #This will show the player a backstory for the game and instructions on how to play.
    def game_start():
        print("\nYou are an amateur paranormal investigator, and today you have decided to break into the abandoned office building near the outskirts of a local city after hearing rumors of an apparition being seen standing in a window.")
        print("You've never actually found proof of ghosts, but you are filled with determination!")
        print("After walking around for about two hours, you've once again failed to find any proof of ghosts.")
        print("Ready to head back home, you go to leave the building.  As you go to walk out the building, an eerie moan echos through the building and you jump and wildly swing your head to look around.")
        print("Just your luck, a ghost is blocking the exit, which also just so happens to be the same door you've came in and there conveniently are no other exits.  You swallow the lump in your throat and begin to form a plan.")
        print("You've never actually built anything to trap a ghost, but you remember reading about ways to trap ghosts online with things that can be easy to find.")
        print("You know you will need: a glass jar, iron, salt, a candle, and some chalk.  You're pretty sure you've seen some stuff that was left behind that you could use; It wasn't like anyone was going to come back for it.")
        print("Maybe you should play it safe and grab the handheld vacuum in the janitor's closet too.  It's stupid, but you never know, it could end up useful.")
        print("You now have a plan, but will it work?  Oh well you don't have many options and honestly, you just want to go home.")
        print("You need to be smart about this, if that ghost touches you, it will steal your soul! (Probably? You don't want to find out).")
        print("You need to gather items from each room and build a trap in the lobby to lure the ghost out and trap it.  To move to a different room, please type North, South, East, or West.")
        print("To add an item to your inventory, please type 'Grab [item_name]'.")
        print("Now lets get to it!!")

    #Inventory function, this will show the player the inventory
    def show_inventory():
        if inventory:
            print("\nYou have:")
            for item in inventory:
                print(f" - {item}")
        else:
            print("\nYou don't have anything right now, you should probably go look for stuff.")

    #This will let the program know the game has started.
    game_start()

    #The game loop starts here!
    while True:
        print(f"\nYou are in the {current_room}.")

        #The player gets a message when they visit a room for the first time
        if current_room not in visited_rooms:
            visited_rooms.add(current_room)
            #This is a message that each room will show when the player enters them for the first time
            if current_room in room_messages:
                print(f"\n{room_messages[current_room]}")
            #The player will see this if there is an item in the room.
            if current_room in room_items:
                print(f"This {room_items[current_room]} looks useful.")

        #Player types in a direction or to grab an item.
        command = input("\nEnter a direction or 'Grab [item_name]': ").strip()

        #Player grab commands
        if command.lower().startswith('grab'):
            parts = command.split(maxsplit=1)

            # Player typed only "grab" without item
            if len(parts) == 1:
                print("Umm...ok, what are you trying to grab?")
                continue

            # Player typed "grab [item_name]"
            item_name = parts[1].strip().lower()

            # Check if the item exists in the current room
            if current_room in room_items and room_items[current_room].lower() == item_name:
                item = room_items.pop(current_room)

                #The player will get this message when they grab an item.
                print(f"\n{item_messages.get(item, 'You picked it up.')}")

                #This checks if the item changes and shows the correct item in the inventory.
                if item in item_changes:
                    new_item = item_changes[item]
                    inventory.append(new_item)
                    print(f"You took the {new_item} from the {item}.")
                else:
                    inventory.append(item)
                    print(f"\nYou grabbed the {item}.")

                # Show inventory after picking up
                show_inventory()

            #The player gets an error message if they are attempting to grab an item that isn't in the room or if there are no items in the room.
            else:
                if current_room in room_items:
                    print(f"That item isn't in this room.")
                else:
                    print("There's nothing else in here that's useful.")
            continue

        #lets players type either go [direction] or just the direction without having to capitalize it.
        if command.lower().startswith('go '):
            direction = command[3:].strip().capitalize()
        else:
            direction = command.capitalize()

        #The player will get a message to let them know which room they are in.
        if direction in ['North', 'South', 'East', 'West']:
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"\nYou walked to the {current_room}.")

                #The player loses if they go to the entrance if they haven't grabbed all items and returned to the lobby.
                if current_room == 'Entrance':
                    print("\nWhat are you doing? The ghost is right there!")
                    print("The ghost attacked you!")
                    print("\nGame Over :(")
                    break

                #The player wins if they grab all the items and return to the lobby.
                if current_room == 'Lobby' and len(inventory) == total_items:
                    print("\nYou take the chalk and quickly draw some symbols that you memorized from a totally legit website you came across once.")
                    print("You then sprinkle the salt and iron mix over the symbols. You then put the candle in the middle of the symbol and placed the glass jar over the candle.")
                    print("The ghost slowly comes towards you. This is it, you're going to die and you won't know how that show you're watching will end.")
                    print("The ghost lifts its hand slowly, pointing at the candle on the ground.")
                    print("'It has to be lit dude,' the ghost says.")
                    print("Oh shoot, you didn't think about that. You think quickly, whipping the vacuum out from under your arm and point it towards the ghost.")
                    print("The ghost just stares at you. You stare back and aim the vacuum at it. Before the ghost could get a laugh out, you press the button to turn it on.")
                    print("The ghost lets out a yelp and begins to get sucked into the vacuum. You stare at the vacuum in astonishment; you weren't expecting that to work!")
                    print("The ghost is now gone and the exit is clear. You quickly run out towards the exit, and out into the world.")
                    print("Now time to get home and shove it in everyone's faces that you found a real ghost.")
                    print("You won!")
                    break

            else:
                print("There are no rooms in that direction.")

        else:
            print("What? That is not a valid direction.")

main()