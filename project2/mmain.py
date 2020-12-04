"""
Calculates the best route to take when visiting the given cities, defining "best" as the highest average of temperature,
while also calculating which hotels to stay at in order to make the best use of your budget without overspending.
"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}

DAYS = len(city_temps)

def cost_route(route):
    """
    Calculates the average temperature for each permutation by taking the sum and dividing it by the length of the
    dictionary containing the cities you wish to visit.
    """
    return sum([city_temps[route[i]][i] for i in range(len(route))])/len(route)



def best_route(all_routes):
    """
    Iterates over all the permutations and compares the average of that one to the next permutation. If the
    average temp is higher then the previous then it overrides the max value and becomes the new max and set's it to the
    variable best
    """
    max_temp = 0
    best = None

    for r in all_routes:
        avg_temp = cost_route(r)
        if max_temp <avg_temp:
            max_temp = avg_temp
            best = r
    return max_temp, best

cities = list(city_temps.keys())
permu = permutations(cities, DAYS)
best_avg_temp, best_way = best_route(permu)

# part 2: Lodging

hotels = list(hotel_rates.keys())

HOTEL_BUDGET = 850

def cost_func(t):
    """"
    Calculates the overall cost for each possible combination of hotels
    """
    s = 0
    for i in t:
        s+= hotel_rates[i]
    return s


combs = combinations_with_replacement(hotels, DAYS)

best_option = min(combs, key= lambda t : HOTEL_BUDGET - cost_func(t) if HOTEL_BUDGET >= cost_func(t) else HOTEL_BUDGET)

if __name__ == "__main__":
    # ..
    print(f'Here is your best route: {best_way} the average of the daily max temp. is {best_avg_temp}F')
    # ..
    print(f'To max out your hotel budget, stay at these hotels: {best_option}, totaling ${cost_func(best_option)}')
