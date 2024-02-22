##
## EPITECH PROJECT, 2024
## parser.py
## File description:
## Parse params
##

import sys

def synth_sch_parse() -> dict:
    data = {
        "n": int(sys.argv[1]),
        "i0": int(sys.argv[2]),
        "i1": int(sys.argv[3]),
    }
    if not data["i0"] < data["i1"]:
        raise ValueError("i1 must be greater than i0")
    if data["i0"] < 0 or data["i1"] < 0:
        raise ValueError("i0 and i1 must be positive")
    return data

def pop_ev_parse() -> dict:
    data = {
        "n": int(sys.argv[1]),
        "k": float(sys.argv[2]),
    }
    if data['k'] < 1 or data['k'] > 4:
            raise ValueError("Growth rate should be between 1 and 4")
    return data

def parse() -> dict:
    if len(sys.argv) == 3:
        data = pop_ev_parse()
    elif len(sys.argv) == 4:
        data = synth_sch_parse()
    else:
        raise Exception("Invalid amount of arguments")
    if data["n"] < 0:
        raise ValueError("n cant be negative")
    return data
