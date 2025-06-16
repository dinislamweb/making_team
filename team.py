import random

def get_int_input(prompt, min_value=1):
    """
    Prompt the user for integer input with a minimum value.

    Args:
        prompt (str): The message to display to the user.
        min_value (int, optional): The minimum acceptable value. Defaults to 1.

    Returns:
        int: The validated integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a number >= {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def list_players(players):
    """
    Displays a numbered list of current players.

    Parameters:
    players (list): A list of player names (strings).

    Returns:
    None: This function only prints the list of players to the console.
    """
    print("\nCurrent Players:")
    for idx, name in enumerate(players, 1):
        print(f"{idx}. {name}")
    print()
def edit_player(players):
    """
    Allows the user to edit the name of an existing player from the list.

    This function first displays the current list of players, then prompts the user 
    to select a player by their index number. It then asks for a new name and updates 
    the player's name if the input is valid.

    Parameters:
    players (list): A list of player names (strings) to be edited.

    Returns:
    None: The function modifies the 'players' list in place and prints messages to the console.

    Notes:
    - Uses `get_int_input()` function (assumed to be defined elsewhere) to safely get numeric input.
    - Does not allow setting an empty name.
    - If an invalid player number is entered, an error message is displayed.
    """
    list_players(players)
    idx = get_int_input("Enter the number of the player to edit: ", 1)
    if 1 <= idx <= len(players):
        new_name = input(f"Enter new name for {players[idx-1]}: ").strip()
        if new_name:
            players[idx-1] = new_name
            print("Player name updated.")
        else:
            print("Name cannot be empty.")
    else:
        print("Invalid player number.")

def manage_players(players):
    """
    Provides a simple interactive menu for managing player names.

    This function allows the user to:
    - View the current list of players.
    - Edit the name of any existing player.
    - Exit the player management loop.

    The function runs in a loop until the user chooses the 'Done' option.

    Parameters:
    players (list): A list of player names (strings) to be managed.

    Returns:
    None: Modifies the 'players' list in place and interacts via console I/O.

    Menu Options:
    1. List players — displays all current players.
    2. Edit player — lets user change the name of a specific player.
    3. Done — exits the player management menu.

    Notes:
    - Uses `list_players()` and `edit_player()` functions internally.
    - Input is handled via standard input; user must enter a valid menu option.

    """
    while True:
        print("\nPlayer Management:")
        print("1. List players")
        print("2. Edit player")
        print("3. Done")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            list_players(players)
        elif choice == '2':
            edit_player(players)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")



