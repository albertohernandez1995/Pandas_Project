import pandas as pd

# Pandas es una libreria que nos permite manejar datos.
if __name__ == '__main__':
    df = pd.read_csv('data.csv')  # Generacion del pandas Dataframe. Cada columna del Dataframe es una serie.
    column1_series = df['Column1']  # Esta variable sera una serie. Una serie se compone de un indice y su valor.
    # El indice normalmente va desde 0  tamaño de la serie -1. Ej: 8 elementos -> 0 - 7.

    dict_df = df.to_dict(orient='records')  # Oirent=recors genera por cada una de las filas un diccionario.
    # La clave es el nombre de la columna y el valor es la info de la celda en esa fila y esa columna.
    # metodos 'read' son para leer desde archivos y metodos 'to' para guardar desde dataframe a los archivos.
    df.to_json('data.json', orient='records', indent=4)
    print(dict_df)
    df_2 = df
    pd.merge(left=df, right=df_2, how='inner')  # Para hacer un inner join.

    # Filtrar filas por valor de una columna especifica
    # & significa and (ambas condiciones deben ser True)
    filtered_df = df[(df['Column2'] == 2) & (df['Column1'] == 'bbb')]  # Devuelve solo la segunda fila
    # | significa or (al menos una condicion es True) (| es AltGr + 1)
    filtered_df = df[(df['Column2'] == 2) | (df['Column1'] == 'ccc')]  # Devuelve las dos ultimas filas
    print(filtered_df)

    # Filtrar dataframe por ciertas columnas
    filtered_df = df[['Column1', 'Column2']]

    # Filtrar con loc
    print('-------LOC-------')
    filtered_df = df.loc[:, ['Column1', 'Column2']]  # Coge todas las filas y solo las columnas 1 y 2
    print(filtered_df)
    print('-------')
    filtered_df = df.loc[
        [1, 2], ['Column1', 'Column2']]  # Coge solo las filas con indice 1 y 2 y solo las columnas 1 y 2
    print(filtered_df)

    # Groupby
    print('-------Groupby-------')
    grouped_df = df.groupby(['Column1'])  # Agrupo por columna 1 y cojo solo la columna 3
    for value_grouped, group_df in grouped_df:
        # Value grouped sera cada valor agrupado, es una tupla ya que se puede agrupar por más de una columna
        # Group_df será el resto de valores
        print(f"Valor agrupado: {value_grouped}")
        print(f"Dataframe de ese grupo: \n{group_df}")  # Saca cada grupo individualmente. Reiniciamos siempre el indice
        print('-------')

    # En groupby, podemos hacer agregaciones (fijarse que grouped_df viene de agrupar el df por Column1

    print('-------Agregaciones-------')
    # Maximo de cada grupo
    print(grouped_df.max().reset_index())
    print('-------')
    # Media de cada grupo en la columna 2 (sacamos solo columna 1 y 2, porque la 1 seria el index
    # (que luego reiniciamos) y la 2 son los valores medios)
    print(grouped_df['Column2'].mean().reset_index())
    print('-------')
