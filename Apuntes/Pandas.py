import pandas as pd

# Pandas es una libreria que nos permite manejar datos.
if __name__ == '__main__':
    df = pd.read_csv('data.csv')  # Generacion del pandas Dataframe. Cada columna del Dataframe es una serie.
    years = df['Year']  # Esta variable sera una serie. Una serie se compone de un indice y su valor.
    # El indice normalmente va desde 0  tamaño de la serie -1. Ej: 8 elementos -> 0 - 7.

    dict_df = df.to_dict(orient='records')  # Oirent=recors genera por cada una de las filas un diccionario.
    # La clave es el nombre de la columna y el valor es la info de la celda en esa fila y esa columna.
    # metodos 'read' son para leer desde archivos y metodos 'to' para guardar desde dataframe a los archivos.
    df.to_json('data.json', orient='records', indent=4)
    print(dict_df)
    df_2 = df
    pd.merge(left=df, right=df_2, how='inner')  # Para hacer un inner join.
