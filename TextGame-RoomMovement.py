# Simple Haunted Office text based game: moving between rooms, quit, and game over
# Gaelyn Jackson

#Haunted Office room directory
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

#The player will see this when the game starts, will give a small backstory as well as instructions to move around.
print('\nYou are trapped in a haunted office building!')
print('Unfortunately, a ghost blocks the entrance that happens to also be the only exit.')
print('It is now time to be brave and figure a way to leave this building in one piece.')
print('To move to a different room, type a direction (North, South, East, or West).')

# Player starts in the lobby
current_room = 'Lobby'

#The loop players will be in while they travel, will show so that players are prompted to enter a command.
while True:
    print(f'\nYou are in the {current_room}.')
    command = input("Choose a direction to move or type 'quit' to leave the game: ").strip().lower()

    #If the player types quit, the game with show a message 'See ya later!'
    if command == 'quit':
        print('See ya later!')
        break

    #Allows the player to type a direction without getting an error, lets a player type "Go [direction]" without an error message.
    if command.startswith('go '):
        direction = command[3:].strip().capitalize()
    else:
        direction = command.capitalize()

    #This will check to make sure that the direction is valid
    if direction in ['North', 'South', 'East', 'West']:
        # If this direction exists for the current room, then the player will move
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print(f'You move walked to the {current_room}.')

            #Game Over message player will get if going to the Entrance
            if current_room == 'Entrance':
                print('\nWhat are you doing? The ghost is right there!')
                print('The ghost attacked you!')
                print('\nGame Over:(')
                break
        else:
            print('There are no rooms in that direction.')
    else:
        print('What?  That is not a valid direction.')