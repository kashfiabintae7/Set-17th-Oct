def prob_a_or_b(a, b, all_possible_outcomes):
    prob_a = len(a) / len(all_possible_outcomes)
    prob_b = len(b) / len(all_possible_outcomes)
    inter = a.intersection(b)
    prob_inter = len(inter) / len(all_possible_outcomes)
    return prob_a + prob_b - prob_inter

evens = {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

print("Probability of Getting an Even or a Number greater than 2:")
print(prob_a_or_b(evens, greater_than_two, all_possible_rolls))

# Event A: Getting an even number → {2, 4, 6}
# Event B: Getting a number greater than 2 → {3, 4, 5, 6}
# Common outcomes: {4, 6}
# → Events are NOT mutually exclusive (they can happen together)
# → Events are INDEPENDENT (one does not affect the other)