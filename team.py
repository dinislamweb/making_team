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
