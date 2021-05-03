import os
from sys import setrecursionlimit
from container import Container, CONTAINER_MAX_CAPACITY
from item import Item

setrecursionlimit(10**6)


def fill_items(quantity: int):
    items = []
    while len(items) < quantity:
        item = Item()
        if item.code not in items:
            items.append(item)
    return sorted(items, key=lambda item: item.value / item.weight, reverse=True)


def fill_container(items: list, container: Container):
    if len(items) > 0 and container.current_capacity < CONTAINER_MAX_CAPACITY:
        item = items[0]
        if container.current_capacity + item.weight <= CONTAINER_MAX_CAPACITY:
            container.add_item_to_container(item)
        else:
            item.fraction_item(container)
        items.remove(item)
        fill_container(items, container)
    return container


def main():
    quantity = int(
        input("How many items do you want to generate? "))
    os.system('cls' if os.name == 'nt' else 'clear')
    return fill_container(fill_items(quantity), Container())


if __name__ == '__main__':
    container = main()
    container.print_container()
