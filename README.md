# Team Maker App

A Python application (CLI and GUI) to help you form teams from a list of players, with interactive player/team management and fair, random assignment.

## Features
- Input the total number of players and their names (auto-formatted: each word capitalized)
- Edit player names interactively
- Specify the number of teams and their names (auto-formatted: each word capitalized)
- Select which players to include in each lottery round
- Randomly and fairly assign selected players to teams, repeating until all are assigned
- Undo the last lottery round if needed
- Clear, visually separated final team assignments
- **GUI version (Tkinter):**
  - Modern, colorful, and responsive interface
  - Centered, visually appealing menus and dialogs
  - Click team names to view player lists
  - Save team assignments to a file

## How to Use
### CLI Version
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

### GUI Version
1. **Run the GUI app:**
   ```bash
   python team_gui.py
   ```
2. **Use the graphical interface:**
   - Enter the number of players/teams, then their names (auto-formatted)
   - Edit names, start the lottery, and view teams
   - Click a team name to see its players
   - Save results to a file

## Example Output (CLI)
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
- All input and output is via the terminal/command prompt or GUI window.
- The app ensures fairness by shuffling players before assignment.
- Player and team names are always formatted with each word capitalized.
- You can only edit player names after initial entry (no add/remove in menu).

## License
This project is provided for educational and personal use.
