import numpy as np
from math import ceil

def relu(x):
    return np.maximum(0, x)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def deriv_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))
def deriv_relu(x):
    return x > 0
def stable_softmax(x):
    x -= np.max(x, axis=0)
    return np.exp(x) / np.sum(np.exp(x), axis=0)
def deriv_stable_softmax(x): # just for test
    sm = stable_softmax(x)
    # return sm * (1 - sm)
    return 1

def deriv_mse(a, t):
    return 2 / len(t) * (a - t)

def get_predict(a):
    return np.argmax(a, axis=0)
def get_accuracy(t, a):
    return np.sum(get_predict(a) == t) / len(t)

def one_hot(Y, classes):
	m = len(Y)
	one_hot = np.zeros((len(classes), m))
	for i in range(m):
		one_hot[classes.index(Y[i])][i] = 1
	return one_hot

class ANN:
    

    activations = {'relu':relu, 'stable_softmax':stable_softmax, 'sigmoid':sigmoid}
    deriv_activations = {'relu':deriv_relu, 'stable_softmax':deriv_stable_softmax, 'sigmoid':deriv_sigmoid}
    losses = {'mse':deriv_mse}

    def __init__(self, input_size:int, hidden_size:list, output_size:int, 
                 hidden_activation = 'relu', output_activation = 'stable_softmax', learning_rate = 0.0001, loss = 'mse', epoch = 200, batch_size = 1000):
        # random weights
        self.w = []
        self.b = []
        # weights input -> fisrt hidden
        self.w.append(np.random.rand(hidden_size[0], input_size) - 0.5)
        self.b.append(np.random.rand(hidden_size[0], 1) - 0.5)
        #weights hidden -> hidden
        for i in range(1, len(hidden_size)):
            self.w.append(np.random.rand(hidden_size[i], hidden_size[i-1]) - 0.5)
            self.b.append(np.random.rand(hidden_size[i], 1) - 0.5)
        # weights last hidden -> output
        self.w.append(np.random.rand(output_size, hidden_size[-1]) - 0.5)
        self.b.append(np.random.rand(output_size, 1) - 0.5)

        # learning rate
        self.learning_rate = learning_rate
        
        # activation
        self.hidden_activation = self.activations[hidden_activation]
        self.output_activation = self.activations[output_activation]

        # deriv_activation
        self.hidden_deriv_activation = self.deriv_activations[hidden_activation]
        self.output_deriv_activation = self.deriv_activations[output_activation]

        # loss
        self.loss = self.losses[loss]

        self.epoch = epoch
        self.batch_size = batch_size
    
    
    def feedforward(self, x):
        o = []
        a = []

        o.append(np.dot(self.w[0], x) + self.b[0])
        a.append(self.hidden_activation(o[0]))

        for i in range(1,len(self.w)-1):
            o.append(np.dot(self.w[i], a[-1]) + self.b[i])
            a.append(self.hidden_activation(o[-1]))
        
        o.append(np.dot(self.w[-1], a[-1]) + self.b[-1])
        a.append(self.output_activation(o[-1]))


        return o, a

    # gradient descent
    # t = target value, o = output, a = activation's output, x = input  
    def backprop(self, t, o, a, x):
        loss = self.loss(a[-1], t)

        # where tf m come from?
        # maybe use to find mean of all dataset
        m = len(t)

        w_gradients = []
        b_gradients = []

        # output layer
        # number of delta = k (number of output layer's node)
        delta = loss * self.output_deriv_activation(o[-1])
        
        # print(np.dot(delta, a[-2].T))
        # print(a[-2])

        w_gradients.append(1/m * np.dot(delta, a[-2].T))
        b_gradients.append(1/m * np.sum(delta))

        for i in range(len(self.w) - 2, 0, -1):
            # n delta(l+1) = n nodes(l+1)
            delta = np.dot(self.w[i + 1].T, delta) * self.hidden_deriv_activation(o[i])
            w_gradients.append(1/m * np.dot(delta, a[i - 1].T))
            b_gradients.append(1/m * np.sum(delta))

        # layer input-hidden
        delta = np.dot(self.w[1].T, delta) * self.hidden_deriv_activation(o[0])
        w_gradients.append(np.dot(delta, x.T))
        b_gradients.append(np.sum(delta))

        length = len(w_gradients)
        for i in range(length):
            self.w[length - i - 1] -= self.learning_rate * w_gradients[i]
            self.b[length - i - 1] -= self.learning_rate * b_gradients[i]


    def fit(self, x, y, classes):
        x = x.T
        n_iters = ceil(len(y) / self.batch_size)

        # splited_x = np.array_split(x.T, n_iters)
        # splited_x = np.array(splited_x)

        # splited_y = np.array_split(y.T, n_iters)
        # splited_y = np.array(splited_y)

        print(f'Epoch = {self.epoch}\nBatch Size = {self.batch_size}\nIteration = {n_iters}')
        # print(f'x shape: {splited_x[0].shape}\ny shape: {splited_y.shape}')

        for i in range(1, self.epoch+1):
            o, a = self.feedforward(x)
            self.backprop(one_hot(y, classes), o, a, x)
            if i%10 == 0 or i == self.epoch:
                accuracy = get_accuracy(y, a[-1])
                print(f'epoch = {i}, accuracy = {accuracy}')
    
    def test_train(self, index, x, y):
        x = x.T
        test = x[:, index, None]
        o, a = self.feedforward(x)
        predict = get_predict(a[-1])[index]
        label = y[index]

        return predict, label, test

