import pandas as pd
# preparando los datos y los nombres de las columnas
atlas = [
      ['France', 'Paris'],
        ['Russia', 'Moscow'],
        ['China', 'Beijing'],
        ['México', 'Ciudad de México'],  
        ['Egypt', 'Cairo'],
]
geography = ['country', 'capital']

# creando un DataFrame
world_map = pd.DataFrame(data=atlas , columns=geography)
print(world_map.dtypes) #imprimimos el atributo dtypes
print(world_map.columns) #imprimimos el atributo columns 
print(world_map.shape) #imprimimos el atributo shape 
print(world_map.info()) #imprimimos todos los atributos a la vez