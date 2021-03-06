import Calendar as calendar


# ----------------------------------------------------------------------------
# Functions dealing with the user. This is the calendar application.
# Please do use input and print as needed in order to provide a
# nice and meaningful user interaction with your application.
# ----------------------------------------------------------------------------


def user_interface():
    '''
    Load calendar.txt and then interact with the user. The user interface
    operates as follows, the text after command: is the command entered by the
    user.
    calendar loaded
    command: add 2017-10-21 9 10 budget meeting
    added
    command: add 2017-10-22 6 7 go to the gym
    added
    command: add 2017-10-23 5 6 go to the gym
    added
    command: add 2017-11-01 15 16 Make sure to submit csc108 assignment 2
    added
    command: add 2017-12-02 16 17 Make sure to submit csc108 assignment 3
    added
    command: add 2017-11-06 8 10 Term test 2
    added
    command: add 2017-10-29 7 8 Get salad stuff,lettuce, red peppers, green peppers
    added
    command: add 2017-11-06 19 22 Sid's birthday
    added
    command: show


        2017-12-02 : 
            start : 16:00,
            end : 17:00,
            title: Make sure to submit csc108 assignment 3
        2017-11-06 : 
            start : 8:00,
            end : 10:00,
            title: Term test 2

            start : 19:00,
            end : 22:00,
            title: Sid's birthday
        2017-11-01 : 
            start : 15:00,
            end : 16:00,
            title: Make sure to submit csc108 assignment 2
        2017-10-29 : 
            start : 7:00,
            end : 8:00,
            title: Get salad stuff, leuttice, red peppers, green peppers
        2017-10-23 : 
            start : 5:00,
            end : 6:00,
            title: go to the gym
        2017-10-22 : 
            start : 6:00,
            end : 7:00,
            title : go to the gym
        2017-10-21 : 
            start : 9:00,
            end : 10:00,
            title : budget meeting


    command: delete 2017-10-29 7
    deleted
    command: delete 2015-12-03 9
    2015-12-03 is not a date in the calendar
    command: delete 2017-12-02 16
    deleted
    command: show
	
        2017-11-06 : 
            start : 8:00,
            end : 10:00,
            title: Term test 2

            start : 19:00,
            end : 22:00,
            title: Sid's birthday
        2017-11-01 : 
            start : 15:00,
            end : 16:00,
            title: Make sure to submit csc108 assignment 2
        2017-10-23 : 
            start : 5:00,
            end : 6:00,
            title: go to the gym
        2017-10-22 : 
            start : 6:00,
            end : 7:00,
            title : go to the gym
        2017-10-21 : 
            start : 9:00,
            end : 10:00,
            title : budget meeting
    command: quit
    calendar saved

    :return: None
    '''
    # Your code goes here
    loaded_calendar = calendar.load_calendar()
    print("calendar loaded, type help for list of commands")

    command = ""
    while (command != "quit"):
        command = input("command:")
        list = calendar.parse_command(command)
        if list[0] == "error":
            print(list[1])
        if list[0] == "add":
            calendar.command_add(list[1], list[2], list[3], list[4], loaded_calendar)
            print("added")
        if list[0] == "show":
            print(calendar.command_show(loaded_calendar))
        if list[0] == "delete":
            delete_output = calendar.command_delete(list[1], list[2], loaded_calendar)
            if delete_output != True:
                print(delete_output)
            else:
                print("deleted")
        if list[0] == "help":
            print(calendar.command_help())

    calendar.save_calendar(loaded_calendar)
    print("calendar saved")

    # pass


if __name__ == "__main__":
    user_interface()
