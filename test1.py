import pandas as pd
from temp_converter import *
city1 =[68,20, 102]
unit = ["C", "C", "F"]
new_list=pd.DataFrame()
for temp, unit in zip(city1, unit):
     t1 = TemperatureConverter(temp, unit)
     new_temp =t1.convert('C')
     
     new_list = new_list.append({'new_temp' : new_temp, 
     "old_temp": temp, "unit": unit}, 
     ignore_index = True)

new_list['City'] = pd.Series(['A', 'B', 'C'])
print(new_list)
 ###
     
