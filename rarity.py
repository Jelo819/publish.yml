import random

def assign(lst, desc=True):
    if not lst:
        return []

    length = len(lst)
    max_rarity, min_rarity = 100, 1  

    rarity_values = [
        int(max_rarity - (i * (max_rarity - min_rarity) / (length - 1)))
        for i in range(length)
    ]

    if not desc:
        rarity_values.reverse()

    return list(zip(lst, rarity_values))

def get(lst, count, desc=True):
    if not lst or count <= 0:
        return ""

    rarity_list = assign(lst, desc)
    choices, weights = zip(*rarity_list)

    return format_list(random.sample(choices, min(count, len(choices))))

def count(lst):
    if not lst:
        return 0

    length = len(lst)

    
    count_rarities = [
        int(100 * (0.5 ** (i / (length / 2))))  
        for i in range(length)
    ]

    
    count_rarities = [max(1, r) for r in count_rarities]

    chosen_count = random.choices(range(1, length + 1), weights=count_rarities, k=1)[0]

    return chosen_count

def format_list(lst):
    if not lst:
        return ""
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return f"{lst[0]} and {lst[1]}"
    
    last = lst.pop()
    return f"{', '.join(lst)}, and {last}"
