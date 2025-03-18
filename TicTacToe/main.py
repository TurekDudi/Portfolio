


def main():
    
    field = ['0','1','2','3','4','5','6','7','8']

    while True:
        players = input("1)single player \n2)Two players\n")
        if players == '2':    
            print_field(field)

            first_player = int(input("choose position: "))

            field[first_player] = 'X'

            print_field(field)

            second_player = int(input("choose position: "))

            field[second_player] = 'O'
        elif players == '1':
            pass
        else: 
            print('choose 1 or 2')


def check_win(player):
    pass


def print_field(field):
    print(f"{field[0]} | {field[1]} | {field[2]}\n"
        "- - - - -\n"
        f"{field[3]} | {field[4]} | {field[5]}\n"
        "- - - - -\n"
        f"{field[6]} | {field[7]} | {field[8]}\n")



if __name__ == "__main__":
    main()
