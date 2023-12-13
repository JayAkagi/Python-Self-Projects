import random

symbol_prize = {
    "[%]": 5,
    "[A]": 10,
    "[$]": 20,
    "[o]": 15,
    "[*]": 25,
    "[X]": 30,
    "[7]": 50
    }
symbols = ["[%]","[A]","[A]","[$]","[o]","[*]","[X]","[7]","[X]",
           "[o]","[A]","[%]","[*]","[$]","[%]","[*]","[$]",
           "[%]","[o]","[A]","[A]","[X]","[*]","[%]","[%]","[A]","[7]","[$]","[o]",
           "[%]","[$]","[A]","[o]","[%]","[%]"]

slot1 = ["[]", "[]", "[]"]
slot2 = ["[]", "[]", "[]"]
slot3 = ["[]", "[]", "[]"]

slot_line_X = [slot1, slot2, slot3]

player_wallet = int(input("Enter wallet amount: "))
coins = 0
allow_play = True

while allow_play:
    print(f"Wallet: {player_wallet}\n"
          f"Coins: {coins}\n")
    user_input = int(input("Enter 1 to spin, 2 to withdraw, 3 to deposit"))
    winning_symbol = None

    if user_input == 1:
        if coins > 5:
            coins -= 10

            spin1 = random.randint(0, len(symbols) - 1)
            spin2 = random.randint(0, len(symbols) - 1)
            spin3 = random.randint(0, len(symbols) - 1)

            for i in range(3):
                slot_line_X[i][0] = symbols[(spin1 + i) % len(symbols)]

            for i in range (3):
                slot_line_X[i][1] = symbols[(spin2 + i) % len(symbols)]

            for i in range(3):
                slot_line_X[i][2] = symbols[(spin3 + i) % len(symbols)]

            for line in slot_line_X:
                print("".join(line))

            first_row = all(slot_line_X[0][i] == slot_line_X[0][0] for i in range(1, 3))
            second_row = all(slot_line_X[1][i] == slot_line_X[1][0] for i in range(1, 3))
            third_row = all(slot_line_X[2][i] == slot_line_X[2][0] for i in range(1, 3))
            diagonal_left_right = all(slot_line_X[i][i] == slot_line_X[0][0] for i in range(1, 3))
            diagonal_right_left = all(slot_line_X[i][2 - i] == slot_line_X[0][2] for i in range(1,3))

            if first_row or second_row or third_row or diagonal_right_left or diagonal_left_right:
                if first_row or diagonal_left_right:
                    winning_symbol = slot_line_X[0][0]
                elif second_row:
                    winning_symbol = slot_line_X[1][0]
                elif third_row:
                    winning_symbol = slot_line_X[2][0]
                elif diagonal_right_left:
                    winning_symbol = slot_line_X[0][2]

            if winning_symbol is not None:
                prize = symbol_prize[winning_symbol]
                print(f"You win {prize}!")
                coins += prize
            else:
                print("No winning combination.")
        else:
            game_over_status = True
            game_over = int(input("You dont have enough coins. Press 1 to add more coins. Press 2 to stop playing"))
            while game_over_status:
                if game_over == 1:
                    deposit_coins = int(input("Enter amount of coins to deposit: "))
                    coins += deposit_coins
                    player_wallet -= deposit_coins
                    game_over_status = False
                elif game_over == 2:
                    print("Thanks for playing!")
                    allow_play = False
                    game_over_status = False
                else:
                    print("Invalid input. Try again")

    elif user_input == 2:
        withdraw_coins = int(input("Enter amount to withdraw: "))
        coins -= withdraw_coins
        player_wallet += withdraw_coins

    elif user_input == 3:
        deposit_coins = int(input("Enter amount of coins to deposit: "))
        coins += deposit_coins
        player_wallet -= deposit_coins








# x = symbols.count("[X]")
# percent = symbols.count("[%]")
# dollar = symbols.count("[$]")
# o = symbols.count("[o]")
# star = symbols.count("[*]")
# seven = symbols.count("[7]")
# A = symbols.count("[A]")
# print(f"% = {percent}, A = {A}, $ = {dollar}, o = {o}, * = {star},"
#       f"X = {x}, 7 = {seven}")