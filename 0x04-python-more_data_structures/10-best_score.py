#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = next(iter(a_dictionary))
    best_score = a_dictionary[best_key]
    for key, value in a_dictionary.items():
        if value > best_score:
            best_key = key
            best_score = value
        return best_key
