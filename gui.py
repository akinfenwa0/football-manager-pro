import tkinter as tk


class FootballManagerApp:

    def __init__(self, root):
        self.root = root

        self.root.title("Football Manager Pro ⚽")
        self.root.geometry("1000x650")

        self.build_dashboard()

    def build_dashboard(self):

        # Header
        header = tk.Frame(self.root, bg="darkgreen", height=60)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="⚽ Football Manager Pro",
            bg="darkgreen",
            fg="white",
            font=("Arial", 14, "bold")
        )
        title.pack(pady=10)

        # Main Area
        main = tk.Frame(self.root)
        main.pack(fill="both", expand=True)

        # Sidebar
        sidebar = tk.Frame(main, bg="lightgrey", width=220)
        sidebar.pack(side="left", fill="y")

        buttons = [
            "Dashboard",
            "Squad",
            "Transfers",
            "Matches",
            "League",
            "Statistics",
            "Settings"
        ]

        for text in buttons:
            button = tk.Button(
                sidebar,
                text=text,
                width=20,
                height=2
            )
            button.pack(pady=5)

        # Content Area
        content = tk.Frame(main)
        content.pack(side="left", fill="both", expand=True)

        dashboard_title = tk.Label(
            content,
            text="Club Dashboard",
            font=("Arial", 20, "bold")
        )
        dashboard_title.pack(pady=20)

        club = tk.Label(
            content,
            text="Club: Arsenal",
            font=("Arial", 14)
        )
        club.pack()

        budget = tk.Label(
            content,
            text="Budget: £500M",
            font=("Arial", 14)
        )
        budget.pack()

        players = tk.Label(
            content,
            text="Players: 0",
            font=("Arial", 14)
        )
        players.pack()
