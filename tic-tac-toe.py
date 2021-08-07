print("Tic - Tac -Toe")
print("player 1 please choose one 'x' or 'o'")
player_1 = input()
if player_1 == "x":
    player_2 = "o"
    print("player 2 got:o")
else:
    player_2="x"
    print("player 1 got:o")

mylist = ["", "", "", "", "", "", "", "", "", ""]


def print_board():
    print(mylist[0] + "\t|" + mylist[1] + "\t|" + mylist[2])
    print("--------------")
    print(mylist[3] + "\t|" + mylist[4] + "\t|" + mylist[5])
    print("--------------")
    print(mylist[6] + "\t|" + mylist[7] + "\t|" + mylist[8])

def intake():
    while True:

        intake_1 = input("enter the position player 1:")
        if mylist[int(intake_1)-1]=='':
            mylist[int(intake_1)-1] = player_1
            print_board()
            if mylist[0] == player_1 and mylist[1] == player_1 and mylist[2] == player_1 or mylist[0] == player_1 and \
                    mylist[3] == player_1 and mylist[6] == player_1 or mylist[0] == player_1 and mylist[
                4] == player_1 and \
                    mylist[8] == player_1 or mylist[1] == player_1 and mylist[4] == player_1 and mylist[
                7] == player_1 or \
                    mylist[2] == player_1 and mylist[5] == player_1 and mylist[8] == player_1 or mylist[
                2] == player_1 and \
                    mylist[4] == player_1 and mylist[6] == player_1 or mylist[3] == player_1 and mylist[
                4] == player_1 and \
                    mylist[5] == player_1 or mylist[6] == player_1 and mylist[7] == player_1 and mylist[8] == player_1:

                print("player 1 wins!")
                break
            intake_2 = input("enter position player 2:")
            if mylist[int(intake_2)-1] == '':
                mylist[int(intake_2)-1] = player_2
                print_board()
                if mylist[0] == player_2 and mylist[1] == player_2 and mylist[2] == player_2 or mylist[
                    0] == player_2 and \
                        mylist[3] == player_2 and mylist[6] == player_2 or mylist[0] == player_2 and mylist[
                    4] == player_2 and \
                        mylist[8] == player_2 or mylist[1] == player_2 and mylist[4] == player_2 and mylist[
                    7] == player_2 or \
                        mylist[2] == player_2 and mylist[5] == player_2 and mylist[8] == player_2 or mylist[
                    2] == player_2 and \
                        mylist[4] == player_2 and mylist[6] == player_2 or mylist[3] == player_2 and mylist[
                    4] == player_2 and \
                        mylist[5] == player_2 or mylist[6] == player_2 and mylist[7] == player_2 and mylist[
                    8] == player_2:
                    print("player 2 wins!")
                    break


while True:
    mylist = ["", "", "", "", "", "", "", "", "", ""]
    print_board()
    intake()
    x=input("wanna play game again?")
    if x =="yes":
        continue
    else:
        break