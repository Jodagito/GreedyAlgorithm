from random import randint, uniform
from uuid import uuid4
from container import CONTAINER_MAX_CAPACITY


class Item:
    code = ''
    value = 0
    weight = 0

    def __init__(self):
        self.code = uuid4().hex
        self.value = randint(10, 10000000)
        self.weight = round(uniform(1, CONTAINER_MAX_CAPACITY), 2)

    def fraction_item(self, container):
        percentage = (CONTAINER_MAX_CAPACITY -
                      container.current_capacity) / self.weight
        if percentage:
            self.value = round(self.value * percentage, 2)
            self.weight = round(self.weight * percentage, 2)
            container.add_item_to_container(self)
