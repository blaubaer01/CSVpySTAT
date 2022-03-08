#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:36:30 2022

@author: blaubaer
"""
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as spy
from scipy.stats import shapiro
import pandas as pd

def qq_plot(df, messwert):
    
    print('Q-Q-Plot \n')
        
    y = df[messwert]
    
    
    spy.stats.probplot(y, dist="norm", plot=plt)
    plt.show() 

def histogram(df, messwert):
    print('Histogram')
    
    y=df[messwert]
    
    sns.displot(y, kde=True)
    
    plt.show()

###test of normality
def normality_test(df, messwert):
    #clear()
    print('Test of normal distribution \n')
        
    y = df[messwert]
    
    stat, p = shapiro(y)
    
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
        decision = 'Sample looks Gaussian (fail to reject H0)'
    else:
        print('Sample does not look Gaussian (reject H0)')
        decision = 'Sample does not look Gaussian (reject H0)'
    

    eintrag = 'Shapiro-Wilk - Test:' + '\nStatistics: ' + str(stat) + '\np-Value: ' + str(p) + '\ndecision: ' + decision
    
    plt.figure(figsize=(6,2))
    plt.subplot(211)
    spy.stats.probplot(y, dist="norm", plot=plt)
    
    plt.subplot(212)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.show() 

