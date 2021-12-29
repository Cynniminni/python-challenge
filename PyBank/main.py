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
    # Get all the profits and losses values into a single list
    index = 0
    change_list = []
    for row in csv_data:
        # Calculate the change between this month and last month, if last month exists
        this_months_profit = int(row[1])
        if csv_data[index - 1]:
            last_months_profit = int(csv_data[index - 1][1])
            change = this_months_profit - last_months_profit
            change_list.append(change)
        # Increment index counter by one
        index += 1

    # Drop the first element, csv_data[-1] is the last element and not applicable in this case
    change_list.pop(0)
    return round(sum(change_list) / len(change_list), 2)

def greatest_increase_in_profits(csv_data):
    """
    Return the largest value of the "Profit/Losses" column and its month.
    :param csv_data:
    :return:
    """
    # Get all the profits and losses values into a single list
    index = 0
    month_list = []
    change_list = []
    for row in csv_data:
        # Calculate the change between this month and the next month, if next month exists
        this_month = row[0]
        this_months_profit = int(row[1])
        if csv_data[index - 1]:
            last_months_profit = int(csv_data[index - 1][1])
            change = this_months_profit - last_months_profit
            month_list.append(this_month)
            change_list.append(change)
        # Increment index counter by one
        index += 1

    # Calculate largest change and get its corresponding month
    largest_change = max(change_list)
    largest_change_index = change_list.index(largest_change)
    largest_month = month_list[largest_change_index]

    return f"{largest_month} (${largest_change})"

def greatest_decrease_in_profits(csv_data):
    """
    Return the lowest value of the "Profit/Losses" column and its month.
    :param csv_data:
    :return:
    """
    # Get all the profits and losses values into a single list
    index = 0
    month_list = []
    change_list = []
    for row in csv_data:
        # Calculate the change between this month and the next month, if next month exists
        this_month = row[0]
        this_months_profit = int(row[1])
        if csv_data[index - 1]:
            last_months_profit = int(csv_data[index - 1][1])
            change = this_months_profit - last_months_profit
            month_list.append(this_month)
            change_list.append(change)
        # Increment index counter by one
        index += 1

    # Calculate largest change and get its corresponding month
    smallest_change = min(change_list)
    smallest_change_index = change_list.index(smallest_change)
    smallest_month = month_list[smallest_change_index]

    return f"{smallest_month} (${smallest_change})"

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
