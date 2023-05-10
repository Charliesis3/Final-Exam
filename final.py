#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:51:57 2023

@author: charliesiciliano
"""

import pandas as pd
import numpy as np

# Read in the data
gas_prices = pd.read_csv("gasoline_prices.csv")
state_codes = pd.read_csv("state_abb_codes.csv")
census_regions = pd.read_csv("censusRegions.csv")

# Merge data
StateCode_GasPrice = pd.merge(state_codes, gas_prices, on='State')

# Create data frame with state code name and corresponding regular and diesel prices
type_gas = ["Code", "Regular", "Diesel"]
gp_name = StateCode_GasPrice[type_gas]

# Merge data with census_regions to include regions
gp_ByRegion = pd.merge(gp_name, census_regions, left_on='Code', right_on='State')

# Remove Washington DC
gp_ByRegion_NoDC = gp_ByRegion[gp_ByRegion['Code'] != 'DC']

# Group by region and calculate percent increase, standard deviation, and coefficient of variation
Result = gp_ByRegion_NoDC.groupby(['Region']).agg(mean_pct_increase=('Diesel', 'mean'), 
                                                  sd_pct_increase=('Diesel', 'std'),
                                                  coef_pct_increase=('Diesel', lambda x: np.std(x) / np.mean(x)),
                                                 )
print(Result)

  Region    mean_pct_increase  sd_pct_increase  coef_pct_increase        
  Midwest   50.39880         7.925107           0.157248      
  Northeast 55.81640         3.024418           0.054185
   South    57.35056         3.885083           0.06774
    West     3.30957        14.069044           0.422372
