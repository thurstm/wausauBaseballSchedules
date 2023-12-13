# sample py
def main ():
    print ("hello wausau")

if __name__ == "__main__":
    main()

def funcBabeRuth():
    print("get file from sports engine")

def funcLittleLeage():
    print("get file from blue sombrero")

def funcWausauWest():
    print("get file from WSD")
    # Define an empty array to store game data
    games = []

    # Split the schedule data by line
    schedule_data = """DateOpponentTimeLocationLocation Detail
    November 24th, 2023Crandon7:45 PMWausau West High SchoolTurkey Shootout - Court 2
    November 25th, 2023TBD8:00 PMWausau West High SchoolTurkey Shootout - Court 2
    ...""".splitlines()

    # Skip the header
    schedule_data = schedule_data[1:]

    # Loop through each line and parse game data
    for line in schedule_data:
        # Split the line by whitespace
        parts = line.split()

        # Extract game information
        date = parts[0]
        opponent = parts[1]
        time = parts[2]
        location = parts[3]
        detail = " ".join(parts[4:])

        # Create a dictionary for each game
        game = {
            "date": date,
            "opponent": opponent,
            "time": time,
            "location": location,
            "detail": detail,
        }

        # Add the game dictionary to the array
        games.append(game)

    # Print the array of games
    print(games)

def funcWausauEast():
    print("get file from WSD")

def funcNewmanCatholic():
    print("get file from rSchool")

def funcJuniorLegion():
    print("get file from ??")

def funcLegionPost10():
    print("get file from ??")


