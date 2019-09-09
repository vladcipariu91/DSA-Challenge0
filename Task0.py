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

"""
 Analysis (Big O):
    Time complexity:
        Reading the texts.csv -> O(n)
        Creating the texts list -> O(n)  
        Reading the calls.csv -> O(n)
        Creating the calls list -> O(n)
        Getting the first text record -> O(1)
            Getting each of the fields from a text record O(1) (3 fields in total)
        Getting the last call record -> O(1)
            Getting each of the fields from a call record O(1) (4 fields in total)
        
        Running the whole code -> O(4n + 9) which can be approximated to O(n)
        Printing the first text record and the last call record are done in constant time O(1)
    
    Space complexity:
        The texts list uses O(n)
        The calls list uses O(n)
        
        For printing the first text record there are 4 more variable allocations -> O(4)
        For printing the last call record there are 5 more variable allocations -> O(5)
        
        For solving the problem the memory allocation is linear O(n)   
"""
