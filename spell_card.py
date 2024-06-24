from card import Card, ResourceType

class SpellCard(Card):
    def __init__(
        self,
        name: str,
        element: str,
        effect: str,
        resource_cost: int,
        resource_type: ResourceType,
        spell_type: str
    ):
        super().__init__(name, element, effect, resource_cost, resource_type)
        self._spell_type = spell_type

    @property
    def spell_type(self):
        return self._spell_type

    @spell_type.setter
    def spell_type(self, new_spell_type: str):
        if not isinstance(new_spell_type, str):
            raise TypeError("Monster card spell_type must be a string")
        self._spell_type = new_spell_type