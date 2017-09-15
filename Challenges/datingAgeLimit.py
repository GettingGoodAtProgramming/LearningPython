

# Returns the lowest age limit for given age
def allowed_dating_age(user_age):
    limit_age = user_age / 2 + 7
    return limit_age


# Prints the user's age and their lower limit on the same line separated by a tab.
def print_ages(user_age):
    print(user_age, "    ", allowed_dating_age(user_age))


# Prints a table of the ages and their lower limit.
def print_ages_list(low, high):
    print("Age", "  ", "Limit")

    for x in range(high-low):
        print_ages(x+low)


# Test
print_ages_list(18, 25)
