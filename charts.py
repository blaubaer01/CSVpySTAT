#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:59:18 2022

@author: blaubaer
"""

import pandas as pd
from tabulate import tabulate
from tksheet import Sheet
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as spy
from scipy.stats import shapiro

import numpy as np
from outliers import smirnov_grubbs as grubbs
from tableview import file_in_html


def boxplot_single(df, messwert, lt, ut):
    print('Simple Boxplot \n')
    
    lt = float(lt)
    ut = float(ut)
        
    df.boxplot(column=messwert, widths=0.5)
    plt.axhline(y=ut,linewidth=2, color='red')
    plt.axhline(y=lt,linewidth=2, color='red')    
    plt.show()
    
    