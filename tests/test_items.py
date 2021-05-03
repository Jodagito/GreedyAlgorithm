from random import uniform
from unittest import TestCase, mock
from container import Container, CONTAINER_MAX_CAPACITY
from item import Item


class TestItems(TestCase):

    def test_item_creation(self):
        item = Item()
        self.assertIsNotNone(item)
        self.assertIsNotNone(item.code)
        self.assertIsNotNone(item.value)
        self.assertIsNotNone(item.weight)

    def test_fraction_item(self):
        item = Item()
        container = Container()
        current_capacity = round(
            uniform(CONTAINER_MAX_CAPACITY / 2, CONTAINER_MAX_CAPACITY), 2)
        percentage = (CONTAINER_MAX_CAPACITY - current_capacity) / item.weight
        container.current_capacity = current_capacity
        initial_value = item.value
        expected_result = round(initial_value * percentage, 2)
        item.fraction_item(container)
        result = item.value
        self.assertNotEqual(initial_value, result)
        self.assertEquals(expected_result, result)
