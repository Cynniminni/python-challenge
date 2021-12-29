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

def count_total_candidate_votes(csv_data: list, candidate_name: str):
    """
    Returns the total number of votes for a given candidate name.
    :return:
    """
    count = 0
    for row in csv_data:
        candidate = row[2]
        if candidate == candidate_name:
            count += 1
    return count

def calculate_vote_percentage(total: int, votes: int):
    """
    Calculates the percentage, given a vote and a total. Formats the result to 3 decimal places.
    :param total:
    :param votes:
    :return:
    """
    result = (votes / total) * 100
    return f"{result:.3f}"

def determine_winner(khan, correy, li, o_tooley):
    """
    Given a list of values for each candidate, determines which candidate has the largest value.
    :param khan:
    :param correy:
    :param li:
    :param o_tooley:
    :return: Name of the candidate with the largest value
    """
    # Determine winner
    biggest_value = max(khan, correy, li, o_tooley)
    if biggest_value == khan:
        return "Khan"
    elif biggest_value == correy:
        return "Correy"
    elif biggest_value == li:
        return "Li"
    elif biggest_value == o_tooley:
        return "O'Tooley"
    else:
        print("ERROR, please check values are all correct")

def print_election_results():
    """
    This is the function that will print the end result for the homework assignment.
    :return:
    """
    # Read csv file and return it as a list
    csv_data = read_csv_file()

    # Get counts for each candidate
    total_votes_count = total_votes(csv_data)
    khan_total_votes = count_total_candidate_votes(csv_data, "Khan")
    correy_total_votes = count_total_candidate_votes(csv_data, "Correy")
    li_total_votes = count_total_candidate_votes(csv_data, "Li")
    o_tooley_total_votes = count_total_candidate_votes(csv_data, "O'Tooley")

    # Get percentages for each candidate
    khan_percentage = calculate_vote_percentage(total_votes_count, khan_total_votes)
    correy_percentage = calculate_vote_percentage(total_votes_count, correy_total_votes)
    li_percentage = calculate_vote_percentage(total_votes_count, li_total_votes)
    o_tooley_percentage = calculate_vote_percentage(total_votes_count, o_tooley_total_votes)

    # Get winner
    winner = determine_winner(khan_percentage, correy_percentage, li_percentage, o_tooley_percentage)

    # Print election results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes_count}")
    print("-------------------------")
    print(f"Khan: {khan_percentage}% ({khan_total_votes})")
    print(f"Correy: {correy_percentage}% ({correy_total_votes})")
    print(f"Li: {li_percentage}% ({li_total_votes})")
    print(f"O'Tooley: {o_tooley_percentage}% ({o_tooley_total_votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")


# Entry point - Where the script begins to execute
if __name__ == "__main__":
    print_election_results()
