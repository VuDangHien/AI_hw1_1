import numpy as np 
filePath = "C:\\Users\\admin\\Desktop\\Ky 20231\\Artificial Intelligence\\CIS419-master\\Assignment1\\hw1_skeleton\\data\\univariateData.dat"
file = open (filePath , "r")
allData = np.loadtxt(file , delimiter=',')
X = np.matrix(allData[:,:-1])
y = np.matrix((allData[:,:-1])).T
n,d =X.shape
from test_linreg_univariate import plotData1D
plotData1D(X, y)
