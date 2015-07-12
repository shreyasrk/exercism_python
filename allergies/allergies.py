allergens = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats'
}


class Allergies:
    def __init__(self, score):
        self.score = score
        self.list = self.get_items_list()

    def is_allergic_to(self, item):
        return True if self.score in allergens.keys() else False

    def get_items_list(self):
        pass
