#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 08:56:56 2022

@author: blaubaer
"""

import pandas as pd
import numpy as np
anzahl_sp = 3
anzahl_r = 4

df= pd.DataFrame(index=np.arange(anzahl_sp), columns=np.arange(anzahl_r))
print (df)
