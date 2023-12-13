import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from ann import ANN, get_accuracy

# import pandas as pd

def shuffle(l):
    return np.random.permutation(l)

# data = pd.read_csv('train.csv')
# data = np.array(data)

# data = data[0:1000]
# m, n = data.shape

# data = data.T
# Y_train = data[0]
# X_train = data[1:n]
# X_train = X_train / 255.


mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data":mnist_raw["data"].T,
    "label":mnist_raw["label"][0]
}

x,y = mnist["data"],mnist["label"]
r = shuffle(70000)
x,y = x[r],y[r]
x_train,y_train,x_test,y_test = x[:60000],y[:60000],x[60000:],y[60000:]

classes = [0,1,2,3,4,5,6,7,8,9]

nn = ANN(input_size=784, hidden_size=[100], output_size=10, 
         hidden_activation='sigmoid', output_activation='stable_softmax',
         learning_rate=0.0001,loss='mse',epoch=100, batch_size=100)

nn.fit(x_train, y_train, classes)

n, m = x_test.shape
print('Test')
for i in range(20):
    index = np.random.randint(1, m)
    predict, label, test = nn.test_train(index , x_test, y_test)
    image = test.reshape((28,28))
    plt.subplot(5,4,i+1)
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.text(0,25,predict,color='y')
    plt.text(0,0,label,color='g')

    
plt.show()