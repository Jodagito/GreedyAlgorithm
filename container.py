CONTAINER_MAX_CAPACITY = 24000


class Container:
    current_capacity = 0.0
    current_value = 0
    current_items = []

    def add_item_to_container(self, item):
        self.current_items.append(item)
        self.current_capacity += item.weight
        self.current_value += item.value

    def print_container(self):
        info = f'The container value is {self.current_value} and its weight is {self.current_capacity}\n\n'
        info += f'\tWhich means its value per weight is {round(self.current_value / self.current_capacity, 2)}\n\n'
        info += f'\t\t\tContains {len(self.current_items)} items\n'
        print(info)
        for item in self.current_items:
            print(item.__dict__)
