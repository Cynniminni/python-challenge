import os
import csv

def read_csv_file():
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory, "Resources", "budget_data.csv")
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

def total_months(csv_data):
    """
    Returns the total number of months in the csv file. This is the same as total number of rows.
    :param csv_data:
    :return:
    """
    return len(csv_data)

def total(csv_data):
    """
    Returns the total sum of the Profit/Losses column.
    :param csv_data:
    :return:
    """
    total_profit_losses = 0
    for row in csv_data:
        profit_losses = int(row[1])
        total_profit_losses += profit_losses
    return total_profit_losses

def average_change(csv_data):
    """
    Return the average value of the "Profit/Losses" column.
    :param csv_data:
    :return:
    """
    total_profit_losses = total(csv_data)
    total_months_count = total_months(csv_data)
    return total_profit_losses / total_months_count

def greatest_increase_in_profits(csv_data):
    """
    Return the largest value of the "Profit/Losses" column and its month.
    :param csv_data:
    :return:
    """
    # Get all the profits and losses values into a single list
    profit_losses_list = []
    for row in csv_data:
        profit_losses = int(row[1])
        profit_losses_list.append(profit_losses)

    # Get the largest profit value and its corresponding index
    max_value = max(profit_losses_list)
    max_index = profit_losses_list.index(max_value)

    # Get the date using the index
    date = csv_data[max_index][0]
    return f"{date} (${max_value})"

def greatest_decrease_in_profits(csv_data):
    """
    Return the lowest value of the "Profit/Losses" column and its month.
    :param csv_data:
    :return:
    """
    # Get all the profits and losses values into a single list
    profit_losses_list = []
    for row in csv_data:
        profit_losses = int(row[1])
        profit_losses_list.append(profit_losses)

    # Get the largest profit value and its corresponding index
    min_value = min(profit_losses_list)
    min_index = profit_losses_list.index(min_value)

    # Get the date using the index
    date = csv_data[min_index][0]
    return f"{date} (${min_value})"

def print_financial_analysis():
    """
    This is the function that will print the end result for the homework assignment.
    :return:
    """
    csv_data = read_csv_file()
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months(csv_data)}")
    print(f"Total: ${total(csv_data)}")
    print(f"Average Change: ${average_change(csv_data)}")
    print(f"Greatest Increase in Profits: {greatest_increase_in_profits(csv_data)}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits(csv_data)}")


# Entry point - Where the script begins to execute
if __name__ == "__main__":
    print_financial_analysis()
