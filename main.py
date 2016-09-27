#python data analysis library
import csv
from pandas import read_csv
import matplotlib.pyplot as plt


#read dataset.csv file
dataset = read_csv('dataset.csv')
reader = csv.reader(open('dataset.csv'), delimiter=',', quotechar='"')


#Show Characteristics-Price Addiction
corr = dataset.corr()._get_item_cache(item='price').plot(kind='bar', stacked=True)
plt.savefig('Characteristics-Price Addiction.png', format = 'png')
plt.title('House Price Addiction With All Characteristics')
plt.grid()
plt.show()


#save all addiction
for row in reader:
    i = 1
    while (i != 20):
        dataset.pivot_table('price', row[i]).plot(kind='bar', stacked=True)
        plt.savefig('price-' + row[i] + ' addiction', format='png')
        i += 1
    break
