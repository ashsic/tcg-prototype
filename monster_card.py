from card import Card, ResourceType

class MonsterCard(Card):
    def __init__(
        self,
        name: str,
        element: str,
        effect: str,
        resource_cost: int,
        resource_type: ResourceType,
        species: str,
        attack: int,
        defense: int,
    ):
        super().__init__(name, element, effect, resource_cost, resource_type)
        self._species = species
        self._attack = attack
        self._defense = defense

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, new_species: str):
        if not isinstance(new_species, str):
            raise TypeError("Monster card species must be a string")
        self._species = new_species

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, new_attack: int):
        if not isinstance(new_attack, int) or new_attack < 0:
            raise ValueError("Monster card attack power must be a non-negative integer")
        self._attack = new_attack

    @property
    def defense(self):
        return self._defense
    
    @defense.setter
    def defense(self, new_defense: int):
        if not isinstance(new_defense, int) or new_defense < 0:
            raise ValueError("Monster card defense power must be a non-negative integer")
        self._defense = new_defense