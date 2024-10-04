import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # check all params for our conditions, quantity must be grater than 0 and grater than min-max range to get nedded amount of randoms
    if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity <= 0:
        return []
    else:
        # use range to generate random numbers 
        numbers = random.sample(range(min, max + 1), quantity)
        # return sorted numbers list
        return sorted(numbers)