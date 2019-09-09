"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_no_duration = {}


def max_time_on_phone():
    for record in calls:
        calling_phone_no = record[0]
        receiving_phone_no = record[1]
        duration = record[3]

        update_duration_record(calling_phone_no, duration)
        update_duration_record(receiving_phone_no, duration)

    print_max_on_phone()


def update_duration_record(phone_no, duration):
    if phone_no_duration.get(phone_no) is None:
        phone_no_duration[phone_no] = int(duration)
    else:
        phone_no_duration[phone_no] += int(duration)


def print_max_on_phone():
    phone_no = ""
    max_time = 0
    for number, duration in phone_no_duration.items():
        if duration > max_time:
            phone_no = number
            max_time = duration

    print(phone_no + " spent the longest time, " + str(max_time) + " seconds, on the phone during September 2016.")


max_time_on_phone()

"""
 Analysis (Big O):
    Time complexity:
        First we need to iterate over the entire list of call records. This results in a time complexity of
        O(call_records) which can be approximated to O(n).
        Second we iterate over the dictionary containing all the unique phone numbers and their associated time 
        spent on calls which results in O(n).
        To run the whole program we have a time complexity of O(2n) which we'll approximate to O(n).        

    Space complexity:
        In order to determine the unique phone numbers and associate the time spent in calls to them we need a dictionary.
        The space complexity for this is roughly O(n).
        
        The total space complexity for the program is also O(n).
"""
