# returns number of periods it would take n things to reach target from spread conversions each period
def disease_halflife(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + disease_halflife(n + (n*spread), spread, target) # n * spread


 # counts the items in lists of lists of lists

def deep_count(p):
    sum = 0
    for e in p:
        sum += 1
        if is_list(e):
            sum += deep_count(e)
    return sum

def is_list(p):
    return isinstance(p, list)


def ancenstry(genes, person):
    if person in genes:
        parents = genes[person]
        results = parents
        for parent in parents:
            result = result + ancestry(genes, parent)
        return results
    return []

# here is where a change was made
ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }
