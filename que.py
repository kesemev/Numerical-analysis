import sys
import random

class Randomizer():
    @staticmethod
    def sample(spread, count):
        return random.sample(range(spread[0], spread[1] + 1), count)

    @staticmethod
    def flatten(collection):
        collection = list(x for y in collection for x in y)
        collection.sort()
        return collection

    def questions(self, seed):
        random.seed(seed)
        spreads = {
            (1,5): 1,
            (6,13): 2,
            (14,17): 1,
            (18,25): 2
        }
        return Randomizer.flatten(Randomizer.sample(*spread) for spread in spreads.items())

id = input('Please enter your ID number: ')

print('You were assigned the following questions: {}'.format(
    Randomizer().questions(id)
))