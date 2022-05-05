from numpy import zeros, where
from sigmoid import sigmoid

def predict(theta, X):
    """ 
    Predict whether the label is 0 or 1 using learned logistic 
    regression parameters theta
    p = predict (theta, X) computes the predictions for X using a 
    threshold at 0.5 (i.e., if sigmoid(theta'*x) >= 0.5, predict 1)
    """

    # Initialize some useful values
    m = X.shape[0] # number of training examples 

    # You need to return the following variables correctly
    p = zeros([m]);

    # ====================== YOUR CODE HERE ======================
    # Instructions: Complete the following code to make predictions using
    #               your learned logistic regression parameters. 
    #               You should set p to a vector of 0's and 1's

    sigm_X = sigmoid(X @ theta)
    p[where(sigm_X >= 0.5)] = 1
    
    # =========================================================================

    return p 