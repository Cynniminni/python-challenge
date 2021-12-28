import os
import pandas

def read_election_csv_file() -> pandas.DataFrame:
    """
    Reads the csv file and loads it into a variable of type DataFrame.
    If the file is not found, raise a FileNotFoundError and end execution.
    :return:
    """
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory, "Resources", "election_data.csv")
    if os.path.exists(file_path):
        csv_data = pandas.read_csv(file_path)
        return csv_data
    else:
        raise FileNotFoundError(f"File not found at: {file_path}")

def total_votes(csv_data):
    pass

def khan_total_votes(csv_data):
    pass

def correy_total_votes(csv_data):
    pass

def li_total_votes(csv_data):
    pass

def o_tooley_total_votes(csv_data):
    pass

def winner(khan, correy, li, o_tooley):
    pass

def print_election_results():
    """
    This is the function that will print the end result for the homework assignment.
    :return:
    """
    csv_data = read_election_csv_file()
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: ")
    print("-------------------------")
    print(f"Khan: ")
    print(f"Correy: ")
    print(f"Li: ")
    print(f"O'Tooley: ")
    print("-------------------------")
    print(f"Winner: ")
    print("-------------------------")


# Entry point - Where the script begins to execute
if __name__ == "__main__":
    print_election_results()
