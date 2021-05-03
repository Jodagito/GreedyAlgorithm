from unittest import TestCase, mock
from container import Container, CONTAINER_MAX_CAPACITY
from item import Item


class TestContainers(TestCase):

    def test_container_creation(self):
        container = Container()
        self.assertIsNotNone(container)

    def test_add_item_to_container(self):
        item = Item()
        container = Container()
        container.add_item_to_container(item)
        self.assertTrue(item in container.current_items)
