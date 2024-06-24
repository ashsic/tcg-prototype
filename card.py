from enum import Enum

class ResourceType(Enum):
  BLOOD = "Blood"
  MANA = "Mana"

class Card:
    def __init__(
        self,
        name: str,
        element: str,
        effect: str,
        resource_cost: int,
        resource_type: ResourceType,
    ):
        self._name = name
        self._element = element
        self._effect = effect
        self._resource_cost = resource_cost
        self._resource_type = resource_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError("Card name must be a string")
        self._name = new_name

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, new_element: str):
        if not isinstance(new_element, str):
            raise TypeError("Card element must be a string")
        self._element = new_element

    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, new_effect: str):
        if not isinstance(new_effect, str):
            raise TypeError("Card effect must be a string")
        self._effect = new_effect

    @property
    def resource_cost(self):
        return self._resource_cost

    @resource_cost.setter
    def resource_cost(self, new_cost: int):
        if not isinstance(new_cost, int) or new_cost < 0:
            raise ValueError("Card resource cost must be a non-negative integer")
        self._resource_cost = new_cost

    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, new_type: ResourceType):
        if not isinstance(new_type, ResourceType):
            raise TypeError("Card resource type must be a member of the ResourceType enum")
        self._resource_type = new_type
