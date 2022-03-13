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
import statsmodels.api as sm
from outliers import smirnov_grubbs as grubbs


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
                


def urwertkarte(df, messwert, lt, ut):
    print('Urwertkarte')
   
    
    yt = df[messwert]
    y = messwert
    if ut!='':
        ut = float(ut)
    if lt!='':
        lt = float(lt)

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
    
    print(ut)
    print(lt)
    print('x-Chart')
    
    df['number'] = range(1, len(df) + 1)
    
    
    x = 'number'
    
    mean_y = yt.mean()
    std_y = yt.std()
    plus3s = mean_y + 3*std_y
    minus3s = mean_y -3*std_y
    median = yt.quantile(0.5)
    upper_q_y = yt.quantile(0.99869)
    lower_q_y = yt.quantile(0.00135)
    
    stat, p = shapiro(df[y])
    
    if p < 0.05:
        mittelwert = median
        ut3s = upper_q_y
        lt3s = lower_q_y
        print('Chart-Parameters:')
        print('median:', median )
        print('Quantil(0.99869)', upper_q_y)
        print('Quantil(0.00135)', lower_q_y)
        text = 'distribution should not follow normal distribution'
        eintrag = 'Median: ' + str(median) + '\n' + 'Quantil(0.99869): ' + str(upper_q_y) + '\n' + 'Quantil(0.00135): ' + str(lower_q_y) + '\n' + text + '\n'
        
    else:
        mittelwert = mean_y
        ut3s = plus3s
        lt3s = minus3s
        print('Chart-Parameters:')
        print('mean:', mean_y )
        print('+3s:', plus3s)
        print('-3s', minus3s)
        
        text = 'distribution should follow normal distribution'
        eintrag = 'Mean: ' + str(mean_y) + '\n' + '+3s: ' + str(plus3s) + '\n' + '-3s: ' + str(minus3s) + '\n' + text + '\n'
        print(eintrag)
        
    if toleranz =='ohne':
        df.plot(x, y, style='-o')
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.title("Urwertkarte: " + messwert)
        
        plt.show()
        
    elif toleranz =='einseitig unten':
              
        df.plot(x, y, style='-o')
        
        
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.axhline(y=lt,linewidth=2, color='red')
        plt.title("Urwertkarte: " + messwert)    
        plt.show()
            
    elif toleranz=='einseitig oben':
            
        df.plot(x, y, style='-o')
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.title("Urwertkarte: " + messwert)
        plt.show()
    
        
    elif toleranz=='OT und UT':
    
        df.plot(x, y, style='-o')
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.axhline(y=lt,linewidth=2, color='red')
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.title("Urwertkarte: " + messwert)
        plt.show()

    elif toleranz=='':
    
        df.plot(x, y, style='-o')
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.axhline(y=lt,linewidth=2, color='red')
        plt.axhline(y=ut,linewidth=2, color='red')
        
        plt.title("Urwertkarte: " + messwert)
        plt.show()


# Mittelwert / sKarte


def xquer_s(df, messwert, lt, ut, samplesize):
    print('Xbar / s Chart')
    

    
    y = messwert
    
    if ut!='':
        ut = float(ut)
    if lt!='':
        lt = float(lt)

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
    
    
    datenanz = df[messwert].count()
    
    
    
    
    if samplesize != '':
        n=int(samplesize)
    else:
        samplesize = 2
        n=int(samplesize)
    
    
    print('daten: ',datenanz)
    fact = datenanz/n
    
    fact1 = datenanz//n
    print('fact1:', fact1)
    print('fact:', fact)
    
    anzahl_ausw = fact1 * n
    print('Löschen: ', anzahl_ausw)
    zeilen_loeschen = datenanz - anzahl_ausw
    
    index_del_list = []
    
                   
        
    print('zeile Löschen:',zeilen_loeschen)
    
    zeilen_loeschen = int(zeilen_loeschen)
    if zeilen_loeschen >0:
        a = 0    
    
        for i in range(a, zeilen_loeschen):
            index_del_list.append(a)
            a += 1
            
        
        
            print(index_del_list)
    
    
        df = df.drop(df.index[index_del_list])
    
        
    samplesize=int(samplesize)
    
    fact = datenanz/samplesize
    fact = int(fact)
    
    df['sample'] = pd.Series(range(1, fact +1)).repeat(samplesize).tolist()
    
    
    
    
    df2 = pd.DataFrame()
    
    #df2['mean_istwert'] = df.groupby('Stichprobe')['Istwert'].describe()
    df2 = df.groupby('sample')[y].describe()
    
    
    count_column = len(df2.columns)
    print('columns', count_column)
    print(df2)
    fn2 = 'describe.csv'
    df2.to_csv(fn2, sep=';', decimal=',')
    
    df3 = pd.read_csv(fn2, sep=';' , decimal=',', header=0)

    #print(df3)
    
    x = 'sample'
    y = 'mean'
    s = 'std'
    
    Xbar = df3['mean'].mean()
    sbar = df3['std'].mean()
    
    xlcl = Xbar - A3[samplesize]*sbar
    xucl = Xbar + A3[samplesize]*sbar
    
    slcl = B3[samplesize]*sbar
    sucl = B4[samplesize]*sbar
    
    print('s-bar :', sbar)
    print('X-bar :',  Xbar)
    
    
    tXbar = truncate(Xbar, 5)
    tsbar = truncate(sbar, 5)
    txlcl = truncate(xlcl,5)
    txucl = truncate(xucl, 5)
    tslcl = truncate(slcl,5)
    tsucl = truncate(sucl, 5)
    
    
    eintrag_x = 'Xbar/s Chart' + '\nXbar: ' + str(tXbar) + '\nucl: ' + str(txucl) + '\nlcl: ' + str(txlcl)
    eintrag_s = 'sbar: ' + str(tsbar) + '\nucl: ' +str(tsucl) + '\nlcl: ' + str(tslcl)
    
    print('statistical values of the Xbar/s Chart \n')
    print('Xbar-Chart:')
    print(eintrag_x  + '\n')
    print('s-Chart:')
    print(eintrag_s)
    
    plt.figure(figsize=(6, 4))
    
    #df3.plot(x, y, ax=axes[0])
    plt.subplot(221)
    sns.lineplot(x=x, y=y, estimator=None, lw=1, marker='o', data=df3)
    plt.axhline(y=Xbar,linewidth=2, color='g')
    plt.axhline(y=xlcl,linewidth=2, color='orange')
    plt.axhline(y=xucl,linewidth=2, color='orange')
    plt.title("Xbar/s Chart" + messwert)
    #df3.plot(x, s, ax = axes[1])
    plt.subplot(222)
    sns.lineplot(x=x, y=s, estimator=None, lw=1, marker='o', data=df3)
    plt.axhline(y=sbar, linewidth=2, color='g')
    plt.axhline(y=slcl,linewidth=2, color='orange')
    plt.axhline(y=sucl,linewidth=2, color='orange')
    
    plt.subplot(223)
    plt.text(0.1,0.5,eintrag_x, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.subplot(224)
    plt.text(0.1,0.5,eintrag_s, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    
    plt.show()    



def LREG(df, yv, xv):
    
    sns.set(color_codes=True)   
         
    
    print('Linear regression \n')    
    
    y = df[yv]
    
    x = df[xv]
    
    yg = yv
    
    xg = xv
    
    x = sm.add_constant(x)

    
    model = sm.OLS(y, x)
    
    
    
    results = model.fit()

    print(results.summary())
    
    
    
    
    
        
        
    
    
    print('coefficient of determination:', results.rsquared)
    print('adjusted coefficient of determination:', results.rsquared_adj)
    print('regression coefficients:', results.params)
    
    ols_resid = sm.OLS(y, x).fit().resid
    
    stat, p = shapiro(ols_resid)
    
    
    
    text_lreg = 'rsquared: ' + str(results.rsquared) + '\nregression coefficients: ' + str(results.params) 
    text_lres = 'Test of normality residuals' + '\np-Value: ' + str(p)
    
    
    
    plt.figure(figsize=(6, 4))
    plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
    sns.regplot(x=xg, y=yg, data=df);
    plt.subplot(222)
    sns.residplot(x=xg, y=yg, data=df, lowess=True, color="g"); 
    plt.subplot(223)
    plt.text(0.1,0.5,text_lreg, ha='left', va='center',fontsize=12)
    plt.axis('off')
    plt.subplot(224)
    plt.text(0.1,0.5,text_lres, ha='left', va='center',fontsize=12)
    plt.axis('off')
    
    plt.show()


def outliert(df, messwert):
    
    sns.set(color_codes=True)
    print('Test of Outliers \n')
    
    y=df[messwert]
    y_val = messwert
    
    print('Value could be outlier:',grubbs.max_test_outliers(y, alpha=0.05))
    
       
    
    eintrag = 'Grubbs-Outlier Test' + '\nValue could be outlier:' + str(grubbs.max_test_outliers(y, alpha=0.05))
    
    plt.figure(figsize=(6,2))
    plt.subplot(211)
    sns.boxplot(x=y)
    plt.subplot(212)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.show()    
