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



############################statistic variables
#########################################################################################
# n   0 1     2      3      4      5      6      7      8      9      10
A2 = [0,0, 1.880, 1.023, 0.729, 0.577, 0.483, 0.419, 0.373, 0.337, 0.308]
D3 = [0,0, 0,     0,     0,     0,     0,     0.076, 0.136, 0.184, 0.223]
D4 = [0,0, 3.267, 2.575, 2.282, 2.115, 2.004, 1.924, 1.864, 1.816, 1.777]
# n   0 1      2      3      4      5      6      7      8      9     10     11     12     13     14     15       20     25
c4 = [0,0,0.7979,0.8862,0.9213,0.9400,0.9515,0.9594,0.9650,0.9693,0.9727,0.9754,0.9776,0.9794,0.9810,0.9823]#,0.9869,0.9896]
B3 = [0,0,     0,     0,     0,     0, 0.030, 0.118, 0.185, 0.239, 0.284, 0.321, 0.354, 0.382, 0.406, 0.428]#, 0.510, 0.565]
B4 = [0,0, 3.267, 2.568, 2.266, 2.089, 1.970, 1.882, 1.815, 1.761, 1.716, 1.679, 1.646, 1.618, 1.594, 1.572]#, 1.490, 1.435]
B5 = [0,0,     0,     0,     0,     0, 0.029, 0.113, 0.179, 0.232, 0.276, 0.313, 0.346, 0.374, 0.399, 0.421]#, 0.504, 0.559]
B6 = [0,0, 2.606, 2.276, 2.088, 1.964, 1.874, 1.806, 1.751, 1.707, 1.669, 1.637, 1.610, 1.585, 1.563, 1.544]#, 1.470, 1.420]
A3 = [0,0, 2.659, 1.954, 1.628, 1.427, 1.287, 1.182, 1.099, 1.032, 0.975, 0.927, 0.886, 0.850, 0.817, 0.789]#, 0.680, 0.606]
#########################################################################################
        
######################################################################        





def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def boxplot_single(df, messwert, lt, ut):
    print('Simple Boxplot \n')
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        df.boxplot(column=messwert, widths=0.5)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        df.boxplot(column=messwert, widths=0.5)
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        df.boxplot(column=messwert, widths=0.5)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        df.boxplot(column=messwert, widths=0.5)
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


def boxplot1f(df, messwert, lt, ut, spdt):
    print('Boxplot one factor \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.boxplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.boxplot(x=x, y=y, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.boxplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.boxplot(x=x, y=y, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


def boxplot2f(df, messwert, lt, ut, spdt, factorx):
    print('Boxplot two factors \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.boxplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.boxplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.boxplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.boxplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()

    
def violin_single(df, messwert, lt, ut):
    print('Simple Violinplot \n')
    
    print('ut:',ut)
    print('lt:', lt)
    
    y = messwert
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.violinplot(y=y, data = df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.violinplot(y=y, data = df)
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.violinplot(y=y, data = df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.violinplot(y=y, data = df)
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()

def violin1f(df, messwert, lt, ut, spdt):
    print('Violinplot one factor \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.violinplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.violinplot(x=x, y=y, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.violinplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.violinplot(x=x, y=y, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


def violin2f(df, messwert, lt, ut, spdt, factorx):
    print('Violinplot two factors \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.violinplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.violinplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.violinplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.violinplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()






def stripplot_single(df, messwert, lt, ut):
    print('Simple Stripplot \n')
    
    print('ut:',ut)
    print('lt:', lt)
    
    y = messwert
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.stripplot(y=y, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.stripplot(y=y, data=df)
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.stripplot(y=y, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.stripplot(y=y, data=df)
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


def strip1f(df, messwert, lt, ut, spdt):
    print('Stripplot one factor \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.stripplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.stripplot(x=x, y=y, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.stripplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.stripplot(x=x, y=y, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


def strip2f(df, messwert, lt, ut, spdt, factorx):
    print('Stripplot two factors \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.stripplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.stripplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.stripplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.stripplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


def swarmplot_single(df, messwert, lt, ut):
    print('Simple swarmplot \n')
    
    print('ut:',ut)
    print('lt:', lt)
    
    y = messwert
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.swarmplot(y=y, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.swarmplot(y=y, data=df)
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.swarmplot(y=y, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.swarmplot(y=y, data=df)
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


def swarmplot1f(df, messwert, lt, ut, spdt):
    print('Swarmplot one factor \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.swarmplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.swarmplot(x=x, y=y, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.swarmplot(x=x, y=y, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.swarmplot(x=x, y=y, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()

def swarmplot2f(df, messwert, lt, ut, spdt, factorx):
    print('Swarmplot two factors \n')
    sns.set(style="whitegrid")
    y = messwert
    x = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.swarmplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        sns.swarmplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.swarmplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.swarmplot(x=x, y=y, hue=factorx, data=df, palette="Set3")
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()


#Beschreibende Statistik
def besch_stat(df, messwert):
    
    
    
    y = df[messwert]
    y_val = messwert
    
    

    print('Descriptive Statistic \n')
    
    df['number'] = range(1, len(df) + 1)
    
    x = df['number']
    stat, p = shapiro(y)
            
    ###one side tolerance ut / normal distribution
    if p >= 0.05:
        #normal verteilt
        print('normal distribution')
        
        mean_y = y.mean()
        std_y = y.std()
        count_y = len(y)
        mean_p_3s = mean_y + 3*std_y
        mean_m_3s = mean_y - 3*std_y
        min_y = y.min()
        max_y = y.max()
        
        t_mean_y = truncate(mean_y, 5)
        t_std_y = truncate(std_y, 5)
        t_mean_p_3s = truncate(mean_p_3s, 5)
        t_mean_m_3s = truncate(mean_m_3s, 5)
        
        text = 'distribution should follow normal distribution'
        
        
        
        
        eintrag = 'Mean: ' + str(t_mean_y) + '\ns: ' + str(t_std_y) + '\n \n+3s: ' + str(t_mean_p_3s) + '\n-3s: ' + str(t_mean_m_3s) + '\n \nMIN: ' + str(min_y) + '\nMAX: '+ str(max_y) + '\nn: ' + str(count_y) + '\n\n' + text
        
        print(eintrag +'\np-value:' + str(p))
        ##graphic
                
        plt.figure(figsize=(6, 4))
        plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
        sns.histplot(y, kde=True)
        plt.title("Descriptive Statistic Value Column: " + messwert)
        plt.subplot(222)
        sns.lineplot(x=x, y=y_val, estimator=None, lw=1, marker='o', data=df)
        #df.plot(y_val)
        plt.axhline(y=mean_y,linewidth=2, color='g')
        plt.axhline(y=mean_p_3s,linewidth=2, color='orange')
        plt.axhline(y=mean_m_3s,linewidth=2, color='orange')
        plt.subplot(223)
        sns.boxplot(x=y)
        plt.subplot(224)
        plt.text(0.1,0.5,eintrag, 
                 ha='left', va='center',
                 fontsize=12)
        plt.axis('off')
        #plt.title(label_chart, fontdict=None, loc='center', pad=None)
        
        plt.show()
        
    else:
        
        median_y = y.quantile(0.5)
                
        upper_q_y = y.quantile(0.99869)
                
        lower_q_y = y.quantile(0.00135)
        min_y = y.min()
        max_y = y.max()
                
        median_y = truncate(median_y, 5)
        upper_q_y = truncate(upper_q_y, 5)
        lower_q_y = truncate(lower_q_y, 5)
        min_y = truncate(min_y, 5)
        max_y =truncate(max_y, 5)
        count_y = len(y)
        
        text = 'distribution should not follow normal distribution'
        
        
        
        
        eintrag = 'Median: ' + str(median_y) + '\n\nQ0.998: '  + str(upper_q_y) + '\nQ0.001: ' + str(lower_q_y) + '\n \nMIN: ' + str(min_y) + '\nMAX: '+ str(max_y) + '\nn: ' + str(count_y) + '\n\n' + text
        
        print(eintrag +'\np-value:' + str(p))
        
        ##graphic
                
        plt.figure(figsize=(6, 4))
        plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
        sns.histplot(y, kde=True)
        plt.title("Descriptive Statistic Value Column: " + messwert)
        plt.subplot(222)
        sns.lineplot(x=x, y=y_val, estimator=None, lw=1, marker='o', data=df)
        #df.plot(y_val)
        plt.axhline(y=median_y,linewidth=2, color='g')
        plt.axhline(y=upper_q_y,linewidth=2, color='orange')
        plt.axhline(y=lower_q_y,linewidth=2, color='orange')
        plt.subplot(223)
        sns.boxplot(x=y)
        plt.subplot(224)
        plt.text(0.1,0.5,eintrag, 
                 ha='left', va='center',
                 fontsize=12)
        plt.axis('off')
        #plt.title(label_chart, fontdict=None, loc='center', pad=None)
        
        plt.show()
    
    #texteintrag = '#'*30 + '\n' + 'Descriptive Statitics' + '\n' + eintrag +'\np-value:' + str(p)+ '\n' + '#'*30
    
    #self.Scrolledtext1.insert(END, texteintrag)

#######################################################################

#Time Series Plot
def trend(df, messwert, lt, ut, spdt):
    print('Time Series Plot')
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    
    
    
    y = messwert
    x = spdt
    #ut = 'UTG'
    #ot = 'OTG'
    yt = df[messwert]

    mean_y = yt.mean()
    
    
    
    df[spdt] = df[spdt].astype('datetime64[ns]')
    
    df = df.sort_values(by=spdt, ascending=1)
    
    
    
    if tolerance == '':
        sns.lineplot(data = df, x=x, y=y, marker='o')
        sns.lineplot(data = df, x=x, y=lt, color='r')
        sns.lineplot(data = df, x=x, y=ut, color='r')
        plt.axhline(y=mean_y,linewidth=2, color='g')
        plt.xticks(rotation=25)
        plt.title("Time Series Plot Column: "+ messwert)
        plt.show()
    elif tolerance == 'einseitig oben':
        sns.lineplot(data = df, x=x, y=y, marker='o')
        
        sns.lineplot(data = df, x=x, y=ut, color='r')
        plt.axhline(y=mean_y,linewidth=2, color='g')
        plt.xticks(rotation=25)
        plt.title("Time Series Plot Column: "+ messwert)
        plt.show()
    
    elif tolerance == 'einseitig unten':
        sns.lineplot(data = df, x=x, y=y, marker='o')
        
        sns.lineplot(data = df, x=x, y=lt, color='r')
        plt.axhline(y=mean_y,linewidth=2, color='g')
        plt.xticks(rotation=25)
        plt.title("Time Series Plot Column: "+ messwert)
        plt.show()
        
    elif tolerance =='ohne':
        sns.lineplot(data = df, x=x, y=y, marker='o')
        
        plt.axhline(y=mean_y,linewidth=2, color='g')
        plt.xticks(rotation=25)
        plt.title("Time Series Plot Column: "+ messwert)
        plt.show()
    
    #texteintrag = '\n' + '#'*30 + '\n' + 'Time Series Plot \nColumn:' + messwert + '\n' + 30*'#'
    
    
    #self.Scrolledtext1.insert(END, texteintrag)


def scatterplot(df,messwert, lt, ut, spdt):
    print('Scatterplot')

    x = messwert
    y = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        df.plot.scatter(y,x)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
            
        df.plot.scatter(y,x)
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        df.plot.scatter(y,x)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        df.plot.scatter(y,x)
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
    
    
def regression_single(df,messwert, lt, ut, spdt):
    
    sns.set(color_codes=True)        
    
    print('Scatter Plot with Regression line linear \n')

    x = messwert
    y = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.regplot(x=x, y=y, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
        sns.regplot(x=x, y=y, data=df)    
        
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.regplot(x=x, y=y, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.regplot(x=x, y=y, data=df)
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()

def regression1f(df,messwert, lt, ut, spdt, factorx):
    
    sns.set(color_codes=True)        
    
    print('Scatter Plot with Regression line linear \n')

    x = messwert
    y = spdt
    
    print('ut:',ut)
    print('lt:', lt)
    
    if lt =='' + ut =='':
        tolerance ='ohne'
        print('erg:', tolerance)
    elif lt !='' + ut =='':
        tolerance ='einseitig unten'
        lt = float(lt)
        print('erg:', tolerance)
    elif ut !='' + lt =='':
        tolerance ='einseitig oben'
        ut = float(ut)
        print('erg:', tolerance)
    elif lt !='' + ut !='':
        tolerance =''
        lt = float(lt)
        ut = float(ut)
        print('erg:', tolerance)
    
    if tolerance =='':
        
            
        sns.lmplot(x=x, y=y, hue=factorx, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
        
    elif tolerance =='ohne':
        
        sns.lmplot(x=x, y=y, hue=factorx, data=df)    
        
        plt.show()
    
    elif tolerance =='einseitig oben':
        
            
        sns.lmplot(x=x, y=y, hue=factorx, data=df)
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.show()
    
    elif tolerance =='einseitig unten':
        
            
        sns.lmplot(x=x, y=y, hue=factorx, data=df)
        
        plt.axhline(y=lt,linewidth=2, color='red')    
        plt.show()
    