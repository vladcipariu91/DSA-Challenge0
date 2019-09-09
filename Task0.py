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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def first_record_texts():
    first_text = texts[0]
    # assuming that all records are correct (have 3 entries)
    incoming_no = first_text[0]
    answering_no = first_text[1]
    timestamp = first_text[2]

    print("First record of texts, " + incoming_no + " texts " + answering_no + " at time " + timestamp)


def last_record_calls():
    last_call = calls[-1]
    # assuming that all records are correct (have 4 entries)
    incoming_no = last_call[0]
    answering_no = last_call[1]
    timestamp = last_call[2]
    duration = last_call[3]

    print(
        "Last record of calls, " + incoming_no +
        " calls " + answering_no +
        " at time " + timestamp +
        ", lasting " + duration +
        " seconds"
    )


first_record_texts()
last_record_calls()
