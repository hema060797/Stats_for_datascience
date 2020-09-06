
import pandas as pd
data1=pd.read_csv('import.csv')
print (data1)




print('it returns the covariance between suitable columns')
exporttrade.cov()
print('it returns the correlation betwween suitabe columns' )
exporttrade.corr()
#UNIVARIATE ANALYSIS
import seaborn as sns



import matplotlib.pyplot as plt
print('univariate analysis using distribution plot ')
sns.FacetGrid(exporttrade,hue="year",height=10).map(sns.distplot,"HSCode").add_legend()
sns.FacetGrid(exporttrade,hue="Commodity",height=10).map(sns.distplot,"year").add_legend()


print('CUMMULATIVE DISTRIBUTIVE FUNCTION AND PROFITABLILITY DENSITY FUNCTION')
import numpy as np
counts,bin_edges=np.histogram(exporttrade['year'],bins=10,density=True)
plt.xlabel('year')
pdf=counts/(sum(counts))
print("pdf=",pdf);
print("bin_edges=",bin_edges);
cdf=np.cumsum(pdf)
print("cdf=",cdf)
plt.plot(bin_edges[1:],pdf);
plt.plot(bin_edges[1:],cdf);

print('BIVARIATE ANALYSIS')
print('BOX PLOT')
sns.boxplot(x='year',y='Commodity',data=exporttrade)
plt.show()

print('MULTIVARIATE ANALYSIS')
sns.pairplot(exporttrade,hue="year",height=3)
plt.show()













import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(15,5))
sns.barplot('year','value',data=exporttrade)
plt.figure(figsize=(10,5))
sns.barplot('year','value',data=importtrade)

exp_countries= exporttrade[['country','value']].groupby(['country']).sum().sort_values(by = 'value', ascending = False)
plt.figure(figsize=(10,5))
sns.barplot(exp_countries.index, exp_countries.value)
plt.figure(figsize=(25,2))
sns.barplot(exp_countries.index, exp_countries.value)

by_country =exporttrade[['country','Commodity']].groupby(['country']).sum().sort_values(by = 'country', ascending = True).head(20)
by_country



