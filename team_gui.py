import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import random

class TeamMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Team Maker App")
        self.root.minsize(400, 400)
        self.root.geometry("800x600")  # Larger default, but resizable
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.players = []
        self.teams = {}
        self.team_assignments = {}
        self.assigned = set()
        self.history = []
        self.setup_main_menu()

    def setup_main_menu(self):
        for widget in self.root.winfo_children(): widget.destroy()
        main_frame = tk.Frame(self.root, bg="#F2F3F4")
        main_frame.grid(row=0, column=0, sticky="nsew")
        for i in range(7):
            main_frame.rowconfigure(i, weight=1)
        main_frame.columnconfigure(0, weight=1)
        tk.Label(main_frame, text="Team Maker App", font=("Arial", 28, "bold"), fg="#2E86C1", bg="#F2F3F4").grid(row=0, column=0, pady=(30,10), sticky="ew")
        # Centered button frame with smaller buttons and less space between them
        btn_frame = tk.Frame(main_frame, bg="#F2F3F4")
        btn_frame.grid(row=1, column=0, rowspan=5, sticky="n")
        btn_inner = tk.Frame(btn_frame, bg="#F2F3F4")
        btn_inner.pack(expand=True)
        btn_opts = {"width": 25, "height": 1, "font": ("Arial", 14), "anchor": "center", "relief": "raised", "bd": 2}
        tk.Button(btn_inner, text="Enter Players", bg="#D4EFDF", fg="#145A32", command=self.enter_players, **btn_opts).pack(pady=6, ipadx=10, ipady=2)
        tk.Button(btn_inner, text="Edit Players", bg="#FCF3CF", fg="#7D6608", command=self.edit_players, **btn_opts).pack(pady=6, ipadx=10, ipady=2)
        tk.Button(btn_inner, text="Enter Teams", bg="#FADBD8", fg="#922B21", command=self.enter_teams, **btn_opts).pack(pady=6, ipadx=10, ipady=2)
        tk.Button(btn_inner, text="Start Lottery", bg="#D6EAF8", fg="#154360", command=self.start_lottery, **btn_opts).pack(pady=6, ipadx=10, ipady=2)
        tk.Button(btn_inner, text="Exit", bg="#F5B7B1", fg="#641E16", command=self.root.quit, **btn_opts).pack(pady=6, ipadx=10, ipady=2)
        self.root.configure(bg="#F2F3F4")

    def enter_players(self):
        self.players = []
        win = tk.Toplevel(self.root)
        win.title("Enter Players")
        win.geometry("400x450")
        win.configure(bg="#E8F8F5")
        num_label = tk.Label(win, text="Enter number of players:", font=("Arial", 14, "bold"), bg="#E8F8F5")
        num_label.pack(pady=10)
        num_entry = tk.Entry(win, font=("Arial", 12))
        num_entry.pack(pady=5)
        num_entry.focus_set()  # Set focus to number entry immediately
        entry = tk.Entry(win, font=("Arial", 12))
        listbox = tk.Listbox(win, font=("Arial", 12), bg="#FDFEFE")
        def start_entry():
            try:
                self.num_players = int(num_entry.get())
                if self.num_players <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive number.", parent=win)
                return
            num_label.pack_forget()
            num_entry.pack_forget()
            start_btn.pack_forget()
            tk.Label(win, text="Enter player names:", font=("Arial", 14, "bold"), bg="#E8F8F5").pack(pady=10)
            entry.pack(pady=5)
            listbox.pack(pady=10, fill="both", expand=True)
            add_btn.pack(pady=5)
            entry.focus_set()  # Set focus to player name entry immediately
        def add_player():
            name = entry.get().strip()
            if name:
                existing_names = [p.split(' #')[0] for p in self.players]
                if name in existing_names:
                    # Prompt user to enter a unique name
                    suggestion = f"{name} #2"
                    new_name = simpledialog.askstring(
                        "Duplicate Name",
                        f"The name '{name}' is already used.\nPlease enter a unique name (e.g., '{suggestion}'):",
                        parent=win
                    )
                    if not new_name:
                        return
                    name = new_name.strip()
                    # Check again for uniqueness
                    while name in existing_names or not name:
                        name = simpledialog.askstring(
                            "Duplicate Name",
                            f"That name is still not unique or empty. Please enter a unique name:",
                            parent=win
                        )
                        if not name:
                            return
                        name = name.strip()
                self.players.append(name)
                listbox.insert(tk.END, f"{len(self.players)}. {name}")
                entry.delete(0, tk.END)
                entry.focus_set()  # Keep focus for next entry
            if len(self.players) == self.num_players:
                entry.config(state='disabled')
                add_btn.config(state='disabled')
                win.destroy()  # Automatically close when last player is added
        start_btn = tk.Button(win, text="Start", font=("Arial", 12), bg="#D4EFDF", fg="#145A32", command=start_entry)
        start_btn.pack(pady=5)
        add_btn = tk.Button(win, text="Add Player", font=("Arial", 12), bg="#D4EFDF", fg="#145A32", command=add_player)
        # Prevent closing before all players are entered
        def on_closing():
            if len(self.players) < getattr(self, 'num_players', 0):
                messagebox.showwarning("Warning", f"Please enter all {self.num_players} player names before closing.", parent=win)
            else:
                win.destroy()
        win.protocol("WM_DELETE_WINDOW", on_closing)

    def edit_players(self):
        win = tk.Toplevel(self.root)
        win.title("Edit Players")
        win.geometry("400x400")
        win.configure(bg="#FEF9E7")
        listbox = tk.Listbox(win, font=("Arial", 12), bg="#FDFEFE")
        for idx, p in enumerate(self.players, 1):
            listbox.insert(tk.END, f"{idx}. {p}")
        listbox.pack(pady=10, fill="both", expand=True)
        def edit_selected():
            idx = listbox.curselection()
            if not idx:
                return
            idx = idx[0]
            new_name = simpledialog.askstring("Edit Player", f"Edit name for {self.players[idx]}")
            if new_name:
                self.players[idx] = new_name
                listbox.delete(idx)
                listbox.insert(idx, f"{idx+1}. {new_name}")
        tk.Button(win, text="Edit Selected", font=("Arial", 12), bg="#FCF3CF", fg="#7D6608", command=edit_selected).pack(pady=5)
        def done():
            win.destroy()
        tk.Button(win, text="Done", font=("Arial", 12), bg="#F5B7B1", fg="#641E16", command=done).pack(pady=10)

    def enter_teams(self):
        self.teams = {}
        self.team_assignments = {}
        win = tk.Toplevel(self.root)
        win.title("Enter Teams")
        win.geometry("400x450")
        win.configure(bg="#FDEDEC")
        num_label = tk.Label(win, text="Enter number of teams:", font=("Arial", 14, "bold"), bg="#FDEDEC")
        num_label.pack(pady=10)
        num_entry = tk.Entry(win, font=("Arial", 12))
        num_entry.pack(pady=5)
        num_entry.focus_set()  # Set focus to number entry immediately
        entry = tk.Entry(win, font=("Arial", 12))
        listbox = tk.Listbox(win, font=("Arial", 12), bg="#FDFEFE")
        def start_entry():
            try:
                self.num_teams = int(num_entry.get())
                if self.num_teams <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive number.", parent=win)
                return
            num_label.pack_forget()
            num_entry.pack_forget()
            start_btn.pack_forget()
            tk.Label(win, text="Enter team names:", font=("Arial", 14, "bold"), bg="#FDEDEC").pack(pady=10)
            entry.pack(pady=5)
            listbox.pack(pady=10, fill="both", expand=True)
            add_btn.pack(pady=5)
            entry.focus_set()  # Set focus to team name entry immediately
        def add_team():
            name = entry.get().strip()
            if name and len(self.teams) < self.num_teams:
                # Accept duplicate team names
                count = sum(1 for t in self.teams if t == name)
                display_name = name if count == 0 else f"{name} ({count+1})"
                self.teams[display_name] = []
                self.team_assignments[display_name] = []
                listbox.insert(tk.END, f"{len(self.teams)}. {display_name}")
                entry.delete(0, tk.END)
                entry.focus_set()  # Keep focus for next entry
            if len(self.teams) == self.num_teams:
                entry.config(state='disabled')
                add_btn.config(state='disabled')
                win.destroy()  # Automatically close when last team is added
        start_btn = tk.Button(win, text="Start", font=("Arial", 12), bg="#FADBD8", fg="#922B21", command=start_entry)
        start_btn.pack(pady=5)
        add_btn = tk.Button(win, text="Add Team", font=("Arial", 12), bg="#FADBD8", fg="#922B21", command=add_team)
        def on_closing():
            if len(self.teams) < getattr(self, 'num_teams', 0):
                messagebox.showwarning("Warning", f"Please enter all {self.num_teams} team names before closing.", parent=win)
            else:
                win.destroy()
        win.protocol("WM_DELETE_WINDOW", on_closing)

    def start_lottery(self):
        if not self.players or not self.teams:
            messagebox.showerror("Error", "Please enter players and teams first.")
            return
        self.assigned = set()
        self.team_assignments = {team: [] for team in self.teams}
        self.history = []
        self.lottery_round()

    def lottery_round(self):
        available = [p for p in self.players if p not in self.assigned]
        if not available:
            self.show_final_teams_only()
            return
        win = tk.Toplevel(self.root)
        win.title("Select Players for Lottery Round")
        win.geometry("400x500")
        win.configure(bg="#EBF5FB")
        tk.Label(win, text="Select players for this round:", font=("Arial", 14, "bold"), bg="#EBF5FB").pack(pady=10)
        frame = tk.Frame(win, bg="#EBF5FB")
        frame.pack(fill="both", expand=True)
        listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, font=("Arial", 12), bg="#FDFEFE", width=30, height=15)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)
        for idx, p in enumerate(available, 1):
            listbox.insert(tk.END, f"{idx}. {p}")
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        def assign():
            indices = listbox.curselection()
            if not indices:
                messagebox.showerror("Error", "Select at least one player.")
                return
            selected = [available[i] for i in indices]
            random.shuffle(selected)
            team_names = list(self.teams.keys())
            for idx, player in enumerate(selected):
                team = team_names[idx % len(team_names)]
                self.team_assignments[team].append(player)
            self.assigned.update(selected)
            self.history.append(selected)
            win.destroy()
            self.show_current_teams_option()
        tk.Button(win, text="Assign to Teams", font=("Arial", 12), bg="#D6EAF8", fg="#154360", command=assign).pack(pady=5)
        def undo():
            if not self.history:
                return
            last_selected = self.history.pop()
            for player in last_selected:
                self.assigned.remove(player)
                for team in self.team_assignments:
                    if player in self.team_assignments[team]:
                        self.team_assignments[team].remove(player)
            win.destroy()
            self.lottery_round()
        tk.Button(win, text="Undo Last Round", font=("Arial", 12), bg="#F5B7B1", fg="#641E16", command=undo).pack(pady=5)

    def show_current_teams_option(self):
        # Check if all players are assigned
        if len(self.assigned) == len(self.players):
            self.show_final_teams_only()
            return
        win = tk.Toplevel(self.root)
        win.title("Lottery Round Complete")
        win.geometry("400x300")
        win.configure(bg="#FDFEFE")
        tk.Label(win, text="Lottery round complete!", font=("Arial", 14, "bold"), bg="#FDFEFE").pack(pady=10)
        def show_teams():
            win.withdraw()
            self.show_teams_one_by_one(final=False, parent_win=win)
        def continue_lottery():
            win.destroy()
            self.lottery_round()
        tk.Button(win, text="Show Current Teams", font=("Arial", 12), bg="#D4EFDF", fg="#145A32", command=show_teams).pack(pady=10)
        # Only show continue button if not all players assigned
        if len(self.assigned) < len(self.players):
            tk.Button(win, text="Continue Lottery", font=("Arial", 12), bg="#D6EAF8", fg="#154360", command=continue_lottery).pack(pady=10)

    def show_final_teams_only(self):
        win = tk.Toplevel(self.root)
        win.title("Final Team Assignments")
        win.geometry("500x600")
        win.configure(bg="#FDFEFE")
        canvas = tk.Canvas(win, bg="#FDFEFE")
        scrollbar = tk.Scrollbar(win, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#FDFEFE")
        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        for team, members in self.team_assignments.items():
            frame = tk.LabelFrame(scrollable_frame, text=team.upper(), font=("Arial", 18, "bold"), fg="#922B21", bg="#FDFEFE", padx=10, pady=10, labelanchor='n')
            frame.pack(padx=15, pady=15, fill="x")
            for i, member in enumerate(members, 1):
                tk.Label(frame, text=f"{i}. {member}", font=("Arial", 14), fg="#154360", bg="#FDFEFE").pack(anchor="w", pady=2)
        tk.Label(scrollable_frame, text="All players have been assigned!", font=("Arial", 16, "bold"), fg="#229954", bg="#FDFEFE").pack(pady=20)
        tk.Button(scrollable_frame, text="Save Teams to File", font=("Arial", 14), bg="#FCF3CF", fg="#7D6608", command=self.save_teams_to_file).pack(pady=10)
        tk.Button(scrollable_frame, text="Back to Menu", font=("Arial", 14), bg="#F5B7B1", fg="#641E16", command=lambda: [win.destroy(), self.setup_main_menu()]).pack(pady=10)

    def show_teams_one_by_one(self, final=True, parent_win=None):
        teams = list(self.team_assignments.items())
        def show_team(idx):
            for widget in self.root.winfo_children(): widget.destroy()
            team, members = teams[idx]
            frame = tk.Frame(self.root, bg="#FDFEFE")
            frame.pack(expand=True, fill="both")
            tk.Label(frame, text=team.upper(), font=("Arial", 32, "bold"), fg="#922B21", bg="#FDFEFE").pack(pady=30)
            for i, member in enumerate(members, 1):
                tk.Label(frame, text=f"{i}. {member}", font=("Arial", 18), fg="#154360", bg="#FDFEFE").pack(pady=5)
            nav_frame = tk.Frame(frame, bg="#FDFEFE")
            nav_frame.pack(pady=30)
            if idx > 0:
                tk.Button(nav_frame, text="Previous Team", font=("Arial", 14), bg="#FCF3CF", fg="#7D6608", command=lambda: show_team(idx-1)).pack(side="left", padx=10)
            if idx < len(teams) - 1:
                tk.Button(nav_frame, text="Next Team", font=("Arial", 14), bg="#D4EFDF", fg="#145A32", command=lambda: show_team(idx+1)).pack(side="left", padx=10)
            if final and idx == len(teams) - 1:
                tk.Label(frame, text="All players have been assigned!", font=("Arial", 18, "bold"), fg="#229954", bg="#FDFEFE").pack(pady=30)
                tk.Button(frame, text="Save Teams to File", font=("Arial", 14), bg="#FCF3CF", fg="#7D6608", command=self.save_teams_to_file).pack(pady=10)
                tk.Button(frame, text="Back to Menu", font=("Arial", 14), bg="#F5B7B1", fg="#641E16", command=self.setup_main_menu).pack(pady=10)
            elif not final:
                tk.Button(frame, text="Back to Lottery", font=("Arial", 14), bg="#F5B7B1", fg="#641E16", command=self.lottery_round).pack(pady=10)
        show_team(0)

    def back_to_lottery(self, parent_win):
        for widget in self.root.winfo_children(): widget.destroy()
        if parent_win:
            parent_win.deiconify()

    def save_teams_to_file(self):
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], title="Save Teams")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                for team, members in self.team_assignments.items():
                    f.write(f"{team}\n")
                    f.write(f"{'='*len(team)}\n")
                    for i, member in enumerate(members, 1):
                        f.write(f"  {i}. {member}\n")
                    f.write("\n")
            messagebox.showinfo("Saved", f"Teams saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TeamMakerApp(root)
    root.mainloop()
