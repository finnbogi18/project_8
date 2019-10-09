''' This program gets the amount of rows and the amount of seats in each row,
    then prints out the rows with the seats, then program then asks the user to book a seat
    and after picked that seat is reserved, then the user can pick more seats unless the reserved ones '''

def seat_picker():
    ''' Prompts the user for a seat number '''
    row, seat = input("Input seat number: ").split()
    row = int(row)
    return row, seat

def get_list_data():
    total_rows = int(input("Enter number of rows: "))
    seats_in_row = int(input("Enter number of seats in each row: "))

    return total_rows, seats_in_row

def list_maker(total_rows, total_seats):






#  Main program starts here.

total_rows, seats_in_row = get_list_data()
seat_list = list_maker(total_rows, seats_in_row)


