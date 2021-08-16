# There are several ways to do normalization
## **Steps**
First, find the lower and upper bound for outliers.

second, collaps in the outliers

finally, use the log normalization

## **About the normalization techniques in Python**
1. Extracting Residuals : The residuals are the differece between each value and the mean of the value's distribution. Each residual is the distance from each distribution's mean which is zero, and the variance hasn't changed.

2. Min_Max Re_scaling:  (x - min) / (max - min). Then the dataset is on the same scale, each distribution has been squeezed and shifted to fit between 0 and 1.

3. log normalization: use np.log to rescale the dataset.

## **Using Numpy for normalizing Large Datasets**
* numpy uses less memory compared to python list,
* apply the scalar operation to each value of the array
* the result of using numpy for large datasets is much faster than using lists.