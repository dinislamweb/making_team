# Team Maker App

A command-line Python application to help you form teams from a list of players, with interactive player management and fair, random assignment.

## Features
- Input the total number of players and their names
- Edit player names interactively
- Specify the number of teams and their names
- Select which players to include in each lottery round
- Randomly and fairly assign selected players to teams, repeating until all are assigned
- Undo the last lottery round if needed
- Clear, visually separated final team assignments

## How to Use
1. **Run the app:**
   ```bash
   python team.py
   ```
2. **Follow the prompts:**
   - Enter the total number of players and their names
   - Use the menu to list or edit player names
   - Enter the number of teams and their names
   - For each round, select which available players to assign
   - Type `back` during player selection to undo the previous round if needed
   - After all players are assigned, view the final team assignments

## Example Output
```
Final Team Assignments:
              TEAM A
              ______
  1. Alice
  2. Bob

              TEAM B
              ______
  1. Carol
  2. Dave

All players have been assigned!
```

## Requirements
- Python 3.x
- No external dependencies

## Notes
- All input and output is via the terminal/command prompt.
- The app ensures fairness by shuffling players before assignment.
- You can only edit player names after initial entry (no add/remove in menu).

## License
This project is provided for educational and personal use.
