#important library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

#style settings
matplotlib.style.use('bmh')

#read dataset.csv
dataset = pd.read_csv('dataset.csv')

#show Characteristics-Price Addiction
corr = dataset.corr()._get_item_cache(item='price').plot(kind='bar', stacked=True)
plt.savefig('Characteristics-Price Addiction.png', format = 'png')
plt.title('House Price Addiction With All Characteristics')
plt.grid()
plt.show()

#price addictoion
for c in dataset.columns.difference(['price']).tolist():
    dataset.pivot_table('price', c).plot(kind='bar', stacked=True)
    plt.savefig('price-{}-addiction.png'.format(c))
