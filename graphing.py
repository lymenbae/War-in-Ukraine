#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:57:12 2022

@author: lymenbae
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import csv
import os
#%% #Reading the Data
equip_loss=pd.read_csv('russia_losses_equipment.csv')
equip_loss=equip_loss.set_index("day")
person_loss=pd.read_csv("russia_losses_personnel.csv")
person_loss=person_loss.set_index("day")
person_loss=person_loss.drop(['personnel*'],axis=1)
#%%
fig,ax1=plt.subplots()
sns.lineplot(data=person_loss,x='day',y='personnel').set(title="Number of Russian soldiers dead")
fig.tight_layout()
fig.savefig("Number of Russian soldiers lost")
#%%
fig,ax1=plt.subplots()
sns.lineplot(data=person_loss,x='day',y='POW').set(title="Number of Russian Prisoners of War in Ukraine")
fig.tight_layout()
fig.savefig("Russian Prisoners of War in Ukraine")
#%%

