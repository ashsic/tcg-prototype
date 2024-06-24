class Board:
    def __init__(self, width: int = 4):
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Board width must be a positive integer")
        self._width = width

        self._fields = [""] * self._width
        self._p1_Spells = [""] * self._width
        self._p2_Spells = [""] * self._width
        self._p1_Monsters = [""] * self._width
        self._p2_Monsters = [""] * self._width

        self._boardOrder = [
            self._p1_Spells,
            self._p1_Monsters,
            self._fields,
            self._p2_Monsters,
            self._p2_Spells,
        ]

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value: str, idx: int):
        if not isinstance(value, str):
            raise TypeError("Field value must be a string")
        if (idx < 0 or idx > self._width - 1):
            raise ValueError(f"Index must be between 0 and {len(self.fields)}.")
        self._fields[idx] = value

    @property
    def p1_Spells(self):
        return self._p1_Spells

    @p1_Spells.setter
    def p1_Spells(self, value: list[str]):
        if not isinstance(value, list):
            raise TypeError("p1_Spells must be a list of strings")
        if len(value) != self._width:
            raise ValueError(f"p1_Spells list length must match board width ({self._width})")
        self._p1_Spells = value

    @property
    def p2_Spells(self):
        return self._p2_Spells

    @p2_Spells.setter
    def p2_Spells(self, value: list[str]):
        if not isinstance(value, list):
            raise TypeError("p2_Spells must be a list of strings")
        if len(value) != self._width:
            raise ValueError(f"p2_Spells list length must match board width ({self._width})")
        self._p2_Spells = value

    @property
    def p1_Monsters(self):
        return self._p1_Monsters

    @p1_Monsters.setter
    def p1_Monsters(self, value: list[str]):
        if not isinstance(value, list):
            raise TypeError("p1_Monsters must be a list of strings")
        if len(value) != self._width:
            raise ValueError(f"p1_Monsters list length must match board width ({self._width})")
        self._p1_Monsters = value

    @property
    def p2_Monsters(self):
        return self._p2_Monsters

    @p2_Monsters.setter
    def p2_Monsters(self, value: list[str]):
        if not isinstance(value, list):
            raise TypeError("p2_Monsters must be a list of strings")
        if len(value) != self._width:
            raise ValueError(f"p2_Monsters list length must match board width ({self._width})")
        self._p2_Monsters = value
    
    def showBoard(self):
        for o in self._boardOrder:
            for s in o:
                print(f'|{s:30}|', end="")
            print()



if __name__ == "__main__":
    f = ["Forest", "Ocean", "Darkness", "Mana Spring"]
    p1s = ["Element Blade", "", "Reroll", ""]
    p1m = ["Chainsaw Imp", "", "Hydra", ""]
    p2s = ["Reroll", "", "", ""]
    p2m = ["", "Elf Swordsman", "Deep Sea Kraken", ""]

    board = Board()

    board.fields = f
    board.p1_Spells = p1s
    board.p1_Monsters = p1m
    board.p2_Spells = p2s
    board.p2_Monsters = p2m

    board.showBoard()