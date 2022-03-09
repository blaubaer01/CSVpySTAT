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

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

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

def CPA(df, messwert, lt, ut):    
            
    sns.set(color_codes=True)
    
    #label_chart = ('Capability Analysis')
    
    print('Capability Analysis \n')
    
    
    
    
    #y = messwert
    if lt !='':
        lt = float(lt)
    if ut !='':
        ut = float(ut)
       
    y = df[messwert]
    
    print('Data-overview choosed column:')
    print(y)
    
    
    if ut =='':
        if lt =='':
            toleranz ='ohne'
    
    if ut !='':
        if lt !='':
            toleranz =''
    
    if ut !='':
        if lt =='':
            toleranz ='einseitig oben'
    
    if ut =='':
        if lt !='':
            toleranz ='einseitig unten'
    
    print (toleranz)    
    
    count_y = y.count()
    if count_y < 25:
        texteintrag='\n' + '#'*30 + '\nUnter 25 Werte wird keine Fähigketsstudie durchgeführt. Ausgewählte Datenmenge: ' + str(count_y) + '\n' + '#'*30 
        print(texteintrag)
        
        
    else:
        
        if count_y < 50:
            proa, pr = 'Cmk', 'Cm'
        elif count_y < 250:
            proa, pr = 'Ppk', 'Pp'
        else:
            proa, pr = 'Cpk', 'Cp'
        
        ###both side tolerance
            
        stat, p = shapiro(y)
        
        print('p-Value: ', p)
        ###both side tolerance / normaldistribution
        if p >= 0.05:
        #normal verteilt
            text = 'distribution should follow normal distribution'    
            
            ##graphic
            
            
            if toleranz =='':
            
                print('both side tolerance - normal distribution')
            #calculation cp/cpk
                mean_y = y.mean()
                std_y = y.std()
                
                cp = (ut-lt) / (6*std_y)
                cpkut = (ut-mean_y)/(3*std_y)
                cpklt = (mean_y-lt)/(3*std_y)
                cpk = min(cpkut, cpklt)
                mean_p_3s = mean_y + 3*std_y
                mean_m_3s = mean_y - 3*std_y
                min_y = y.min()
                max_y = y.max()
                cpk = truncate(cpk, 3)
                cp = truncate(cp, 3)
                mean_y = truncate(mean_y, 5)
                std_y = truncate(std_y, 5)
                mean_p_3s = truncate(mean_p_3s, 5)
                mean_m_3s = truncate(mean_m_3s, 5)
                min_y = truncate(min_y, 5)
                max_y =truncate(max_y, 5)
                count_y = truncate(count_y, 0)
                
                
                
                
                
                print(mean_y,std_y , cp, cpk)
                #text = 'distribution should follow normal distribution'
                eintrag = 'Mean: ' + str(mean_y) + ' s: ' + str(std_y) + '\n+3s: ' + str(mean_p_3s) + '\n-3s: ' + str(mean_m_3s) + '\n' + pr + ': ' + str(cp) + '\n' + proa + ': ' + str(cpk) + '\nUT: ' + str(ut) + ' LT: ' + str(lt) + '\nMIN: ' + str(min_y) + ' MAX: '+ str(max_y) + '\nn: ' + str(count_y) + '\n' + text + '\n'
                plt.figure(figsize=(6, 4))
                plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
                sns.histplot(x=y)
                plt.title("Process Capability Analyse \n")
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(222)
                spy.stats.probplot(y, dist="norm", plot=plt)
                plt.subplot(223)
                sns.boxplot(x=y)
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(224)
                plt.text(0.1,0.5,eintrag, 
                         ha='left', va='center',
                         fontsize=12)
                plt.axis('off')
                #plt.title(label_chart, fontdict=None, loc='center', pad=None)
                plt.show()
            
            elif toleranz =='einseitig oben':
                
                print('one side tolerance ut / normal distribution')
            
                mean_y = y.mean()
                std_y = y.std()
                
                cpkut = (ut-mean_y)/(3*std_y)
                cpk = cpkut
                mean_p_3s = mean_y + 3*std_y
                mean_m_3s = mean_y - 3*std_y
                min_y = y.min()
                max_y = y.max()
                
                
                
                cpk = truncate(cpk, 3)
                mean_y = truncate(mean_y, 5)
                std_y = truncate(std_y, 5)
                mean_p_3s = truncate(mean_p_3s, 5)
                mean_m_3s = truncate(mean_m_3s, 5)
                min_y = truncate(min_y, 5)
                max_y =truncate(max_y, 5)
                count_y = truncate(count_y, 0)
                #text = 'distribution should follow normal distribution'
                eintrag = 'Mean: ' + str(mean_y) + ' s:' + str(std_y) + '\n+3s: ' + str(mean_p_3s) + '\n-3s: ' + str(mean_m_3s) + '\n' + proa + ': ' + str(cpk) + '\nUT: ' + str(ut) + '\nMIN: ' + str(min_y) + ' MAX: '+ str(max_y) + '\nn: ' + str(count_y)+ '\n' + text + '\n' 
                    
                    
                
                
                plt.figure(figsize=(6, 4))
                plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
                sns.histplot(x=y)
                plt.title("Process Capability Analyse ")
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.subplot(222)
                spy.stats.probplot(y, dist="norm", plot=plt)
                plt.subplot(223)
                sns.boxplot(x=y)
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.subplot(224)
                plt.text(0.1,0.5,eintrag, 
                         ha='left', va='center',
                         fontsize=12)
                plt.axis('off')
                #plt.title(label_chart, fontdict=None, loc='center', pad=None)
                plt.show()
            
            elif toleranz =='einseitig unten':
                
                print('one side tolerance /normal distribution')
            
                mean_y = y.mean()
                std_y = y.std()
                
                cpklt = (mean_y-lt)/(3*std_y)
                cpk = cpklt
                
                mean_p_3s = mean_y + 3*std_y
                mean_m_3s = mean_y - 3*std_y
                min_y = y.min()
                max_y = y.max()
                
                
                cpk = truncate(cpk, 3)
                mean_y = truncate(mean_y, 5)
                std_y = truncate(std_y, 5)
                mean_p_3s = truncate(mean_p_3s, 5)
                mean_m_3s = truncate(mean_m_3s, 5)
                min_y = truncate(min_y, 5)
                max_y =truncate(max_y, 5)
                count_y = truncate(count_y, 0)            
                #text = 'distribution should follow normal distribution'
                
                eintrag = 'Mean: ' + str(mean_y) + ' s:' + str(std_y) + '\n+3s: ' + str(mean_p_3s) + '\n-3s: ' + str(mean_m_3s) + '\n' + proa + ': ' + str(cpk) + '\nLT: ' + str(lt) + '\nMIN: ' + str(min_y) + ' MAX: '+ str(max_y) + '\nn: ' + str(count_y) + '\n' + text + '\n' 

                
                
                
                plt.figure(figsize=(6, 4))
                plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
                sns.histplot(x=y)
                plt.title("Process Capability Analyse ")
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(222)
                spy.stats.probplot(y, dist="norm", plot=plt)
                plt.subplot(223)
                sns.boxplot(x=y)
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(224)
                plt.text(0.1,0.5,eintrag, 
                         ha='left', va='center',
                         fontsize=12)
                plt.axis('off')
                #plt.title(label_chart, fontdict=None, loc='center', pad=None)
                plt.show()
            
            
            elif toleranz=='ohne':
                print('Ohne Toleranz ist keine Fähigkeitsanalyse möglich')
        
        ###both side tolerance / other distribution
        elif p < 0.05:
        #nicht normalverteilt
            print('both side tolerance other distribution')
            text = 'distribution should not follow normal distribution'
            
            
            
            ##graphic
            if toleranz =='':
                
                median_y = y.quantile(0.5)
            
                upper_q_y = y.quantile(0.99869)
                
                lower_q_y = y.quantile(0.00135)
                min_y = y.min()
                max_y = y.max()
                
                
                
                cp = (ut-lt) / (upper_q_y - lower_q_y)
                cpkut = (ut-median_y)/(upper_q_y-median_y)
                cpklt = (median_y-lt)/(median_y-lower_q_y)
                cpk = min(cpkut,cpklt)
                cpk = truncate(cpk, 3)
                cp = truncate(cp, 3)
                median_y = truncate(median_y, 5)
                upper_q_y = truncate(upper_q_y, 5)
                lower_q_y = truncate(lower_q_y, 5)
                min_y = truncate(min_y, 5)
                max_y =truncate(max_y, 5)
                count_y = truncate(count_y, 0)
                
                print(median_y ,upper_q_y, lower_q_y , cp, cpk)
                #text = 'distribution should not follow normal distribution'
                eintrag = 'Median: ' + str(median_y) + '\nQ0.998: ' + str(upper_q_y) + '\nQ0.001: ' + str(lower_q_y) + '\n' + pr + ': ' + str(cp) + '\n' + proa + ': ' + str(cpk) + '\nUT: ' + str(ut) + ' LT: ' + str(lt) + '\nMIN: ' + str(min_y) + ' MAX: '+ str(max_y) + '\nn: ' + str(count_y) + '\n' + text + '\n'
                print(eintrag)
                plt.figure(figsize=(6, 4))
                plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
                sns.histplot(x=y)
                plt.title("Process Capability Analyse ")
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(222)
                spy.stats.probplot(y, dist="norm", plot=plt)
                plt.subplot(223)
                sns.boxplot(x=y)
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(224)
                plt.text(0.1,0.5,eintrag, 
                         ha='left', va='center',
                         fontsize=12)
                plt.axis('off')
                #plt.title(label_chart, fontdict=None, loc='center', pad=None)
                plt.show()
            
            elif toleranz =='einseitig oben':
                
                median_y = y.quantile(0.5)
                upper_q_y = y.quantile(0.99869)
                lower_q_y = y.quantile(0.00135)
                min_y = y.min()
                max_y = y.max()
                
                
                
                cpkut = (ut-median_y)/(upper_q_y-median_y)
                cpk = cpkut
                
                cpk = truncate(cpk, 3)
                median_y = truncate(median_y, 5)
                upper_q_y = truncate(upper_q_y, 5)
                lower_q_y = truncate(lower_q_y, 5)
                min_y = truncate(min_y, 5)
                max_y =truncate(max_y, 5)
                count_y = truncate(count_y, 0)
                #text = 'distribution should not follow normal distribution'
                
                eintrag = 'Median: ' + str(median_y) + '\nQ0.998: ' + str(upper_q_y) + '\nQ0.001: ' + str(lower_q_y) + '\n' + proa + ': ' + str(cpk) + '\nUT: ' + str(ut) + '\nMIN: ' + str(min_y) + ' MAX: '+ str(max_y) + '\nn: ' + str(count_y)+ '\n' + text + '\n' 
                    
                
                
                    
                
                plt.figure(figsize=(6, 4))
                plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
                sns.histplot(x=y)
                plt.title("Process Capability Analyse " + bauteilnummer + " " + iqs +"\nMerkmal: " + str(merkmal) + "\nMaschine: " + maschine)
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.subplot(222)
                spy.stats.probplot(y, dist="norm", plot=plt)
                plt.subplot(223)
                sns.boxplot(x=y)
                plt.axvline(x=ut,linewidth=2, color='r')
                plt.subplot(224)
                plt.text(0.1,0.5,eintrag, 
                         ha='left', va='center',
                         fontsize=12)
                plt.axis('off')
                #plt.title(label_chart, fontdict=None, loc='center', pad=None)
                plt.show()
            
            elif toleranz =='einseitig unten':
                median_y = y.quantile(0.5)
                upper_q_y = y.quantile(0.99869)
                lower_q_y = y.quantile(0.00135)
                min_y = y.min()
                max_y = y.max()
                
                
                cpklt = (median_y-lt)/(median_y-lower_q_y)
                cpk = cpklt
            
                cpk = truncate(cpk, 3)
                median_y = truncate(median_y, 5)
                upper_q_y = truncate(upper_q_y, 5)
                lower_q_y = truncate(lower_q_y, 5)
                min_y = truncate(min_y, 5)
                max_y =truncate(max_y, 5)
                count_y = truncate(count_y, 0)            
                #text = 'distribution should not follow normal distribution'
                
                eintrag = 'Median: ' + str(median_y) + '\nQ0.998: ' + str(upper_q_y) + '\nQ0.001: ' + str(lower_q_y) + '\n' + proa + ': ' + str(cpk) + '\nLT: ' + str(lt) + '\nMIN: ' + str(min_y) + ' MAX: '+ str(max_y) + '\nn: ' + str(count_y) + '\n' + text + '\n'
                plt.figure(figsize=(6, 4))
                plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
                sns.histplot(x=y)
                plt.title("Process Capability Analyse ")
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(222)
                spy.stats.probplot(y, dist="norm", plot=plt)
                plt.subplot(223)
                sns.boxplot(x=y)
                plt.axvline(x=lt,linewidth=2, color='r')
                plt.subplot(224)
                plt.text(0.1,0.5,eintrag, 
                         ha='left', va='center',
                         fontsize=12)
                plt.axis('off')
                #plt.title(label_chart, fontdict=None, loc='center', pad=None)
                plt.show()
            elif toleranz=='ohne':
                print('Ohne Toleranz ist keine Fähigkeitsanalyse möglich')