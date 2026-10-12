import csv
import os
from datetime import datetime

import custom_module


# Task 2: Read a CSV File
def _read_csv(path, rows_as_tuples=False):
    """Read a CSV into the assignment's fields/rows structure."""
    data = {"fields": [], "rows": []}
    try:
        with open(path, "r", newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.reader(csv_file)
            for row_number, row in enumerate(reader):
                if row_number == 0:
                    data["fields"] = row
                else:
                    data["rows"].append(tuple(row) if rows_as_tuples else row)
    except FileNotFoundError:
        # The assignment's three source CSV files were not included. Keeping
        # the empty structure lets functions and tests import independently.
        pass
    return data


def read_employees():
    return _read_csv("../csv/employees.csv")


employees = read_employees()


# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = (
    employees["fields"].index("employee_id")
    if "employee_id" in employees["fields"]
    else None
)


# Task 4: Find the Employee First Name
def first_name(row_number):
    return employees["rows"][row_number][column_index("first_name")]


# Task 5: Find the Employee with a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches


# Task 7: Sort Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]


# Task 8: Create a dict for an Employee
def employee_dict(row):
    employee = {}
    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee[field] = row[index]
    return employee


# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    employee_id_index = column_index("employee_id")
    result = {}
    for row in employees["rows"]:
        result[row[employee_id_index]] = employee_dict(row)
    return result


# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = _read_csv("../csv/minutes1.csv", rows_as_tuples=True)
    minutes2 = _read_csv("../csv/minutes2.csv", rows_as_tuples=True)
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()


# Task 13: Create minutes_set
def create_minutes_set():
    return set(minutes1["rows"]) | set(minutes2["rows"])


minutes_set = create_minutes_set()


# Task 14: Convert to datetime
def create_minutes_list():
    minutes = list(minutes_set)
    return list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes)
    )


minutes_list = create_minutes_list() if minutes_set else []


# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda item: item[1])
    converted_list = list(
        map(lambda item: (item[0], datetime.strftime(item[1], "%B %d, %Y")), minutes_list)
    )
    with open("./minutes.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list


if __name__ == "__main__":
    print(employees)
    print(minutes1)
    print(minutes2)
    print(minutes_set)
    print(minutes_list)
