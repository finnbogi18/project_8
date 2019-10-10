''' This program gets the amount of rows and the amount of seats in each row,
    then prints out the rows with the seats, then program then asks the user to book a seat
    and after picked that seat is reserved, then the user can pick more seats unless the reserved ones '''

import string 

SEATS = "ABCDEFGHIJ"

def get_list_data():
    """ This function takes in no data. It firts prompts the user to input how many rows it needs.
        Secondly its prompts the user to input how many seats are in each row. """
    total_rows = int(input("Enter number of rows: "))
    seats_in_row = int(input("Enter number of seats in each row: "))
    total_seats = total_rows * seats_in_row
    
    return total_rows, seats_in_row, total_seats

def list_maker(total_rows, total_seats):
    """ Creates a list of available seats given the input from the user """
    seats_list = []
    temp_list = []

    for row in range(1, total_rows + 1):
        temp_list.append(row)
        for seat in range(total_seats):
            temp_list.append(SEATS[seat])
        seats_list.append(temp_list)
        temp_list = []
        
    return seats_list

def seat_picker(seats_list):
    """ Takes the seat list as an input and prompts the user to reserve seats.
        If seats do not exist or the seat is taken the user recieves an error.
        When all the seats are taken, the function stops asking for inputs.  """
    status = True
    counter = 0
    while status is True: # In this loop the function promts the user for an input of a seat and executes acordingly.
        seat = ""
        row, seat = input("Input seat number (row seat): ").split()
        seat = seat.upper()

        if seat in SEATS:
            seat_index = SEATS.find(seat) + 1
        try:
            row = int(row)
            seats_list[row - 1][seat_index]
        except IndexError: # If the seat entered by the user doesn't exist, an error message is printed out.
            print("Seat number is invalid!")
        except UnboundLocalError: # If the seat entered by the user is a invalid input, an error message is printed out.
            print("Seat number is invalid!")
        except ValueError: # If the row is not a number, gives an error.
            print("Seat number is invalid!")
        else:
            
            if seats_list[row - 1][seat_index] == "X": # Replaces a seat letter with an X to show that it has been chosen.
                print("That seat is taken!")
            else:
                seats_list[row - 1][seat_index] = "X"
                counter += 1
                seat_printer(seat_list)
                status_two = True
                while (status_two is True) and (counter < total_seats): # Prompts the user wether or not to choose more seats.
                    more_seats = input("More seats (y/n)? ")
                    more_seats.lower()
                    if more_seats == "n":
                        status = False
                        status_two = False
                    elif more_seats == "y":
                        status_two = False
                    else:
                        print("Invalid input! Please input y(es) or n(o).") # Defensive programming if the user inputs somethin else than y or n
                        
        if counter == total_seats: # Checks if any free seats are left.
            status = False

    return seats_list

def seat_printer(seat_list):
    """ Prints out the aligned seats from the seat list provided. """
    for row in range(len(seat_list)): # For each row in list
        print("{:>2}".format(seat_list[row][0]), end = "   ")
        for seat in range(1, len(seat_list[row])): # For each seat in row
            seats = (len(seat_list[row]) - 1)
            seats_divided = int(seats / 2)
            if seat < seats_divided: # Prints out all but one of the left side of seats.
                print(seat_list[row][seat], end = " ")
            elif seat == seats_divided: # Prints out the last seat of the left side. 
                print(seat_list[row][seat], end = "   ")
            elif seat > seats_divided: # Prints out the right side of seats.
                print(seat_list[row][seat], end = " ")
        print()
            



#  Main program starts here.

total_rows, seats_in_row, total_seats = get_list_data()
seat_list = list_maker(total_rows, seats_in_row)
seat_printer(seat_list)
seat_picker(seat_list)




