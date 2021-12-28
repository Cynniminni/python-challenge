import os
import pandas

def read_budget_csv_file() -> pandas.DataFrame:
    """
    Reads the csv file and loads it into a variable of type DataFrame.
    If the file is not found, raise a FileNotFoundError and end execution.
    :return:
    """
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory, "Resources", "budget_data.csv")
    if os.path.exists(file_path):
        budget_csv_data = pandas.read_csv(file_path)
        return budget_csv_data
    else:
        raise FileNotFoundError(f"File not found at: {file_path}")

def total_months(csv_data):
    """
    Returns the total number of months in the csv file. This is the same as total number of rows.
    :param csv_data:
    :return:
    """
    index = csv_data.index
    total_num_rows = len(index)
    return total_num_rows

def total(csv_data):
    """
    Returns the total sum of the Profit/Losses column.
    :param csv_data:
    :return:
    """
    total_profit_losses = csv_data["Profit/Losses"].sum()
    return total_profit_losses

def average_change(csv_data):
    """
    Return the average value of the "Profit/Losses" column.
    :param csv_data:
    :return:
    """
    column = csv_data["Profit/Losses"]
    average = column.mean()
    format_average = "{:.2f}".format(average)
    return format_average

def greatest_increase_in_profits(csv_data):
    """
    Return the largest value of the "Profit/Losses" column and its month.
    :param csv_data:
    :return:
    """
    column = csv_data["Profit/Losses"]
    max_value = column.max()
    max_index = column.idxmax()
    column = csv_data["Date"]
    date = column.get(max_index)
    return f"{date} (${max_value})"

def greatest_decrease_in_profits(csv_data):
    """
    Return the lowest value of the "Profit/Losses" column and its month.
    :param csv_data:
    :return:
    """
    column = csv_data["Profit/Losses"]
    min_value = column.min()
    min_index = column.idxmin()
    column = csv_data["Date"]
    date = column.get(min_index)
    return f"{date} (${min_value})"

def print_financial_analysis():
    """
    This is the function that will print the end result for the homework assignment.
    :return:
    """
    csv_data = read_budget_csv_file()
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
