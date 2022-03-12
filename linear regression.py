import numpy as np

# known data:
X = [1,3,7,9,0,-3,1]
# unknown data:
Y = [15,45,105,140,0,-40,16]

'''
Y = aX + B
a = [ (X-min(Xs))(Y-min(Ys)) ] / (X-min(Xs))^2
B = min(Ys) - min(Xs)*a 
'''

# make Solvation:
def solve(x,y):
    Sa = 0
    Ma = 0
    for i in range(len(x)):
        Sa += (x[i]-np.min(x)) * (y[i]-np.min(y))
        Ma += (x[i]-np.min(x))**2
    a = Sa/Ma
    b = np.min(y) - np.min(x)*a
    print("coef = " + str(a))
    print("insept = " + str(b))
    y_predict = []
    for i in x:
        y_predict.append(a*i +b)
    return(y_predict)

# find erorr:
def find_erorr(x,y):
    erorr = 0
    for i in range(len(x)):
        erorr += ( x[i]-y[i] )**2
    return np.sqrt(erorr/len(x))

print( find_erorr( (solve(X,Y)) , Y ) )

