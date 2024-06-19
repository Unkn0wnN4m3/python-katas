from typing import List

from terminaltexteffects.effects import effect_print

from square import Colors


class Square:
    """
    Make a square filled out by any latter you want.

    Attributes:
        side -- the side length of the square
        symbol -- ascii symbol or text to be used (default: "*")

    Methods:
        build_iter() -- return a list of lists with strings
        build_string() -- return the square in text string
        print_with_color() -- prints on console with colors
        build() -- print in console using the effects library "terminaltexteffects"
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

    def build_iter(self) -> List[List[str]]:
        """
        Build a iterable, a list of lists.

        Parameters:
            None

        Return:
            A list filled by symbols you choose
        """
        return [
            [f"{self.__symbol}" for _ in range(self.__side)] for _ in range(self.__side)
        ]

    def build_string(self) -> str:
        """
        builds directly on square in text strings

        Parameters:
            None

        Return:
            The square in a text string
        """
        txt = ""

        for i in self.build_iter():
            for j in i:
                txt += j + " "

            txt += "\n"

        return txt

    def print_with_color(self, color: str) -> None:
        """
        Print the square in your terminal, and colorize de output.

        Parameters:
            color -- choose your color. Should be "green" or "cyan" or "blue"

        Return:
            None
        """
        match color:
            case "green":
                print(f"{Colors.GREEN}{self.build_string()}{Colors.RESET}", end=" ")
            case "cyan":
                print(f"{Colors.CYAN}{self.build_string()}{Colors.RESET}", end=" ")
            case "blue":
                print(f"{Colors.BLUE}{self.build_string()}{Colors.RESET}", end=" ")
            case _:
                print(f"{Colors.GREEN}{self.build_string()}{Colors.RESET}", end=" ")

    def print_with_effect(self) -> None:
        """
        Print the square in your terminal using 'terminaltexteffects'.

        Parameters:
        None

        Return:
            None
        """
        effect = effect_print.Print(self.build_string())
        with effect.terminal_output() as terminal:
            for frame in effect:
                terminal.print(frame)
