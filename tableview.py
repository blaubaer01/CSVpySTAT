#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:51:24 2020

@author: blaubaer (Ricky Helfgen)
"""
import pandas as pd
import webbrowser
from sys import platform



    


######################################################################
###show DataFrame in browser    
def file_in_html(df):
    
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

    #fn = 'ja'
    html_string = '''
    <html>
    <head><title>HTML Pandas Dataframe with CSS</title></head>
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <body>
    CSVpySTAT - Table Statistics - Dataframe: <br>
        {table}
        </body>
        </html>.
    '''

    # OUTPUT AN HTML FILE
    with open('myhtml.html', 'w') as f:
        f.write(html_string.format(table=df.to_html(classes='mystyle',index = False).replace('<th>','<th style = "background-color: red">')))
    
    url = 'myhtml.html'
    
    if platform == "linux" or platform == "linux2":
        webbrowser.open_new_tab(url)
    elif platform == "darwin":
        file_location = "file:///" + url
        webbrowser.open_new_tab(file_location)
    elif platform == "win32":
        webbrowser.open_new_tab(url)


    
    

    
    
    
    