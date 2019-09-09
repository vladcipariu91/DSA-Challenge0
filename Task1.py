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

"""
 Analysis (Big O):
    Time complexity:
        We need to iterate over both the texts and calls -> O(n + m) where n is the number of texts
        and m is the number of calls. This is an overall O(n)
        
    Space complexity:
        We create a set that will store the unique numbers since a set doesn't contains duplicates.
        The set will have a space complexity of O(n)
        Doing texts + calls creates a new list of size n + m (n is the number of texts
        and m is the number of calls) this results in a list with a space complexity of O(n).
        
        The approximation of the space complexity is O(n).        
"""
