import os

'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 : 
            start : 08:00, 
			end : 09:00,
			title : Eye doctor
			
            start : 12:30,
			end : 13:00,
			title : lunch with sid
            
			start : 18:00,
			end : 19:00, 
			title : dinner with jane
        2018-10-29 : 
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car
			
            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway
			
            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 : 
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me


def command_add(date, start_time, end_time, title, calendar):
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    """

    # YOUR CODE GOES HERE
    if start_time > end_time or start_time < 0 or start_time > 24 or end_time < 0 or end_time > 24:
        return False

    if date not in calendar:
        calendar[date] = []

    index = len(calendar[date])
    for i, event in enumerate(calendar[date]):
        if start_time<event["start"]:
            index = i
            break
    calendar[date].insert(index, {"start": int(start_time), "end": int(end_time), "title": title})




    #calendar[date].append({"start": int(start_time), "end": int(end_time), "title": title})

    return True

    # pass


def command_show(calendar):
    r"""
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\n2018-05-06 : \n    start : 19:00,\n    end : 23:00,\n    title : Sid's birthday\n2018-02-10 : \n    start : 12:00,\n    end : 23:00,\n    title : Change oil in blue car\n\n    start : 20:00,\n    end : 22:00,\n    title : dinner with Jane\n2018-01-15 : \n    start : 08:00,\n    end : 09:00,\n    title : lunch with sid\n\n    start : 11:00,\n    end : 13:00,\n    title : Eye doctor\n2017-12-22 : \n    start : 05:00,\n    end : 08:00,\n    title : Fix tree near front walkway\n\n    start : 13:00,\n    end : 15:00,\n    title : Get salad stuff"
    """

    def get_time(event):
        return event["start"]

    output = ""
    sorted_calendar = sorted(calendar, reverse=True)
    for key in sorted_calendar:
        output += "\n" + key + " : "
        calendar[key].sort(key=get_time)
        for i, event in enumerate(calendar[key]):
            output += "\n    start : {:0>2d}".format(event["start"]) + ":00,\n    end : {:0>2d}".format(
                event["end"]) + ":00,\n    title : " + event["title"]
            if i+1 != len(calendar[key]):
                output+= "\n"


    return output


# pass


def command_delete(date, start_time, calendar):
    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True

    """

    # YOUR CODE GOES HERE

    if not date in calendar:
        return date + " is not a date in the calendar"

    for i, event in enumerate(calendar[date]):
        if event["start"] == start_time:
            del calendar[date][i]
            if len(calendar[date]) == 0:
                del calendar[date]
            return True

    return 'There is no event with start time of ' + str(start_time) + ' on date ' + date + ' in the calendar'

    pass


# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

"""
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

"""


def save_calendar(calendar):
    """
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists. The calendar events do not have
    to be saved in any particular order

    The format of calendar.txt is the following:

    date_1:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_2:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_n:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n

    Example: The following calendar...



        2018-03-13 : 
                start : 13:00,
                end : 13:00,
                title : Have fun
        2018-03-11 : 
                start : 10:00,
                end : 12:00,
                title : Another event on this date

                start : 14:00,
                end : 16:00,
                title : CSCA08 test 2
        2018-02-28 : 
                start : 11:00,
                end : 12:00,
                title : Python class

     appears in calendar.txt as ...

    2018-03-13:13-13 Have fun
    2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
    2018-02-28:11-12 Python class

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    """
    # YOUR CODE GOES HERE
    output = ""
    reversed_calendar={}
    for key in sorted(calendar.keys(),reverse=True):
        reversed_calendar[key] = calendar[key]
    for key in reversed_calendar:
        output += key + ":"
        for i, event in enumerate(reversed_calendar[key]):
            output += "{:0>2d}".format(event["start"]) + "-" + "{:0>2d}".format(event["end"]) + " " + event["title"]
            if not i + 1 == len(reversed_calendar[key]):
                output += "\t"
        output += "\n"
    f = open("calendar.txt", "w")
    f.write(output)
    f.close()
    return True

    #pass


def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.

    '''

    # YOUR CODE GOES HERE
    import os
    calendar = {}
    file = 'calendar.txt'
    if os.path.exists(file):
        fileStream = open(file, "r")
        lines = fileStream.readlines()
        for line in lines:
            lineColonSplit = line.split(':')
            date = lineColonSplit[0]
            events = lineColonSplit[1]
            calendar[date] = []
            eventsArray = events.split('\t')
            for parts in eventsArray:
                activity = {}
                colonIndex = parts.index('-')
                start_time = parts[0:colonIndex]
                rest = parts[colonIndex + 1:len(parts)]
                titleSpaceIndex = rest.index(' ')
                end_Time = rest[0:titleSpaceIndex]
                title = rest[titleSpaceIndex + 1:len(rest)]
                activity["start"] = int(start_time)
                activity["end"] = int(end_Time)
                title=title.rstrip("\n")
                activity["title"] = title
                calendar[date].append(activity)
        fileStream.close()

    else:
        fileStream = open(file, 'w')
        fileStream.close()
    return calendar
    pass


# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''
    return command == "add" or command == "delete" or command == "quit" or command == "help" or command == "show"

    # YOUR CODE GOES HERE
    # pass


def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE
    parts = date.split("-")
    if len(parts) != 3:
        return False
    if len(parts[0]) != 4 or not is_natural_number(parts[0]):
        return False
    if len(parts[1]) != 2 or not is_natural_number(parts[1]) or int(parts[1]) == 0 or int(parts[1]) > 12:
        return False
    if len(parts[2]) != 2 or not is_natural_number(parts[2]) or int(parts[2]) == 0 or int(parts[2]) > 31:
        return False
    return True

    # pass


def is_natural_number(str):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE
    count = 0
    for s in str:
        count += 1
        if (s < '0') or (s > '9'):
            return False;
    return count != 0;
    pass


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', '14']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE
    parts = line.split(" ")

    if parts[0] == "help":
        return ["help"]
    if not is_command(parts[0]):
        return ['help']

    if parts[0] == "add":
        if len(parts) >= 5:
            y = ""
            for x in range(4, len(parts)):
                y += parts[x] + " "
            y = y.rstrip()
            if is_calendar_date(parts[1]):
                if is_natural_number(parts[2]) and is_natural_number(parts[3]):
                    return [parts[0], parts[1], int(parts[2]), int(parts[3]), y]
                else:
                    return ['error', 'not valid number']
            else:
                return ['error', 'not a valid calendar date']
        else:
            return ["error", "add DATE START_TIME END_TIME DETAILS"]

    if parts[0] == "show":
        if len(parts) == 1:
            return parts
        else:
            return ["error", "show"]

    if parts[0] == "delete":
        if len(parts) == 3:
            if is_calendar_date(parts[1]):
                if is_natural_number(parts[2]):
                    parts[2] =int(parts[2])
                    return parts
                else:
                    return ["error", "not a valid event start time"]
            else:
                return ["error", "not a valid calendar date"]
        else:
            return ["error", "delete DATE START_TIME"]

    if parts[0] == "quit":
        return ["quit"]
    #pass



if __name__ == "__main__":
    import doctest

    doctest.testmod()
