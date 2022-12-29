import numpy as np

x = np.array(([2, 9], [1, 5], [3, 6]), dtype = float)
y = np.array(([92], [86], [89]), dtype = float)
x = x / np.amax(x, axis = 0)
y /= 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def der_sigmoid(x):
    return x * (1 - x)

weight_hidden = np.random.uniform(size = (2, 3))
bias_hidden = np.random.uniform(size = (1, 3))

weight_output = np.random.uniform(size = (3, 1))
bias_output = np.random.uniform(size = (1, 1))

for i in range(1000):
    hidden_activation = sigmoid(np.dot(x, weight_hidden) + bias_hidden)
    output = sigmoid(np.dot(hidden_activation, weight_output) + bias_output)

    first = y - output
    output_gradient = der_sigmoid(output)
    d_output = first * output_gradient
    hidden = d_output.dot(weight_output.T)
    hidden_gradient = der_sigmoid(sigmoid(np.dot(x, weight_hidden) + bias_hidden))
    d_hidden = hidden * hidden_gradient

    weight_output += sigmoid(np.dot(x, weight_hidden) + bias_hidden).T.dot(d_output) * 0.1
    weight_hidden += x.T.dot(d_hidden) * 0.1

print("Input : {}".format(str(x)))
print("Actual output : {}".format(str(y)))
print("Predicted output : {}".format(output))