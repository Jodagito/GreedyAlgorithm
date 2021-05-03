from unittest import TestCase
from container import Container, CONTAINER_MAX_CAPACITY
from main import fill_container, fill_items


class TestMain(TestCase):

    def test_fill_items(self):
        items = fill_items(10)
        self.assertIsNotNone(items)
        for item in items:
            self.assertIsNotNone(item)
        self.assertEquals(10, len(items))

    def test_fill_container(self):
        items = fill_items(10)
        container = Container()
        items = fill_container(items, container)
        self.assertAlmostEquals(CONTAINER_MAX_CAPACITY,
                                container.current_capacity)
