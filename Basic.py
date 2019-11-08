# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:48:23 2019

@author: samer
"""
import os

import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Loading dataset


df = pd.read_csv('C:\\Users\\samer\\CEDB11\\CEBD-1160-fall-2019-code\\5-python-dataviz-notebook\\data\\wine.data',
                      sep=',',
                      header=0)
df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids',
                   'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
                   'proline']
sns.pairplot(df)
plt.savefig('C:\\Users\\samer\\viz_homework\\viz-homework\\plt\\plot1.png', dpi=300)
plt.close()
sns.pairplot(df,hue='alcohol', diag_kind='hist')
plt.savefig('C:\\Users\\samer\\viz_homework\\viz-homework\\plt\\plot2.png', dpi=300)
plt.close()
