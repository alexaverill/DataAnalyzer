import numpy as np
import matplotlib.pyplot as plt
import csv
# code originally found here: https://www.geeksforgeeks.org/linear-regression-python-implementation/
#added in ways to pull data from csv file.
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()
 
def main():
    fileIn = input("Enter csv file path:")
    # observations
    
    with open(fileIn,'r') as f:
        reader = csv.reader(f)
        dataList = list(reader)
    #print(dataList)
    print(len(dataList))
    lnList = []
    tList = []
    x=0;
    for element in dataList:
        lnList.append(float(dataList[x][5]))
        tList.append(float(dataList[x][6]))
        x +=1
    print(lnList);
    print(tList);
    x = np.array(lnList)
    y = np.array(tList)
 
    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
    # plotting regression line
    plot_regression_line(x, y, b)   
if __name__ == "__main__":
    main()