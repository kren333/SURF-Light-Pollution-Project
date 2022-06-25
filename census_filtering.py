# to use: 1) comment out lines 70-72 2) run program 3) comment out lines 56, 59, 62
# 4) remove comment out on lines 70-72 5) add 'id' to first row of csv files 6) run program


import pandas as pd
import csv
import numpy as np


# filter data from unfiltered spreadsheet
def filter_csv(file_name, codes, var):
    data = pd.read_csv(file_name, index_col=var)
    blank = pd.DataFrame()

    for i in codes:
        # blank = pd.concat([blank, data.loc[i]], axis=1)
        blank = blank.append(data.loc[i])

    return blank


# list of census tract ids
code_list = ("1400000US42003070300",
             "1400000US42003070800",
             "1400000US42003140400",
             "1400000US42003141400",
             "1400000US42003980300",
             "1400000US42003180700",
             "1400000US42003180300",
             "1400000US42003562400",
             "1400000US42003481000",
             "1400000US42003160800",
             "1400000US42003161000",
             "1400000US42003160900",
             "1400000US42003130800",
             "1400000US42003140500",
             "1400000US42003565300",
             "1400000US42003120900",
             "1400000US42003120900",
             "1400000US42003980100",
             "1400000US42003101800",
             "1400000US42003981000",
             "1400000US42003981000",
             "1400000US42003060300",
             "1400000US42003060500",
             "1400000US42003980400",
             "1400000US42003290400",
             "1400000US42003290100",
             "1400000US42003191700",
             "1400000US42003562800",
             "1400000US42003562800",
             "1400000US42003563100",
             "1400000US42003191100",
             )

# create and filter files
incomes = filter_csv("meanincome.csv", code_list, "id")
# incomes.to_csv('filtered_mean_income.csv')

family_poverty = filter_csv("family_poverty.csv", code_list, "id")
# family_poverty.to_csv('filtered_family_poverty.csv')

unemployment = filter_csv("unemployment.csv", code_list, "id")
# unemployment.to_csv('filtered_unemployment.csv')

population = filter_csv("population.csv", code_list, "id")
# population.to_csv('filtered_population.csv')

age_sex = filter_csv("age_sex.csv", code_list, "id")
# age_sex.to_csv('filtered_age_sex.csv')

# combine filtered files w/light pollution data
# incomes_np = incomes.to_numpy()
# family_poverty_np = family_poverty.to_numpy()
# unemployment_np = unemployment.to_numpy()

only_poverty = pd.read_csv("filtered_family_poverty.csv", usecols=
        ["id","Estimate!!Number!!PER CAPITA INCOME BY RACE AND HISPANIC OR LATINO ORIGIN!!Total population", "Estimate!!Percent Distribution!!HOUSEHOLD INCOME!!All households!!With cash public assistance income or Food Stamps/SNAP"])
# only_poverty.to_csv('per_capita_income_and_percent_food_stamps.csv')

only_pop = pd.read_csv("filtered_population.csv", usecols=["id", "Estimate!!SEX AND AGE!!Total population"])
# only_pop.to_csv('total_population.csv')

# population_np = only_pop.to_numpy()


