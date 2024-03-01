import pandas as pd
from pandas import Series
import json


# Given a csv file with students names and scores, find the student with the highest score.
def highest_score(filepath, col_score, col_name):
    df = pd.read_csv(filepath)
    idx_max_value = df[col_score].idxmax()
    full_row = df.loc[idx_max_value]
    return full_row[col_name]


# Given a csv file with employee details (name, age, salary), calculate de average salary of all employees.

def average_salary(filepath, col_salary):
    df = pd.read_csv(filepath)
    salary = df[col_salary]
    mean = salary.mean()
    return mean


# Write a program that reads a CSV file and finds the total sales revenue for a specific product.

def product_revenue(filepath, col_product, product, col_sales, col_number):
    df = pd.read_csv(filepath)
    # Seleccion de una fila por el valor de una columna concreta
    product_row = df[df[col_product] == product]
    # Multiplicamos los elementos de ambas series y obtenemos otra serie
    revenue_series = product_row[col_sales] * product_row[col_number]
    # No sabemos el indice que tendra el unico elemento de revenue_series,
    # por eso sumamos todos los elementos de la serie y obtenemos el resultado
    return revenue_series.sum()


# Given a CSV file with temperature data for each day of the week, find the average temperature for each day.
def average_temperature(filepath, col_day, day, col_minimum, col_maximum):
    df = pd.read_csv(filepath)
    day_row = df[df[col_day] == day]
    temperature_mean = (day_row[col_minimum] + day_row[col_maximum]) / 2
    return temperature_mean.sum()


# Given a CSV file with students details, read it into a Pandas Dataframe and find the average age of students.
def age_average(filepath, col_age):
    df = pd.read_csv(filepath)
    age = df[col_age]
    average = age.mean().round(1)
    # Para redondear en caso de que el decimal salga periodico (en este caso redondeo al primer decimal)
    return average


# Implement a program that generates a Pandas Series with dates and filter it to get a specific range.
def generate_panda_series():
    my_dates = pd.date_range(start='1/1/2024', end='1/9/2024')
    print(my_dates)


# Write a Python program that uses Pandas to read a CSV file and find the maximum and minimum values in each column.
def max_and_min(filepath, col_value1, col_value2, col_value3):
    df = pd.read_csv(filepath)
    max_values = [df[col_value1].max(), df[col_value2].max(), df[col_value3].max()]
    min_values = [df[col_value1].min(), df[col_value2].min(), df[col_value3].min()]
    return max_values, min_values


# Create a function that takes a Pandas DataFrame and returns a new DataFrame with rows sorted in ascending order.
def sort_asc_order(filepath):
    df = pd.read_csv(filepath)
    idx_ascend = df.sort_index(ascending=False)
    return idx_ascend


# Given a Pandas DataFrame, filter the rows to include only the rows where a specific column meets a condition.
def filter_dataframe(filepath, col_name, value):
    df = pd.read_csv(filepath)
    filtered_df = df[df[col_name] == value]
    return list(filtered_df.index)


# Implement a program that reads a CSV file into a Pandas DataFrame and calculates the sum of a specific column.
def sum_values_column(filepath, col_values):
    df = pd.read_csv(filepath)
    column_sum = df[col_values].sum()
    return column_sum


# Write a function that takes a Pandas DataFrame and adds a new calculated column to the DataFrame
def new_sum_column(filepath, col_1, col_2, col_3, new_col):
    df = pd.read_csv(filepath)
    df[new_col] = df[col_1] + df[col_2] + df[col_3]
    return df


# Given a Pandas DataFrame, group the data by a specific column and calculate the mean of another column
def pd_sort_column_mean(filepath, col_to_group):  # group by
    df = pd.read_csv(filepath)
    group = df.groupby([col_to_group]).mean().reset_index()
    return group


# Create a program that reads a JSON file into Pandas DataFrame and extracts specific info from it.

def read_json(filepath, col_info, index):
    df = pd.read_json(filepath)
    info_student = df.at[index, col_info]
    return info_student


# Implement a function that takes a Pandas DataFrame and returns the transpose of the DataFrame
def transpose_data_frame():
    df = pd.DataFrame({'score_1': [5, 6, 7], 'score_2': [9, 8, 7]})
    transpose = df.transpose()
    print(transpose)


if __name__ == '__main__':
    pass
    # print(pd_sort_column_mean('Animals.csv', 'Animal'))
