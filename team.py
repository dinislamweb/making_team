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

