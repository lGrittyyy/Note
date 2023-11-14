##Import Numpy and all other modules

import numpy as np 

##create 2d vector with movie ratings. Rows are ratings, columns are reviewers
## NB:  [[]] means a 2d array is created, otherwise it would just be a list of 3 arrays 
movie_ratings = np.array([[63.0, 54.0, 70.0, 50.0],
                          [94.0, 85.0, 70.0, 50.0],
                          [64.0, 90.0, 73.0, 85.0]])

## Perform basic math on all value of the 2d vector
star_ratings = movie_ratings / 20 

#select ratings by the second revier
r2_ratings = movie_ratings[:, 2]

#Selects all value of the column above a threshold 

threshold = 70 

r2_ratings[r2_ratings > threshold]

##reading a csv and creading an array form it 
test_2 = np.genfromtxt('test_2.csv', delimiter=',')
#print(test_2)


##Numpy allows for element-wise operations which standard lists do not allow
#list
l = [1,2,3,4,5]

l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i]+3)

#numpy, making an array out of a list and performing math onto it 
a = np.array(l)
a_plus_3 = a+3

#sqauring 
a ** 2

#square root
a = np.sqrt(a)

##selection of a value within a 1d array 
##INDEXED FROM 0. 1:3 takes element 1 included through 3 excluded
my_value = a [1:3]

##selection on 2d arrays
##third row, second column
my_value_2d = movie_ratings[2,1]
#print(my_value_2d)

##logical operations can be perfromed element wise as well

my_log_array = np.array([1,2,3,4,5])
my_operation = my_log_array[my_log_array > 3]
print(my_operation)
my_complex_operation = my_log_array[(my_log_array >= 2) & (my_log_array <= 4)]
print(my_complex_operation)