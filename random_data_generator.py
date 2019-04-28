import numpy as np

mu1 = 1                            # set the number of points (e.g. 100), the mean, and the standard deviation.
sigma1 = 3
num1 = 100
mu2 = 9
sigma2 = 3
num2 =100

rand_data_set1 = np.random.normal(mu1, sigma1, num1)  #generate random number with numpy function.
rand_data_set2 = np.random.normal(mu2, sigma2, num2)

data_set = np.append(rand_data_set1, rand_data_set2) #mix two random data sets into one.
data_set = list(data_set)

text_file_name = 'dataset.txt'   # save the data set into a text file.
file = open(text_file_name, 'w')
for number in data_set:
    file.write(str(number) + '\n')
file.close()
print('save complete.')
