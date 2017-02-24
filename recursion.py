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