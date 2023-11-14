import numpy as np


## use np.mean to find average value 


my_array = np.array([2, 25, 43, 57, 9, 80])

average = np.mean(my_array)
#print(average)

##np.mean can also be used a logical operation and returns the percentage of elemetns that meet that condition

higher_than = np.mean(my_array >= 30)
#print(higher_than)

##when used on 2d arrays, np.mean can return the mean value of the whole array or that of intern values 

my_2d_array = np.array([[1,4,3,6,7],
                        [5,90,87,65,32],
                        [45,65,7,8,1],
                        [32, 41, 56, 7,8]])

my_2d_mean = np.mean(my_2d_array)

rows_mean = np.mean(my_2d_array, axis = 1)
columns_mean = np.mean(my_2d_array, axis=0)

#print(rows_mean, columns_mean)

##The command np.median gets you the median for the array
##NB: the median is useful because it is not affected by outliers as it is the number for which 50% of the dataset is below and 50% is above
##    it's the 50th percentile (25th is a quartile, 75th is a third quartile)

my_median = np.median(my_array)
print(my_median)

##Other percentile values can be obtained by running np.percentile([array], [percentile value])


##The standard deviation can be obtained with np.std and tells how spread apart the data is, similarly to the interquartile range between third and firt quaritlez