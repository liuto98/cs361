print("Welcome to the NBA Stats Command Line Application")


class InputDetection(Exception):
    pass


class StatReturn:
    def __init__(self, year, player, ppg, assists, rebounds):
        self.year = year
        self.player = player
        self.ppg = ppg
        self.assists = assists
        self.rebounds = rebounds

    def __str__(self):
        return f"{self.player}, {self.ppg}, {self.assists}, {self.rebounds}"


user_stat = StatReturn(None, None, None, None, None)


def get_year():
    print("We are viewing per-game stats by year.")
    print("What year would you like to view? You can choose any year between 1950-2023")
    year_input = input("Format (yyyy), no spaces: ")
    user_stat.year = year_input


def get_player():
    print("Which player would you like stats for? Enter -b to go back at any time.")
    print("You can also enter -d to print a dictionary of available players.")
    while True:
        try:
            player_input = input("Format (First Last), space between first and last name: ")

            if player_input == "-d":
                raise InputDetection

            if player_input == "-b":
                get_year()
                get_player()

        except InputDetection:
            print("Printing available players: ")

        else:
            break

    if player_input != "-d" or "-b":
        user_stat.player = player_input

def advanced_stats():
    pass


def return_stats():
    print("Basic stats such as points, assists, and rebounds will be shown.")
    print("Optionally, you can enter -a for advanced statistics. Enter -b to go back to player selection.")
    print("You can also enter -h for help regarding advanced statistics.")
    while True:
        try:
            user_input = input("Enter an command (optional): ")

            if user_input == "-b":
                get_player()
                return_stats()

            if user_input == "-a":
                raise InputDetection

            if user_input == "-h":
                print("Insert stats descriptions here.")

        except InputDetection:
            advanced_stats()

        else:
            break


if __name__ == "__main__":
    get_year()
    get_player()
    return_stats()
