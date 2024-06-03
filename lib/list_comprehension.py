#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) == 0:
        return []
    else: 
        return [num for num in num_list if num%2 == 0]

def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []
    else:
        return [string + '!' for string in sentence_list]