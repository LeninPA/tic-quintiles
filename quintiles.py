#!/usr/bin/env python
import argparse
import pandas as pd

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
    "-d", "--data",
    help="Path to data",
    default="./data/clean/pob_mitad_cleaned.csv"
)
parser.add_argument(
    "-D", "--decile",
    help="Calculates deciles instead of quintiles",
    action="store_true"
)
args = parser.parse_args()

if args.decile:
    print("Will calculate decile instead of quintiles")
# Reading data
df = pd.read_csv(args.data)
year = args.year

# TODO: Entidad as CLI args
entidad = 'República Mexicana'

total = df.loc[(df['AÑO'] == year) & (df['ENTIDAD'] == entidad),\
               'POBLACION'].sum()
# Quintiles
# TODO: Segregate by sex
year0 = df.loc[(df['AÑO'] == year) & \
               (df['ENTIDAD'] == entidad) & \
               (df['EDAD'] == 0), \
               'POBLACION'].sum()
qt1 = df.loc[(df['AÑO'] == year) & (df['ENTIDAD'] == entidad)
               & (df['EDAD'] >= 1) & (df['EDAD'] <= 5), 'POBLACION'].sum()
qt = [year0, qt1]
for i in range(18):
    qt.append(df.loc[(df['AÑO'] == 2025) & \
                     (df['ENTIDAD'] == 'República Mexicana') & \
                     (df['EDAD'] >= (5*i + 6)) &
                     (df['EDAD'] <= (5*i + 10)),\
                     'POBLACION'].sum())
lastqt = df.loc[(df['AÑO'] == year) & \
               (df['ENTIDAD'] == entidad) & \
               (df['EDAD'] >= 100), \
               'POBLACION'].sum()
print(f"Mexico's total population in the year {year} is {total} people")
for elem in qt:
    print(int(elem))
