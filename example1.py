from square import Square

if __name__ == "__main__":
    try:
        side = int(input("What size square do you want? "))
        symbol = str(input("What symbol do you want to use? "))
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    except Exception as e:
        print(f"Something went wrong: {e}")
    else:
        sq = Square(side, symbol)

        try:
            print_mode = int(
                input("Do you want to print it with (1) color or with (2) effects? ")
            )
        except ValueError:
            print("Oops! That was no valid number. Try again...")
        except Exception as e:
            print(f"Something went wrong: {e}")
        else:
            match print_mode:
                case 1:
                    color = str(
                        input("What color do you want? [green|cyan|blue] ")
                    ).lower()
                    sq.print_with_color(color)
                case 2:
                    sq.print_with_effect()
                case _:
                    print("Invalid option. Run the script again")
