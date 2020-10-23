from homework4_prac import related_groceries

class grocery(related_groceries):
    def __init__(self, grocery='', grocery2=''):
        super().__init__(grocery,grocery2)

    def all_frequency(self):
        all_groceries = []
        for line in self.all_lines:
            temp = [item for item in line.strip().split(',')
                    if len(item) > 1 and not item.startswith('2019')
                    and item != self.grocery]
            all_groceries.extend(temp)
        set_groceries = set(all_groceries)
        for item in set_groceries:
            frequency = super().frequency()
            print(frequency)

grocery().all_frequency()