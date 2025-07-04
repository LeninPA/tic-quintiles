#!/usr/bin/env python
import argparse

# Create CLI interface
parser = argparse.ArgumentParser(
    prog="quintile.py",
    description="Calculates quintiles for a given dataset",
    epilog="Created by TICs x Sudo"
)
parser.add_argument(
    "year",
    help="Year for which quintiles will be calculated",
    type=int
)
parser.add_argument(
    "-d", "--decile",
    help="Calculates deciles instead of quintiles",
    action="store_true"
)
args = parser.parse_args()

if args.decile:
    print("Will calculate decile instead of quintiles")
