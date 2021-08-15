## Energy saved from recycling
<p>Did you know that recycling saves energy by reducing or eliminating the need to make materials from scratch? For example, aluminum can manufacturers can skip the energy-costly process of producing aluminum from ore by cleaning and melting recycled cans. Aluminum is classified as a non-ferrous metal.</p>
<p>Singapore has an ambitious goal of becoming a zero-waste nation. The amount of waste disposed of in Singapore has increased seven-fold over the last 40 years. At this rate, Semakau Landfill, Singapore’s only landfill, will run out of space by 2035. Making matters worse, Singapore has limited land for building new incineration plants or landfills.</p>
<p>The government would like to motivate citizens by sharing the total energy that the combined recycling efforts have saved every year. They have asked you to help them.</p>
<p>You have been provided with three datasets. The data come from different teams, so the names of waste types may differ.</p>
<div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
    <div style="font-size:16px"><b>datasets/wastestats.csv - Recycling statistics per waste type for the period 2003 to 2017</b>
    </div>
    <div>Source: <a href="https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling">Singapore National Environment Agency</a></div>
<ul>
    <li><b>waste_type: </b>The type of waste recycled.</li>
    <li><b>waste_disposed_of_tonne: </b>The amount of waste that could not be recycled (in metric tonnes).</li>
    <li><b>total_waste_recycle_tonne: </b>The amount of waste that could be recycled (in metric tonnes).</li>
    <li><b>total_waste_generated: </b>The total amount of waste collected before recycling (in metric tonnes).</li>
    <li><b>recycling_rate: </b>The amount of waste recycled per tonne of waste generated.</li>
    <li><b>year: </b>The recycling year.</li>
</ul>
    </div>
<div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6; margin-top: 17px;">
    <div style="font-size:16px"><b>datasets/2018_2019_waste.csv - Recycling statistics per waste type for the period 2018 to 2019</b>
    </div>
    <div> Source: <a href="https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling">Singapore National Environment Agency</a></div>
<ul>
    <li><b>Waste Type: </b>The type of waste recycled.</li>
    <li><b>Total Generated: </b>The total amount of waste collected before recycling (in thousands of metric tonnes).</li> 
    <li><b>Total Recycled: </b>The amount of waste that could be recycled. (in thousands of metric tonnes).</li>
    <li><b>Year: </b>The recycling year.</li>
</ul>
    </div>
<div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6; margin-top: 17px;">
    <div style="font-size:16px"><b>datasets/energy_saved.csv -  Estimations of the amount of energy saved per waste type in kWh</b>
    </div>
<ul>
    <li><b>material: </b>The type of waste recycled.</li>
    <li><b>energy_saved: </b>An estimate of the energy saved (in kiloWatt hour) by recycling a metric tonne of waste.</li> 
    <li><b>crude_oil_saved: </b>An estimate of the number of barrels of oil saved by recycling a metric tonne of waste.</li>
</ul>

</div>
<pre><code>
</code></pre>


```python
# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd
```


Cleaning and importing the first dataset which contains values from year 2003 to 

2017 : Refer to it as Dataset 'A'



```python
names = ['Waste_type', 'Total_waste_recycled', 'Year']
recy_2003 = pd.read_csv('datasets/wastestats.csv')
recy_2003.drop(['waste_disposed_of_tonne', 'total_waste_generated_tonne','recycling_rate'], inplace=True, axis=1)
recy_2003.columns = ['Waste_type', 'Total_waste_recycled', 'Year']
recy_2003.set_index('Year', inplace=True)
recy_2003['Total_waste_recycled'] = recy_2003['Total_waste_recycled']
recy_2003.sort_index(ascending=True, inplace=True)
recy_2003.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Waste_type</th>
      <th>Total_waste_recycled</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2003</th>
      <td>Horticultural Waste</td>
      <td>119300.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>Paper/Cardboard</td>
      <td>466200.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>Plastics</td>
      <td>39100.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>Construction Debris</td>
      <td>398300.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>Wood/Timber</td>
      <td>40800.0</td>
    </tr>
  </tbody>
</table>
</div>




Cleaning and importing the first dataset which contains values from year 2018 

to 2019: Refer to it as Dataset 'B'



```python
recy_2018 = pd.read_csv('datasets/2018_2019_waste.csv')

recy_2018.drop('Total Generated (\'000 tonnes)', inplace=True, axis=1)
recy_2018.columns = names
recy_2018['Total_waste_recycled'] = recy_2018['Total_waste_recycled']*1000
recy_2018.set_index('Year', inplace=True)
recy_2018.sort_index(ascending=True, inplace=True)
recy_2018.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Waste_type</th>
      <th>Total_waste_recycled</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018</th>
      <td>Overall</td>
      <td>4726000</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Scrap Tyres</td>
      <td>29000</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Glass</td>
      <td>12000</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Non-Ferrous Metal</td>
      <td>170000</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Used Slag</td>
      <td>179000</td>
    </tr>
  </tbody>
</table>
</div>




The table gives the amount of energy saved in kilowatt hour (kWh) and 

the amount of crude oil (barrels) by recycling 1 metric tonne (1000 kilogram) 

per waste type



Importing and cleaning the conversion table, 

also refer to above cell for the conversion metrics



```python
df = pd.read_csv('datasets/energy_saved.csv')
df1 = df.transpose()
df1.reset_index(drop=True, inplace=True)
df1 = df1.iloc[:,2:]
header_row = df1.iloc[0]
energy_saved = df1.iloc[1:]
energy_saved.columns = header_row
energy_saved.set_index('material').fillna('0')
energy_saved.drop('crude_oil saved', axis=1, inplace=True)
energy_saved.columns = ['Waste_type', 'Energy_saved']
energy_saved = energy_saved.iloc[0:4]
energy_saved['Energy_saved'] = energy_saved['Energy_saved'].str.strip(' Kwh').astype('float64')
energy_saved
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Waste_type</th>
      <th>Energy_saved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Plastic</td>
      <td>5774.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Glass</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ferrous Metal</td>
      <td>642.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Non-Ferrous Metal</td>
      <td>14000.0</td>
    </tr>
  </tbody>
</table>
</div>




Joining Both the Datasets A and B, also assigning the index as Year



```python
rec15 = recy_2003[recy_2003.index >= 2015]
rec15_18 = [rec15, recy_2018]
recy_15_18 = pd.concat(rec15_18)
recy_15_18.sort_index()
recy_15_18.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Waste_type</th>
      <th>Total_waste_recycled</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>Food</td>
      <td>104100.0</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Paper/Cardboard</td>
      <td>603700.0</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Plastics</td>
      <td>57800.0</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>C&amp;D</td>
      <td>1402900.0</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Horticultural waste</td>
      <td>237200.0</td>
    </tr>
  </tbody>
</table>
</div>




Cleaning the data, matching the names with the metrics dataset 

Grouping the data for the 4 materials [Plastic, Ferrous, non ferrous, glass]



```python
w = ['Ferrous metal', 'Glass', 'Plastic', 'Ferrous Metal', 'Plastics', 'Non-Ferrous Metal', 'Non-ferrous metal', 'Non-ferrous metals']
food = recy_15_18[recy_15_18['Waste_type'].isin(w)].groupby(['Year','Waste_type']).sum()
food.reset_index(inplace=True)
food.at[[3,7,15,19],'Waste_type'] = 'Plastic'
food.at[[0,4,8],'Waste_type'] = 'Ferrous Metal'
food.at[[2,6,10,14,18],'Waste_type'] = 'Non-Ferrous Metal'
food.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Waste_type</th>
      <th>Total_waste_recycled</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>Ferrous Metal</td>
      <td>1333300.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>Glass</td>
      <td>14600.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>Non-Ferrous Metal</td>
      <td>160400.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>Plastic</td>
      <td>57800.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Ferrous Metal</td>
      <td>1351500.0</td>
    </tr>
  </tbody>
</table>
</div>




Calculating the energy saved for each material for each year, and adding it as 

a new column in out DataFrame named Food



```python
food['Energy_saved'] = 1
for ind1,row1 in food.iterrows():
    for ind2, row2 in energy_saved.iterrows():
        if row1[1] == row2[0]:
            food['Energy_saved'].iloc[ind1] = row1[2] * row2[1]
food.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Waste_type</th>
      <th>Total_waste_recycled</th>
      <th>Energy_saved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>Ferrous Metal</td>
      <td>1333300.0</td>
      <td>8.559786e+08</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>Glass</td>
      <td>14600.0</td>
      <td>6.132000e+05</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>Non-Ferrous Metal</td>
      <td>160400.0</td>
      <td>2.245600e+09</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>Plastic</td>
      <td>57800.0</td>
      <td>3.337372e+08</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Ferrous Metal</td>
      <td>1351500.0</td>
      <td>8.676630e+08</td>
    </tr>
  </tbody>
</table>
</div>




Finally preparing the data in the desired format

Setting the index as the year column

Grouping by the year column on food dataframe and adding all the values

accordingly in the energy saved column



```python
annual_energy_savings = food.groupby('Year').sum()
annual_energy_savings.drop('Total_waste_recycled', inplace=True, axis=1)
annual_energy_savings.reset_index(inplace=True)
annual_energy_savings.columns = ['year', 'total_energy_saved']
annual_energy_savings.set_index('year', inplace=True)
annual_energy_savings
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_energy_saved</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>3.435929e+09</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>2.554433e+09</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>2.470596e+09</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>2.698130e+09</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>2.765440e+09</td>
    </tr>
  </tbody>
</table>
</div>




```python
%%nose

import pandas as pd
import re
import numpy as np

convert_index = lambda x: [re.match('(\d{4})', date).group(0) for date in x.index.values.astype(str)]

test_solution = pd.DataFrame({'year': [2015, 2016, 2017, 2018, 2019],\
                             'total_energy_saved': [3.435929e+09, 2554433400, 2.470596e+09, 2.698130e+09,
       2.765440e+09]}).set_index('year')

def test_project():
    
    # Check whether the answer has been saved and is a DataFrame
    assert 'annual_energy_savings' in globals() and type(annual_energy_savings) == pd.core.frame.DataFrame, \
    "Have you assigned your answer to a DataFrame named `annual_energy_savings`?"
    
    # Check whether they have the right column in their DataFrame
    assert annual_energy_savings.columns.isin(['total_energy_saved']).any(), \
    "Your DataFrame is missing the required column!"
    
    # Check whether they have included the correct index
    assert annual_energy_savings.index.name == 'year', \
    "Your DataFrame is missing the required index!"
    
    # Check whether the values (converted to an integer) contain in the only column are correct
    # and check whether the index is identical
    assert (test_solution.total_energy_saved.astype('int64').values == \
    annual_energy_savings.total_energy_saved.astype('int64').values).all()\
    and convert_index(test_solution) == convert_index(annual_energy_savings), \
    "Your submitted DataFrame does not contain the correct values!"
```






    1/1 tests passed



