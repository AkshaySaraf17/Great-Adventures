import time
import os
import sys

import sys

def racing_track():
    track_width = 15
    track_length = 20
    print("Setting up track...")
    for i in range(track_width):
        for j in range(track_length):
            if i == 0 or i == track_width - 1:
                print('', end='')
            elif j == 0 or j == track_length - 1:
                print('|', end='')
                time.sleep(0.2)
            else:
                print(' ', end='')
        print()

def find_shortcut():
    def clear_screen():

        if sys.platform.startswith('win'):
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    track = [
        "|             |",
        "|             |",
        "|   🏃        |",
        "|    /\\       |",
        "|   /  \\      |",
        "|  /    \\     |",
        "| /      \\    |",
        "|             |",

    ]
    print("Alright, should find shortcut now")

    for _ in range(1):
        for frame in range(1):
            clear_screen()
            for line in track:
                print(line)

            # Simulate the stick figure moving through the shortcut
            track[3] = "|              |"
            track[4] = "|    🏃        |"

            time.sleep(0.2)

            clear_screen()
            for line in track:
                print(line)

            # Return to the original position
            track[3] = "|   🏃         |"
            track[4] = "|    /\\       |"

            time.sleep(0.2)

    clear_screen()
    for line in track:
        print(line)
    print("Woah,that was fast")
# Call the function to see the animation


def display_marketplace():
    print("""
    *****************************************
    *       Virtual Marketplace            *
    *****************************************
    """)
    print("You enter a dazzling virtual marketplace filled with various stalls and vendors.")
    time.sleep(2)
    print("""
       ______
     /      \\
    |  $$_$$ |
    |  |__|  | 
    |   __   | 
    |  |  |  | 
    |__|  |__|
    """)
    print("A mysterious vendor catches your eye, offering a rare and powerful upgrade.\n")
    time.sleep(2)




def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def display_social_hub():
    print("""
    *****************************************
    *          Social Hub                   *
    *****************************************
    """)
    type_effect("The social hub buzzes with activity. A mysterious character offers a cryptic quest.\n")
    time.sleep(1)

    character_art = [
        "( )",
        "-|-",
        "/_\\"
    ]
    for line in character_art:
        type_effect(line, delay=0.5)
    print()

def display_winning_animation():
    message = "YOU WON THE RACE!!!! 🔥🏆🔥"

    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)

    time.sleep(1)
    print("\nKudos ✨ to you for believing in yourself & going solo and making the right choices as others turned out to be zombies 🎉🎉\n")
    time.sleep(3)
    print("GAME OVER............ 🛑‼️💔")


def display_player_death_animation():
    print("In the cold silence of betrayal, you realize that the ally you trusted has revealed their true colors.\n"
          "As the shadows of deception unfold, your vision fades into darkness.\n"
          "The unknown person you placed your trust in has proven to be a formidable enemy, and your choice has led you to a grim fate.\n"
          "In the end, the cruel reality dawns upon you—your journey concludes here, a cautionary tale of trust misplaced.\n")
    player_dismantle(my_list)


my_list = ["  O", " /|\\", " / \\"]
def player_dismantle(my_list):

    s = ''
    for item in my_list:
        s += str(item)
    for i in s:
        time.sleep(0.5)
        print(i,end='')
    print("\nPlayer dismantled 😓\nStatus: DEAD")
    sys.exit()








