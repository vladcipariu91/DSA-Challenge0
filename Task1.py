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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def unique_phone_numbers():
    phone_numbers_set = set()

    for record in texts + calls:
        sending_number = record[0]
        phone_numbers_set.add(sending_number)
        receiving_number = record[1]
        phone_numbers_set.add(receiving_number)

    print("There are " + str(len(phone_numbers_set)) + " different telephone numbers in the records.")


unique_phone_numbers()
