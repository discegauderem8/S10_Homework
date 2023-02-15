
def first_computer_move(n, m):
    move = 0
    if n % (m + 1) & n % m <= m & n % (m+1) < 0:
        move = n % (m + 1)
    elif n % m & n % m <= m & n % (m+1) < 0:
        move = n % m
    else:
        move = 1
    new_n = n - move
    with open("amount.txt", "w", encoding="UTF-8") as file:
        file.write(f"{new_n}")
    with open("max_move.txt", "w", encoding="UTF-8") as file:
        file.write(f"{m}")
    return f"Компьютер взял {move} конфет, осталось: {new_n}"


def other_computer_moves(x):
    move = 0
    with open("amount.txt", "r", encoding="UTF-8") as file:
        reader = file.read()
        n = int(reader)
        n = n - x
    if n <= 0:
        return(f"Вы взяли {x} конфет(ы), осталось: {n}. \nИгра окончена, вы победили!")
    with open("max_move.txt", "r", encoding="UTF-8") as file:
        reader = file.read()
        m = int(reader[0])
    if (x <= m):
        if n % (m + 1) & n % m <= m:
            move = n % (m + 1)
        elif n % m & n % m <= m:
            move = n % m
        else:
            move = 1
        new_n = n - move
        if new_n <= 0:
            return(f"Вы взяли {x} конфет(ы)\nКомпьютер взял {move} конфет(ы), осталось: {new_n}. \nИгра окончена, победил компьютер")
        with open("amount.txt", "w", encoding="UTF-8") as file:
            file.write(f"{new_n}")
        return f"Вы взяли {x} конфет(ы)\nКомпьютер взял {move} конфет(ы), осталось: {new_n}"
    else:
        return f"Вы взяли неправильное число конфет, попробуйте еще раз"

