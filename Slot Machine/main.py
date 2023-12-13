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
symbols = ["[%]","[A]","[$]","[o]","[*]","[X]","[7]","[X]",
           "[o]","[A]","[%]","[*]","[$]","[%]","[*]","[$]",
           "[%]","[o]","[A]","[X]","[*]","[%]","[A]","[7]","[$]","[o]",
           "[%]","[$]","[A]","[o]","[%]"]

slot1 = ["[]", "[]", "[]"]
slot2 = ["[]", "[]", "[]"]
slot3 = ["[]", "[]", "[]"]

slot_line_X = [slot1, slot2, slot3]


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
    if first_row and diagonal_left_right:
        winning_symbol = slot_line_X[0][0]
    elif second_row:
        winning_symbol = slot_line_X[1][0]
    elif third_row:
        winning_symbol = slot_line_X[2][0]
    elif diagonal_right_left:
        winning_symbol = slot_line_X[0][2]

    prize = symbol_prize[winning_symbol]
    print(f"You win {prize}!")
else:
    print("No winning combination.")






# x = symbols.count("[X]")
# percent = symbols.count("[%]")
# dollar = symbols.count("[$]")
# o = symbols.count("[o]")
# star = symbols.count("[*]")
# seven = symbols.count("[7]")
# A = symbols.count("[A]")
# print(f"% = {percent}, A = {A}, $ = {dollar}, o = {o}, * = {star},"
#       f"X = {x}, 7 = {seven}")