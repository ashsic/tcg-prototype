from card import Card

class Deck:
    def __init__(self, name: str, creator: str, cards: list[Card] = [], length: int = 40):
        if not isinstance(name, str):
            raise TypeError("Deck name must be a string")
        self._name = name

        if not isinstance(creator, str):
            raise TypeError("Deck creator must be a string")
        self._creator = creator

        if not isinstance(cards, list):
            raise TypeError("Deck cards must be a list of Card objects")
        if len(cards) > length:
            raise ValueError(f"Number of cards ({len(cards)}) cannot exceed deck length ({length})")
        self._cards = cards

        if not isinstance(length, int) or length <= 0:
            raise ValueError("Deck length must be a positive integer")
        self._length = length

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError("Deck name must be a string")
        self._name = new_name

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, new_creator: str):
        if not isinstance(new_creator, str):
            raise TypeError("Deck creator must be a string")
        self._creator = new_creator

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, new_cards: list[Card]):
        if not isinstance(new_cards, list):
            raise TypeError("Deck cards must be a list of Card objects")
        if len(new_cards) > self._length:
            raise ValueError(f"Number of cards ({len(new_cards)}) cannot exceed deck length ({self._length})")
        self._cards = new_cards

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length: int):
        if not isinstance(new_length, int) or new_length <= 0:
            raise ValueError("Deck length must be a positive integer")
        if len(self._cards) > new_length:
            raise ValueError(f"Number of cards ({len(self._cards)}) cannot exceed new deck length ({new_length})")
        self._length = new_length
