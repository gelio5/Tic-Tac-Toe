field = list(' ' * 9)
win_line = ''
win_counter = 0


def show_field():
    print(f'---------\n'
          f'| {field[0]} {field[1]} {field[2]} |\n'
          f'| {field[3]} {field[4]} {field[5]} |\n'
          f'| {field[6]} {field[7]} {field[8]} |\n'
          f'---------')


def winner():
    global win_counter
    global win_line
    if field[0] == field[1] == field[2] and (field[0] == 'X' or field[0] == 'O'):
        win_line = 'h1'
        win_counter += 1
    if field[3] == field[4] == field[5] and (field[3] == 'X' or field[3] == 'O'):
        win_line = 'h2'
        win_counter += 1
    if field[6] == field[7] == field[8] and (field[6] == 'X' or field[6] == 'O'):
        win_line = 'h3'
        win_counter += 1
    if field[0] == field[3] == field[6] and (field[0] == 'X' or field[0] == 'O'):
        win_line = 'v1'
        win_counter += 1
    if field[1] == field[4] == field[7] and (field[1] == 'X' or field[1] == 'O'):
        win_line = 'v2'
        win_counter += 1
    if field[2] == field[5] == field[8] and (field[2] == 'X' or field[2] == 'O'):
        win_line = 'v3'
        win_counter += 1
    if field[0] == field[4] == field[8] and (field[0] == 'X' or field[0] == 'O'):
        win_line = 'd1'
        win_counter += 1
    if field[2] == field[4] == field[6] and (field[2] == 'X' or field[2] == 'O'):
        win_line = 'd2'
        win_counter += 1
    if win_counter == 0 and field.count(' ') == 0:
        print('Draw')
        exit()

    if win_line == 'h1' or win_line == 'v1' or win_line == 'd1':
        print(f'{field[0]} wins')
        exit()
    elif win_line == 'h2' or win_line == 'v2' or win_line == 'd2':
        print(f'{field[4]} wins')
        exit()
    elif win_line == 'h3' or win_line == 'v3':
        print(f'{field[8]} wins')
        exit()


def input_coordinate():
    global field
    column, row = input('Enter the coordinates: > ').split()
    if not (column.isdecimal() and row.isdecimal()):
        print('You should enter numbers!')
        input_coordinate()
    else:
        column = int(column)
        row = int(row)
        if row > 3 or row < 1 or column > 3 or column < 1:
            print('Coordinates should be from 1 to 3!')
            input_coordinate()
        else:
            coordinates = {'13': 0, '23': 1, '33': 2,
                           '12': 3, '22': 4, '32': 5,
                           '11': 6, '21': 7, '31': 8}
            if field[coordinates[str(column) + str(row)]] == ' ':
                if field.count(' ') % 2 == 1:
                    field[coordinates[str(column) + str(row)]] = 'X'
                else:
                    field[coordinates[str(column) + str(row)]] = 'O'
            else:
                print('This cell is occupied! Choose another one!')
                input_coordinate()


show_field()
while True:
    input_coordinate()
    show_field()
    winner()



