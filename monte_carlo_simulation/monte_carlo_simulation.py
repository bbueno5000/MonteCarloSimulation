"""
DOCSTRING
"""
import random

def roll_dice():
    """
    DOCSTRING
    """
    return bool(100 > random.randint(1, 100) > 50)

def simple_bettor(bankroll, initial_wager, wager_count):
    """
    DOCSTRING
    """
    wager = initial_wager
    for _ in range(wager_count):
        if roll_dice():
            bankroll += wager
        else:
            bankroll -= wager
    return bankroll

if __name__ == '__main__':
    for _ in range(100):
        print('Bankroll:' + str(simple_bettor(10000, 100, 100)))
