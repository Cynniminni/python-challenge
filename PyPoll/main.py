import os
import csv

def read_csv_file():
    """
    Reads the election_data.csv file and returns it as csv_data. It drops the header row so only the actual data remains.
    :return:
    """
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory, "Resources", "election_data.csv")
    if os.path.exists(file_path):
        # Read csv file and save it as a list of lists
        csv_data = []
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                csv_data.append(row)

        # Drop the header row
        csv_data.pop(0)

        # Return the csv data as a list
        return csv_data
    else:
        raise FileNotFoundError(f"File not found at: {file_path}")

def total_votes(csv_data):
    """
    Returns the total number of votes, which is equivalent to the number of rows in the csv_data.
    :param csv_data:
    :return:
    """
    return len(csv_data)

def get_unique_candidate_list(csv_data):
    """
    Returns the unique list of candidates in a dictionary, where key is the candidate name and value is the number of votes.
    The votes will all be 0 to begin.
    :param csv_data:
    :return:
    """
    candidate_dict = {}
    for row in csv_data:
        candidate_name = row[2]
        if candidate_name not in candidate_dict:
            candidate_dict[candidate_name] = {
                "votes": 0,
                "vote_percentage": ""
            }
    return candidate_dict

def count_candidate_votes(candidate_dict: dict, csv_data: list) -> dict:
    """
    Go through the candidate list and count the number of votes each time it appears.
    :param candidate_dict:
    :param csv_data:
    :return:
    """
    # Go through the csv and get the candidate's name
    for row in csv_data:
        candidate_name = row[2]

        # Add the candidate vote to the dictionary and update it
        for candidate, data in candidate_dict.items():
            if candidate_name == candidate:
                data["votes"] += 1
    return candidate_dict

def calculate_vote_percentage(candidate_dict: dict):
    """
    Calculates the total number of votes and returns a dict containing the vote percentage for each candidate.
    :param candidate_dict:
    :return:
    """
    # Get total vote count by adding all the votes together
    total = 0
    for data in candidate_dict.values():
        total += data["votes"]

    for candidate, data in candidate_dict.items():
        data["vote_percentage"] = f"{round((int(data['votes']) / total) * 100, 2)}%"

    # Add total number of votes to the dictionary
    candidate_dict["total_votes"] = total
    return candidate_dict

def determine_winner(candidate_dict) -> str:
    votes_list = []
    for candidate, data in candidate_dict.items():
        if isinstance(data, dict):
            votes = data["votes"]
            votes_list.append(votes)
    winner = max(votes_list)

    for candidate, data in candidate_dict.items():
        if isinstance(data, dict):
            if winner == data["votes"]:
                winner = candidate
    return winner

def print_election_results():
    """
    This is the function that will print the end result for the homework assignment.
    :return:
    """
    # Read csv file and return it as a list
    csv_data = read_csv_file()

    # Process the candidate dictionary
    candidate_dict = get_unique_candidate_list(csv_data)
    candidate_dict = count_candidate_votes(candidate_dict, csv_data)
    candidate_dict = calculate_vote_percentage(candidate_dict)

    # Save results in a list of strings
    candidate_lines = []
    for candidate, data in candidate_dict.items():
        if isinstance(data, dict):
            candidate_lines.append(
                f"{candidate}: {data['vote_percentage']} ({(data['votes'])})"
            )

    lines = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {candidate_dict['total_votes']}",
        "-------------------------"
    ]
    lines.extend(candidate_lines)
    winner_lines = [
        "-------------------------",
        f"Winner: {determine_winner(candidate_dict)}",
        "-------------------------",
    ]
    lines.extend(winner_lines)

    for line in lines:
        print(line)


# Entry point - Where the script begins to execute
if __name__ == "__main__":
    print_election_results()
