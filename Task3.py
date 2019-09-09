"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# Part A
def get_prefixes_called_from_bangalore():
    prefixes_called_from_bangalore = set()

    for record in calls:
        calling_no = record[0]
        if is_phone_from_bangalore(calling_no):
            receiving_no = record[1]

            if is_fixed_line(receiving_no):
                prefixes_called_from_bangalore.add(get_fixed_line_area_code(receiving_no))

            if is_mobile_number(receiving_no):
                prefixes_called_from_bangalore.add(get_mobile_number_prefix(receiving_no))

            if is_telemarketer(receiving_no):
                prefixes_called_from_bangalore.add(get_telemarketer_prefix())

    sorted_prefixes = sorted(prefixes_called_from_bangalore)
    print("The numbers called by people in Bangalore have codes:")
    for prefix in sorted_prefixes:
        print(prefix)


# Part B
def get_percentage_of_calls_from_bangalore_to_bangalore():
    total_calls = 0
    calls_to_bangalore = 0

    for record in calls:
        calling_no = record[0]
        receiving_no = record[1]

        if is_phone_from_bangalore(calling_no) and is_phone_from_bangalore(receiving_no):
            calls_to_bangalore += 1

        total_calls += 1

    percentage = (float(calls_to_bangalore) / total_calls) * 100
    print("{:.{}f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
        percentage, 2))


def is_phone_from_bangalore(phone_no):
    return is_fixed_line(phone_no) and phone_no.find("(080)") == 0


def is_fixed_line(phone_no):
    return "(" in phone_no


def get_fixed_line_area_code(phone_no):
    parts = phone_no.split(")")
    return parts[0] + ")"


def is_mobile_number(phone_no):
    return " " in phone_no


def get_mobile_number_prefix(phone_no):
    return phone_no[0:4]


def is_telemarketer(phone_no):
    return phone_no.find("140") == 0


def get_telemarketer_prefix():
    return "140"


get_prefixes_called_from_bangalore()
get_percentage_of_calls_from_bangalore_to_bangalore()
