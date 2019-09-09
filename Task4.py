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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def get_possible_telemarketers():
    only_outgoing = set()
    other = set()

    for record in calls:
        calling_no = record[0]
        only_outgoing.add(calling_no)

        receiving_no = record[1]
        other.add(receiving_no)

    for record in texts:
        sending_no = record[0]
        other.add(sending_no)

        receiving_no = record[1]
        other.add(receiving_no)

    telemarketers = sorted(only_outgoing - other)

    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers:
        print(telemarketer)


get_possible_telemarketers()
