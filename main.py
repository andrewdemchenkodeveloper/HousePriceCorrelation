#python data analysis library
from pandas import read_csv, DataFrame


#read dataset.csv file
dataset = read_csv('C:\\Users\\Admin\\PycharmProjects\\FactorsInfluencingHousePrice\\dataset.csv')


#calculate correlation coefficient for price

corr = dataset.corr()._get_item_cache(item='price')


#printing the results
print('Dependence coefficient of house prices:' + '\n')
print(corr)
print('\n' + 'The most important factors are: \'bathroom\' (52%), '
      '\'sqft_living\' (70%), \'grade\' (66%),  \'sqft_above\' (60%), '
      '\'sqft_living15\' (58%)')