import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

dict_data = {'a': 100, 'b': 200, 'c': 300}

#df = pd.read_csv('california_housing_test.csv')

dataframe_from_dict = pd.DataFrame(dict_data.items(), columns=['key', 'value'])

df = pd.DataFrame({
    '1': [1, 2, 3, 4, 4, 2,2,2],
    '2': [2, 4, 6, 2,2,2,2,6]
})

# Непересекающиеся элементы
no_intersect_1 = df['1'][~df['1'].isin(df['2'])]
no_intersect_2 = df['2'][~df['2'].isin(df['1'])]

# Узнать частоту уникальных элементов объекта Series или в 
# одной колонке (можно для нескольких) Dataframe, и построить гистограм
# му (семейство гистограмм) с помощью plt.bar();
# Unique 
unique_ser  = df['1']

unique_count= unique_ser.value_counts()

# Гистограмма
# plt.bar(unique_count.index, unique_count.values)
# plt.xlabel('значения')
# plt.ylabel('Частота')
# plt.title('Гистограмма частот')
# plt.grid(True)
# plt.show()

print(unique_count)


# Объединить два объекта Dataframe вертикально 
# (конкатенация: pd.concat()) и горизонтально 
# (добавить столбцы: df.insert() или pd.merge());


df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': ['a', 'b', 'c']})

df2 = pd.DataFrame({'A': [4, 5, 6],
                    'B': ['d', 'e', 'f']})


result_concat = pd.concat([df1, df2], ignore_index=True)
print(result_concat)
data = ['x', 'y', 'z', 'w', 'v', 'u']
result_concat.insert(2, 'C', data)
result_merge = pd.merge(df1, df2, left_index=True, right_index=True)
print(result_merge)


#построить график зависимости одного столбца от другого для 
# Dataframe 
# (можно несколько, т.е. создать семейство кривых на одном графике).

plt.plot(df['1'],df['2'])

plt.title('Зависимость y от x')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.show()