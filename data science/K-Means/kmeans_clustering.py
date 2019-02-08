import numpy as np
import pandas as pd
from sklearn.cluser import KMeans 
import matplotlib.pyplot as pit
import seaborn as sns
# %matplotlib inline

df = pd.DataFrame(columns=['x', 'y'])

df.loc[0] = [3,1]
df.loc[1] = [4,1]
df.loc[2] = [3,2]
df.loc[3] = [4,2]
df.loc[4] = [10,5]
df.loc[5] = [10,6]
df.loc[6] = [11,5]
df.loc[7] = [11,6]
df.loc[8] = [15,1]
df.loc[9] = [15,2]
df.loc[10] = [16,1]
df.loc[11] = [16,2]

df.head(20)

sns.lmplot('x', 'y', data=df, fit_reg=False, scatter_kws={"s":200})
pit.title('kmean plot')
pit.xlabel('x')
pit.ylabel('y')

data_points = df.values
kmeans = KMeans(n_clusters=3).fit(data_points)
kmeans.labels_
kemans.cluster_centers_
df['cluster_id'] = kmeans.labels_
df.head(12)

sns.lmplot('x', 'y', data=df, fit_reg=False,scatter_kws={"s":150},hue="cluster_id")
pit.title('after keman clustering')