import time
import sys


def loading_animation():
    sys.stdout.write("Loading Game")
    for _ in range(7):
        sys.stdout.write("....")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")


def display_intro_animation():
    print(
        "Welcome to the OASIS, a vast virtual universe where anything is possible.\nIn the year 2045, reality is harsh, but the OASIS offers an escape like no other. \nCreated by the eccentric genius Hari, Akshay, Tanmay and Abhishek, this digital realm has become a playground for the entire world.")
    time.sleep(1)
    print("\n--- DISCLAIMER: The fate of your journey is in your hands ---\n")
    time.sleep(2)


def get_user_input():
    character_name = input("Enter name to be displayed in the game: ")
    return character_name


def display_character_details(character_name):
    print("\nCreating your character...(this may take a while)")
    time.sleep(4)
    print("\n***************\n")
    time.sleep(0.5)
    print("  O")
    time.sleep(0.5)
    print(" /|\\")
    time.sleep(0.5)
    print(" / \\")
    time.sleep(0.5)
    time.sleep(1)
    print(f"Name: {character_name}")
    print("Level: 1")
    print("Money: 0$")
    print("\n***************")
    time.sleep(1)
    print("\nLET'S PLAY !!!\n")


def start_game():
    # Game loading animation
    loading_animation()
    # Display introduction animation
    display_intro_animation()

    # Get user input
    character_name = get_user_input()

    # Display character details with animations
    display_character_details(character_name)


start_game()
