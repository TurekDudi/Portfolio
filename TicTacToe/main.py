import random
import time

def main():
    while True:
        used = []
        field = ['0','1','2','3','4','5','6','7','8']
        ai = random.sample(field,8)
        players = input("1)single player \n2)Two players\n3)Exit\n")
        if players == '3':
            break
        while True: 
            if check_win(field) != False:
                print(f"player {check_win(field)} win")
                break
            print_field(field)
            while True:
                try:
                    first_player = int(input("choose position: "))
                    used.append(str(first_player))
                    field[first_player] = 'X'
                    break
                except:
                    pass
            print_field(field)
            if players =='2':
                second_player = int(input("choose position: "))
 
            elif players =='1':
                time.sleep(1)
                for letter in used:
                    if letter in ai:
                        ai.remove(letter)
                second_player = int(ai.pop())
            field[second_player] = 'O'
            



def check_win(field):
    posibilities = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in posibilities:
        if field[a] == field[b] == field[c] == 'X':
            return 'X'
        elif field[a] == field[b] == field[c] == 'O':
            return 'O'
    return False
    


def print_field(field):
    print(f"{field[0]} | {field[1]} | {field[2]}\n"
        "- - - - -\n"
        f"{field[3]} | {field[4]} | {field[5]}\n"
        "- - - - -\n"
        f"{field[6]} | {field[7]} | {field[8]}\n")



if __name__ == "__main__":
    main()
