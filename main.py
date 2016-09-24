#python data analysis library
from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt


#read dataset.csv file
dataset = read_csv('dataset.csv')


#Show Characteristics-Price Addiction
corr = dataset.corr()._get_item_cache(item='price').plot(kind='bar', stacked=True)
plt.savefig('Characteristics-Price Addiction.png', format = 'png')
plt.title('House Price Addiction With All Characteristics')
plt.grid()
plt.show()


#Date-Price Addiction
dataset.pivot_table('price', 'date').plot(kind='bar', stacked=True)
plt.savefig('Date-Price Addiction.png', format = 'png')

#Bedrooms-Price Addiction
dataset.pivot_table('price', 'bedrooms').plot(kind='bar', stacked=True)
plt.savefig('Bedrooms-Price Addiction.png', format = 'png')

#Bathrooms-Price Addiction
dataset.pivot_table('price', 'bathrooms').plot(kind='bar', stacked=True)
plt.savefig('Bathrooms-Price Addiction.png', format = 'png')

#Sqft_living-Price Addiction
dataset.pivot_table('price', 'sqft_living').plot(kind='bar', stacked=True)
plt.savefig('Sqft_living-Price Addiction.png', format = 'png')

#Sqft_lot-Price Addiction
dataset.pivot_table('price', 'sqft_lot').plot(kind='bar', stacked=True)
plt.savefig('Sqft_lot-Price Addiction.png', format = 'png')

#Floors-Price Addiction
dataset.pivot_table('price', 'floors').plot(kind='bar', stacked=True)
plt.savefig('Floors-Price Addiction.png', format = 'png')

#Waterfront-Price Addiction
dataset.pivot_table('price', 'waterfront').plot(kind='bar', stacked=True)
plt.savefig('Waterfront-Price Addiction.png', format = 'png')

#View-Price Addiction
dataset.pivot_table('price', 'view').plot(kind='bar', stacked=True)
plt.savefig('View-Price Addiction.png', format = 'png')

#Condition-Price Addiction
dataset.pivot_table('price', 'condition').plot(kind='bar', stacked=True)
plt.savefig('Condition-Price Addiction.png', format = 'png')

#Grade-Price Addiction
dataset.pivot_table('price', 'grade').plot(kind='bar', stacked=True)
plt.savefig('Grade-Price Addiction.png', format = 'png')

#Sqft_above-Price Addiction
dataset.pivot_table('price', 'sqft_above').plot(kind='bar', stacked=True)
plt.savefig('Sqft_above-Price Addiction.png', format = 'png')

#Sqft_basement-Price Addiction
dataset.pivot_table('price', 'sqft_basement').plot(kind='bar', stacked=True)
plt.savefig('Sqft_basement-Price Addiction.png', format = 'png')

#Yr_built-Price Addiction
dataset.pivot_table('price', 'yr_built').plot(kind='bar', stacked=True)
plt.savefig('Yr_built-Price Addiction.png', format = 'png')

#Yr_renovated-Price Addiction
dataset.pivot_table('price', 'yr_renovated').plot(kind='bar', stacked=True)
plt.savefig('Yr_renovated-Price Addiction.png', format = 'png')

#Zipcode-Price Addiction
dataset.pivot_table('price', 'zipcode').plot(kind='bar', stacked=True)
plt.savefig('Zipcode-Price Addiction.png', format = 'png')

#Lat-Price Addiction
dataset.pivot_table('price', 'lat').plot(kind='bar', stacked=True)
plt.savefig('Lat-Price Addiction.png', format = 'png')

#Long-Price Addiction
dataset.pivot_table('price', 'long').plot(kind='bar', stacked=True)
plt.savefig('Long-Price Addiction.png', format = 'png')

#Sqft_living15-Price Addiction
dataset.pivot_table('price', 'sqft_living15').plot(kind='bar', stacked=True)
plt.savefig('Sqft_living15-Price Addiction.png', format = 'png')

#Sqft_lot15-Price Addiction
dataset.pivot_table('price', 'sqft_lot15').plot(kind='bar', stacked=True)
plt.savefig('Sqft_lot15-Price Addiction.png', format = 'png')