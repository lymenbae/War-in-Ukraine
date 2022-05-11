#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:53:45 2022

@author: lymenbae
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import csv
import os
import datapane as dp
#%% #Reading the Data
equip_loss=pd.read_csv('russia_losses_equipment.csv')
person_loss=pd.read_csv("russia_losses_personnel.csv")
#Dropping the unnecessary column
person_loss=person_loss.drop(['personnel*'],axis=1) 
#%% 
person_loss.head(10)
#Sets index for sorting by date
person_loss.set_index('date',inplace=True)
person_loss.info()
#%%
#The description of the machinery and military equipment that Russia has lost
equip_loss.head(10)
#Filling empty spaces with zeroes
equip_loss=equip_loss.fillna(0)
equip_loss.set_index('date', inplace=True)
#%%
#Creating the new dataframe with the columnns that we are going to work with
pow_data = person_loss[["day", "POW"]]
pow_data.reset_index('date', inplace=True)
#adding the new line that would show the increase trendline
last = 0
increase = []
for i in (pow_data['POW'].values):
    count = i - last
    increase.append(count)
    last = i
#%%
#Graphing the differences
fig,ax1=plt.subplots()
pow_data['Daily_Increase_in_Prisoners_of_War'] = increase
pow_data_ = pow_data[['date', 'POW', 'Daily_Increase_in_Prisoners_of_War']].set_index('date')
pow_data_.plot(figsize=(16,6))
plt.xlabel('Days since Invasion')
plt.ylabel('Count of Prisoners')
plt.title("Total Daily Prisoner of War VS Daily Increase in Prisoners of War")
plt.show()
fig.savefig("Increase in Prisoners of War vs the Total Amount.png")
#%%
#Merging the two datasets
merged=equip_loss.merge(person_loss,how='outer',validate='1:1',indicator=True)
#Plotting the correlations
(fig1,ax1)=plt.subplots(dpi=300)
merged = pd.merge(equip_loss, person_loss).drop(['day'], axis=1)
merged = merged.corr()['POW'].sort_values(ascending=False)
merged.plot.barh(title='Correlation (POW) & Equipment Loss by Russia',
                 figsize=(10,8),alpha=.9,color='black')
#Looping over data for the frequency correlation and rounding the value to 3 digits
#enumerate function allows to iterate through a sequence but it keeps track of both the index and the element. 
for index, value in enumerate(merged):
    value=round(value,3)
    label = format(value)
    plt.annotate(label, xy=(value-.1, index-.1), color='white')
fig1.tight_layout()
fig1.savefig("POW and Equipment Loss Correlation")
#Looking at the Equipment Losses:
equip_loss.describe()
#categorizing the units for air, ground and naval categories
#This will better show the total losses for equipment
air_units = ['helicopter', 'aircraft', 'drone']
naval_units = ['naval ship']
ground_units = ['APC', 'military auto', 'tank', 'field artillery', 'fuel tank', 'MRL','anti-aircraft warfare', 'special equipment', 'mobile SRBM system']
equip_loss['Total Air Units'] = equip_loss[air_units].sum(axis=1)
equip_loss['Total Naval Units'] = equip_loss[naval_units].sum(axis=1)
equip_loss['Total Ground Units'] = equip_loss[ground_units].sum(axis=1)
equip_loss.head(50)
#Because the console didn't show the whole output, I created another dataframe
equip_loss.columns

equip_loss2 = equip_loss[['Total Air Units', 'Total Naval Units', 'Total Ground Units']]
equip_loss2.head(50)
#%%
fig,ax1=plt.subplots()
equip=sns.lineplot(data=equip_loss).set(title="Total Equipment Losses")
sns.move_legend(equip, "bottom left", bbox_to_anchor=(1, 1))
fig.savefig("Total Equipment Losses.png")
#%%

