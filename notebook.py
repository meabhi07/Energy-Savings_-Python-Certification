#!/usr/bin/env python
# coding: utf-8

# ## Energy saved from recycling
# <p>Did you know that recycling saves energy by reducing or eliminating the need to make materials from scratch? For example, aluminum can manufacturers can skip the energy-costly process of producing aluminum from ore by cleaning and melting recycled cans. Aluminum is classified as a non-ferrous metal.</p>
# <p>Singapore has an ambitious goal of becoming a zero-waste nation. The amount of waste disposed of in Singapore has increased seven-fold over the last 40 years. At this rate, Semakau Landfill, Singapore’s only landfill, will run out of space by 2035. Making matters worse, Singapore has limited land for building new incineration plants or landfills.</p>
# <p>The government would like to motivate citizens by sharing the total energy that the combined recycling efforts have saved every year. They have asked you to help them.</p>
# <p>You have been provided with three datasets. The data come from different teams, so the names of waste types may differ.</p>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:16px"><b>datasets/wastestats.csv - Recycling statistics per waste type for the period 2003 to 2017</b>
#     </div>
#     <div>Source: <a href="https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling">Singapore National Environment Agency</a></div>
# <ul>
#     <li><b>waste_type: </b>The type of waste recycled.</li>
#     <li><b>waste_disposed_of_tonne: </b>The amount of waste that could not be recycled (in metric tonnes).</li>
#     <li><b>total_waste_recycle_tonne: </b>The amount of waste that could be recycled (in metric tonnes).</li>
#     <li><b>total_waste_generated: </b>The total amount of waste collected before recycling (in metric tonnes).</li>
#     <li><b>recycling_rate: </b>The amount of waste recycled per tonne of waste generated.</li>
#     <li><b>year: </b>The recycling year.</li>
# </ul>
#     </div>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6; margin-top: 17px;">
#     <div style="font-size:16px"><b>datasets/2018_2019_waste.csv - Recycling statistics per waste type for the period 2018 to 2019</b>
#     </div>
#     <div> Source: <a href="https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling">Singapore National Environment Agency</a></div>
# <ul>
#     <li><b>Waste Type: </b>The type of waste recycled.</li>
#     <li><b>Total Generated: </b>The total amount of waste collected before recycling (in thousands of metric tonnes).</li> 
#     <li><b>Total Recycled: </b>The amount of waste that could be recycled. (in thousands of metric tonnes).</li>
#     <li><b>Year: </b>The recycling year.</li>
# </ul>
#     </div>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6; margin-top: 17px;">
#     <div style="font-size:16px"><b>datasets/energy_saved.csv -  Estimations of the amount of energy saved per waste type in kWh</b>
#     </div>
# <ul>
#     <li><b>material: </b>The type of waste recycled.</li>
#     <li><b>energy_saved: </b>An estimate of the energy saved (in kiloWatt hour) by recycling a metric tonne of waste.</li> 
#     <li><b>crude_oil_saved: </b>An estimate of the number of barrels of oil saved by recycling a metric tonne of waste.</li>
# </ul>
# 
# </div>
# <pre><code>
# </code></pre>

# In[118]:


# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd


# 
# Cleaning and importing the first dataset which contains values from year 2003 to 
# 
# 2017 : Refer to it as Dataset 'A'
# 

# In[119]:


names = ['Waste_type', 'Total_waste_recycled', 'Year']
recy_2003 = pd.read_csv('datasets/wastestats.csv')
recy_2003.drop(['waste_disposed_of_tonne', 'total_waste_generated_tonne','recycling_rate'], inplace=True, axis=1)
recy_2003.columns = ['Waste_type', 'Total_waste_recycled', 'Year']
recy_2003.set_index('Year', inplace=True)
recy_2003['Total_waste_recycled'] = recy_2003['Total_waste_recycled']
recy_2003.sort_index(ascending=True, inplace=True)
recy_2003.head()


# 
# Cleaning and importing the first dataset which contains values from year 2018 
# 
# to 2019: Refer to it as Dataset 'B'
# 

# In[120]:


recy_2018 = pd.read_csv('datasets/2018_2019_waste.csv')

recy_2018.drop('Total Generated (\'000 tonnes)', inplace=True, axis=1)
recy_2018.columns = names
recy_2018['Total_waste_recycled'] = recy_2018['Total_waste_recycled']*1000
recy_2018.set_index('Year', inplace=True)
recy_2018.sort_index(ascending=True, inplace=True)
recy_2018.head()


# 
# The table gives the amount of energy saved in kilowatt hour (kWh) and 
# 
# the amount of crude oil (barrels) by recycling 1 metric tonne (1000 kilogram) 
# 
# per waste type
# 

# 
# Importing and cleaning the conversion table, 
# 
# also refer to above cell for the conversion metrics
# 

# In[121]:


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


# 
# Joining Both the Datasets A and B, also assigning the index as Year
# 

# In[122]:


rec15 = recy_2003[recy_2003.index >= 2015]
rec15_18 = [rec15, recy_2018]
recy_15_18 = pd.concat(rec15_18)
recy_15_18.sort_index()
recy_15_18.head()


# 
# Cleaning the data, matching the names with the metrics dataset 
# 
# Grouping the data for the 4 materials [Plastic, Ferrous, non ferrous, glass]
# 

# In[123]:


w = ['Ferrous metal', 'Glass', 'Plastic', 'Ferrous Metal', 'Plastics', 'Non-Ferrous Metal', 'Non-ferrous metal', 'Non-ferrous metals']
food = recy_15_18[recy_15_18['Waste_type'].isin(w)].groupby(['Year','Waste_type']).sum()
food.reset_index(inplace=True)
food.at[[3,7,15,19],'Waste_type'] = 'Plastic'
food.at[[0,4,8],'Waste_type'] = 'Ferrous Metal'
food.at[[2,6,10,14,18],'Waste_type'] = 'Non-Ferrous Metal'
food.head()


# 
# Calculating the energy saved for each material for each year, and adding it as 
# 
# a new column in out DataFrame named Food
# 

# In[124]:


food['Energy_saved'] = 1
for ind1,row1 in food.iterrows():
    for ind2, row2 in energy_saved.iterrows():
        if row1[1] == row2[0]:
            food['Energy_saved'].iloc[ind1] = row1[2] * row2[1]
food.head()


# 
# Finally preparing the data in the desired format
# 
# Setting the index as the year column
# 
# Grouping by the year column on food dataframe and adding all the values
# 
# accordingly in the energy saved column
# 

# In[125]:


annual_energy_savings = food.groupby('Year').sum()
annual_energy_savings.drop('Total_waste_recycled', inplace=True, axis=1)
annual_energy_savings.reset_index(inplace=True)
annual_energy_savings.columns = ['year', 'total_energy_saved']
annual_energy_savings.set_index('year', inplace=True)
annual_energy_savings


# In[126]:


get_ipython().run_cell_magic('nose', '', '\nimport pandas as pd\nimport re\nimport numpy as np\n\nconvert_index = lambda x: [re.match(\'(\\d{4})\', date).group(0) for date in x.index.values.astype(str)]\n\ntest_solution = pd.DataFrame({\'year\': [2015, 2016, 2017, 2018, 2019],\\\n                             \'total_energy_saved\': [3.435929e+09, 2554433400, 2.470596e+09, 2.698130e+09,\n       2.765440e+09]}).set_index(\'year\')\n\ndef test_project():\n    \n    # Check whether the answer has been saved and is a DataFrame\n    assert \'annual_energy_savings\' in globals() and type(annual_energy_savings) == pd.core.frame.DataFrame, \\\n    "Have you assigned your answer to a DataFrame named `annual_energy_savings`?"\n    \n    # Check whether they have the right column in their DataFrame\n    assert annual_energy_savings.columns.isin([\'total_energy_saved\']).any(), \\\n    "Your DataFrame is missing the required column!"\n    \n    # Check whether they have included the correct index\n    assert annual_energy_savings.index.name == \'year\', \\\n    "Your DataFrame is missing the required index!"\n    \n    # Check whether the values (converted to an integer) contain in the only column are correct\n    # and check whether the index is identical\n    assert (test_solution.total_energy_saved.astype(\'int64\').values == \\\n    annual_energy_savings.total_energy_saved.astype(\'int64\').values).all()\\\n    and convert_index(test_solution) == convert_index(annual_energy_savings), \\\n    "Your submitted DataFrame does not contain the correct values!"')

