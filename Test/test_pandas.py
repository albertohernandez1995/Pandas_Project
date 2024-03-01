from pathlib import Path

from pytest import mark

from Apuntes.Pandas_Exercises import (highest_score, average_salary, product_revenue, average_temperature, age_average,
                                      max_and_min, filter_dataframe, sum_values_column, new_sum_column, read_json,
                                      pd_sort_column_mean)

params_score = [
    ('Score', 'Name', 'Javi')
]

params_average = [
    ('Salary', 3000.0)
]

params_product = [
    ('Product', 'Car', 'Sales', 'Number', 27000),
    ('Product', 'Bicycle', 'Sales', 'Number', 18000),
    ('Product', 'Boat', 'Sales', 'Number', 17000),

]

params_temperature = [
    ('Day', 'Monday', 'Minimum', 'Maximum', 11.0),
    ('Day', 'Tuesday', 'Minimum', 'Maximum', 7.5),
    ('Day', 'Wednesday', 'Minimum', 'Maximum', 11.5),
    ('Day', 'Thursday', 'Minimum', 'Maximum', 14.5),
    ('Day', 'Friday', 'Minimum', 'Maximum', 9.5),
    ('Day', 'Saturday', 'Minimum', 'Maximum', 10.5),
    ('Day', 'Sunday', 'Minimum', 'Maximum', 7.5)
]

params_age_average = [
    ('Age', 26.3)
]

params_value_max_min = [
    ('Value1', 'Value2', 'Value3', ([9, 9, 9], [2, 4, 2]))
]

params_filter_condition = [
    ('Value2', 7, [1, 2])

]

params_sum_values_columns = [
    ('Value2', 31)
]

params_new_sum_columns = [
    ('Value1', 'Value2', 'Value3', 'Sum_values', [12, 11, 25, 15, 20])

]

params_read_json = [
    ('Name', 0, 'Javi')
]

params_animals = [
    ('Animal', 'Max_Speed', [375.0, 25.0])
]


@mark.parametrize('col_for_group, col_observations, reference', params_animals)
def test_sort_column_mean(data_path, col_for_group, col_observations, reference):
    csv_file = data_path / 'Animals.csv'
    result = pd_sort_column_mean(csv_file, col_for_group)
    assert result[col_observations].tolist() == reference


@mark.parametrize('col_info, index, reference', params_read_json)
def test_read_json(data_path, col_info, index, reference):
    json_file = data_path / 'student_data.json'
    result = read_json(json_file, col_info, index)
    assert result == reference


@mark.parametrize('col_1, col_2, col_3, new_col, reference', params_new_sum_columns)
def test_new_sum_column(data_path, col_1, col_2, col_3, new_col, reference):
    csv_file = data_path / 'Values.csv'
    result = new_sum_column(csv_file, col_1, col_2, col_3, new_col)
    assert result[new_col].tolist() == reference


@mark.parametrize('col_values, reference', params_sum_values_columns)
def test_sum_value_column(data_path, col_values, reference):
    csv_file = data_path / 'Values.csv'
    result = sum_values_column(csv_file, col_values)
    assert result == reference


@mark.parametrize('col_value, value, reference', params_filter_condition)
def test_filter_condition(data_path, col_value, value, reference):
    csv_file = data_path / 'Values.csv'
    result = filter_dataframe(csv_file, col_value, value)
    assert result == reference


@mark.parametrize('col_value1, col_value2, col_value3, reference', params_value_max_min)
def test_max_min_value(data_path, col_value1, col_value2, col_value3, reference):
    csv_file = data_path / 'Values.csv'
    result = max_and_min(csv_file, col_value1, col_value2, col_value3)
    assert result == reference


@mark.parametrize('col_age, reference', params_age_average)
def test_age_average(data_path, col_age, reference):
    csv_file = data_path / 'students_data.csv'
    result = age_average(csv_file, col_age)
    assert result == reference


@mark.parametrize('col_day, day, col_minimum, col_maximum, reference', params_temperature)
def test_average_temperature(data_path, col_day, day, col_minimum, col_maximum, reference):
    csv_file = data_path / 'temperature.csv'
    result = average_temperature(csv_file, col_day, day, col_minimum, col_maximum)
    assert result == reference


@mark.parametrize('col_product, product, col_sales, col_number, reference', params_product)
def test_revenue(data_path, col_product, product, col_sales, col_number, reference):
    csv_file = data_path / 'sales.csv'
    result = product_revenue(csv_file, col_product, product, col_sales, col_number)
    assert result == reference


@mark.parametrize('col_salary, reference', params_average)
def test_average_salary(data_path, col_salary, reference):
    csv_file = data_path / 'employees_data.csv'
    result = average_salary(csv_file, col_salary)
    assert result == reference


@mark.parametrize('col_score, col_name, reference', params_score)
def test_high_score(data_path, col_score, col_name, reference):
    csv_file = data_path / 'students_data.csv'
    result = highest_score(csv_file, col_score, col_name)
    assert result == reference
