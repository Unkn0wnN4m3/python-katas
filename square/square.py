from typing import List

from square import Colors


class Square:
    """
    Make a square filled out by any latter you want.

    Attrubutes:
        side -- the side lenght of the square
        symbol -- ascii symbol or text to be used (default: "*")

    Methods:
        build() -- return a list of lists with strings
    """

    def __init__(self, side: int, symbol: str) -> None:
        """
        Constructs all the necessary attributes for the Square object.

        Parameters:
            side -- square length
            symbol -- square symbol
        """
        self.__side = side
        self.__symbol = symbol

    def build(self) -> List[List[str]]:
        """
        Build into a list of lists.

        Parameters:
            None

        Return:
            A list filled by symbols you choose
        """
        return [
            [f"{self.__symbol}" for _ in range(self.__side)] for _ in range(self.__side)
        ]

    def print_with_color(self, color):
        """
        Print the square in your terminal, and colorize de output.

        Parameters:
            color -- choose your color. Should be "green" or "cyan" or "blue"

        Return:
            None
        """
        # [ ["*", "*"], ["*", "*"] ]
        for i in self.build():
            # ["*", "*"]
            for j in i:
                match color:
                    case "green":
                        print(f"{Colors.green}{j}{Colors.reset}", end=" ")
                    case "cyan":
                        print(f"{Colors.cyan}{j}{Colors.reset}", end=" ")
                    case "blue":
                        print(f"{Colors.blue}{j}{Colors.reset}", end=" ")
                    case _:
                        print(f"{Colors.green}{j}{Colors.reset}", end=" ")
            print()
