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
def select_players(players, assigned):
    """
    Allows the user to select a subset of unassigned players for the current lottery round.

    This function filters out already assigned players, displays the list of available players,
    and lets the user choose which ones to include in the next random team assignment.

    Parameters:
    players (list): A complete list of all player names (strings).
    assigned (list): A list of already assigned player names (strings) to be excluded.

    Returns:
    list or None:
        - Returns a list of selected player names (strings) if selection is successful.
        - Returns None if the user types 'back', indicating they want to exit selection.

    Input Format:
    - User is prompted to enter a comma-separated list of player numbers based on the displayed list.
    - Example: `1, 3, 4` selects the 1st, 3rd, and 4th available players.
    - Typing `back` allows the user to cancel and go back to the previous menu.

    Notes:
    - Invalid or out-of-range inputs are handled gracefully with informative prompts.
    - Players who have already been assigned are not shown in the selection list.
    """
    available = [p for p in players if p not in assigned]
    while True:
        print("\nAvailable players for this round:")
        for idx, name in enumerate(available, 1):
            print(f"{idx}. {name}")
        print("Enter player numbers from the current available list separated by commas (e.g., 1,3,5):")
        inp = input("Select players: ").strip()
        if inp.lower() == 'back':
            return None  # Signal to go back
        try:
            indices = [int(i)-1 for i in inp.split(',') if i.strip().isdigit()]
            selected = [available[i] for i in indices if 0 <= i < len(available)]
            if selected:
                return selected
            else:
                print("No valid players selected.")
        except Exception:
            print("Invalid input. Try again.")




