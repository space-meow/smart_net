import re


TIME_REGEX = re.compile(r"[0-2][0-9]:[0-5][0-9]")
DURATION_REGEX = re.compile(r"[0-9]+[SMH]")

def set_alarm():
    
    time_choice = ""
    while not TIME_REGEX.match(time_choice):
        time_choice = str(input("What time: "))
    
    return [time_choice]

def set_timer():

    dur_choice = ""
    while not DURATION_REGEX.match(dur_choice):
        dur_choice= str(input("How long ([0-9]+[SMH])"))
    return [dur_choice]
