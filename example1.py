from square import Square

# x -> proceso -> 3
# f(x) = x2 -> 2^2

if __name__ == "__main__":
    try:
        side = int(input("Give me the square lenght: "))
        symbol = str(input("Give me the square symbol: "))
        color = str(input("Choose one color [green|cyan|blue]: ")).lower()
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    else:
        sq = Square(side=side, symbol=symbol)
        sq.print_with_color(color=color)
