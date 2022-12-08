import numpy as np

def variance(data): 
  # Number of observations 
  n = len(data) 
  # Mean of the data 
  mean = np.mean(data)
  # Square deviations 
  deviations = [(x - mean) ** 2 for x in data] 
  # Variance 
  variance = np.sum(deviations) / n 
  return variance 

# standart deviation
def stdev(data): 
  var = variance(data) 
  std_dev = np.sqrt(var) 
  return std_dev
  
def calculate(list):
  # Check if list contains less than 9 numbers
  if (len(list) < 9):
    raise ValueError('List must contain nine numbers.')
  
  arr = np.array([[list[0], list[1], list[2]], 
                  [list[3], list[4], list[5]],
                  [list[6], list[7], list[8]]])
  
  arr_max_col = np.array([]) # array of max values of columns
  for i in range(len(arr)):
    arr_max_col = np.append(arr_max_col, np.amax([arr[0][i], 
                                                  arr[1][i], 
                                                  arr[2][i]]))
  arr_max_col = arr_max_col.tolist()
  
  arr_max_row = np.array([np.amax(arr[0]), 
                          np.amax(arr[1]),
                          np.amax(arr[2])
                         ]).tolist()  # array of max values of rows
  
  val_max = np.amax([arr_max_col, arr_max_row]).tolist()  # max value between 2 arrays

  arr_min_col = np.array([]) # array of min values of columns
  for i in range(len(arr)):
    arr_min_col = np.append(arr_min_col, np.amin([arr[0][i], 
                                                  arr[1][i], 
                                                  arr[2][i]]))
  arr_min_col = arr_min_col.tolist()
  
  arr_min_row = np.array([np.amin(arr[0]), 
                          np.amin(arr[1]),
                          np.amin(arr[2])
                         ]).tolist()  # array of min values of rows
  
  val_min = np.amin([arr_min_col, arr_min_row]).tolist()  # min value between 2 arrays
  
  arr_sum_col = np.array([]) # array of sum of columns
  for i in range(len(arr)):
    arr_sum_col = np.append(arr_sum_col, np.sum([arr[0][i], 
                                                 arr[1][i], 
                                                 arr[2][i]]))
  arr_sum_col = arr_sum_col.tolist()
  
  arr_sum_row = np.array([np.sum(arr[0]), 
                          np.sum(arr[1]),
                          np.sum(arr[2])
                         ]).tolist()  # array of sum of rows

  val_sum = np.sum(arr_sum_col) # sum of values of list

  arr_mean_col = np.array([]) # array of mean values of columns
  for i in range(len(arr)):
    arr_mean_col = np.append(arr_mean_col, np.mean([arr[0][i], 
                                                    arr[1][i], 
                                                    arr[2][i]]))
  arr_mean_col = arr_mean_col.tolist()
  
  arr_mean_row = np.array([np.mean(arr[0]), 
                           np.mean(arr[1]),
                           np.mean(arr[2])
                          ]).tolist()  # array of mean values of rows

  
  val_mean = np.mean(arr_mean_col) # mean of values of list

  arr_variance_col = np.array([]) # array of variance values of columns
  for i in range(len(arr)):
    arr_variance_col = np.append(arr_variance_col, variance([arr[0][i], 
                                                             arr[1][i], 
                                                             arr[2][i]]))
  arr_variance_col = arr_variance_col.tolist()
  
  arr_variance_row = np.array([]) # array of variance values of rows
  arr_variance_row = np.array([variance(arr[0]), 
                               variance(arr[1]),
                               variance(arr[2])
                              ]).tolist()  # array of mean values of rows
  
  val_variance = variance(np.array(list)) # variance of list

  arr_stdev_col = np.array([]) # array of standart deviation values of columns
  for i in range(len(arr)):
    arr_stdev_col = np.append(arr_stdev_col, stdev([arr[0][i],
                                                    arr[1][i],
                                                    arr[2][i]]))
  arr_stdev_col = arr_stdev_col.tolist()

  arr_stdev_row = np.array([]) # array of standart deviation values of rows
  for i in range(len(arr)):
    arr_stdev_row = np.append(arr_stdev_row, stdev([arr[i][0],
                                                   arr[i][1],
                                                   arr[i][2]]))
  arr_stdev_row = arr_stdev_row.tolist()

  val_stdev = stdev(np.array(list)) # standart deviation of list
  
  calculations = {
    'mean': [arr_mean_col, arr_mean_row, val_mean],
    'variance': [arr_variance_col, arr_variance_row, val_variance],
    'standard deviation': [arr_stdev_col, arr_stdev_row, val_stdev],
    'max': [arr_max_col, arr_max_row, val_max],
    'min': [arr_min_col, arr_min_row, val_min],
    'sum': [arr_sum_col, arr_sum_row, val_sum]
  }

  return calculations
