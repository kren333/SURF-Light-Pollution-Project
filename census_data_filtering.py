import pandas as pd
import csv
import numpy as np

# set to 1 to refresh semi-filtered files
want_to_write = 0

# remove dupes
df = pd.read_csv("helper files/codes.csv", sep="\t or ,")
df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
df.to_csv("helper files/new_codes.csv", index=False)


# filter data from unfiltered spreadsheet
def filter_csv(file_name, codes_file, var):
    data = pd.read_csv(file_name, index_col=var)
    blank = pd.DataFrame()
    file = pd.read_csv(codes_file)

    codes = file["id"]

    for i in codes:
        blank = blank.append(data.loc[i])

    return blank


def get_col(file_name, col_file, file):
    data = pd.read_csv(file_name)
    blank = pd.DataFrame()
    cols = pd.read_csv(col_file)
    new = cols[file]
    new = new.dropna()

    for i in new:
        blank[i] = data[i]

    return blank


code_list = "helper files/codes.csv"

# create and filter files
incomes = filter_csv("raw files/meanincome.csv", code_list, "id")
if want_to_write == 1:
    incomes.to_csv('filtered files/filtered_mean_income.csv')

unemployment = filter_csv("raw files/unemployment.csv", code_list, "id")
if want_to_write == 1:
    unemployment.to_csv('filtered files/filtered_unemployment.csv')

population = filter_csv("raw files/population.csv", code_list, "id")
if want_to_write == 1:
    population.to_csv('filtered files/filtered_population.csv')

age_sex = filter_csv("raw files/age_sex.csv", code_list, "id")
if want_to_write == 1:
    age_sex.to_csv('filtered files/filtered_age_sex.csv')

occupancy = filter_csv("raw files/occupancy.csv", code_list, "id")
if want_to_write == 1:
    occupancy.to_csv('filtered files/filtered_occupancy.csv')

# filter the filtered files to get the columns wanted

# set to 1 to refresh final files
want_to_write2 = 1

income_final = get_col("filtered files/filtered_mean_income.csv", "helper files/cols.csv", "mean_income")
if want_to_write2 == 1:
    income_final.to_csv('files to use/income.csv')

unemployment_final = get_col("filtered files/filtered_unemployment.csv", "helper files/cols.csv", "unemployment")
if want_to_write2 == 1:
    unemployment_final.to_csv('files to use/unemployment.csv')

population_final = get_col("filtered files/filtered_population.csv", "helper files/cols.csv", "population")
if want_to_write2 == 1:
    population_final.to_csv('files to use/population.csv')

age_sex_final = get_col("filtered files/filtered_age_sex.csv", "helper files/cols.csv", "age_sex")
if want_to_write2 == 1:
    age_sex_final.to_csv('files to use/age_sex.csv')

occupancy_final = get_col("filtered files/filtered_occupancy.csv", "helper files/cols.csv", "occupancy")
if want_to_write2 == 1:
    occupancy_final.to_csv('files to use/occupancy.csv')
