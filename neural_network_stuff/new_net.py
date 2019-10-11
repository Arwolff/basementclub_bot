import numpy as np


def sigmoid(x):  
    return math.exp(-np.logaddexp(0, -x))

class NeuralNetwork:
    def __init__(self,x ,y):
        self.input  = x
        self.weight = np.random.rand(4.1)
        self.y      = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        

        
