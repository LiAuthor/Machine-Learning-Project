import numpy as np
import h5py
from skimage import transform, data
import imageio
import pickle
import os

def sigmoid(Z):

    A = 1/(1+np.exp(-Z))
    cache = Z
    return A, cache

def relu(Z):

    A = np.maximum(0,Z)
    assert(A.shape == Z.shape)
    cache = Z 
    return A, cache

def linear_forward(A, W, b):

    Z = np.dot(W, A) + b
    assert(Z.shape == (W.shape[0], A.shape[1]))
    cache = (A, W, b)

    return Z, cache


def linear_activation_forward(A_prev, W, b, activation):


    if activation == "sigmoid":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = sigmoid(Z)
    elif activation == "relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = relu(Z)

    assert(A.shape == (W.shape[0], A_prev.shape[1]))
    cache = (linear_cache, activation_cache)
    return A, cache


def L_model_forward(X, parameters):

    caches = []
    A = X
    L = len(parameters) // 2
    for l in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(
            A_prev, parameters['W' + str(l)], parameters['b' + str(l)], "relu")
        caches.append(cache)

    AL, cache = linear_activation_forward(
        A, parameters['W' + str(L)], parameters['b' + str(L)], "sigmoid")
    caches.append(cache)
    assert(AL.shape == (1, X.shape[1]))
    return AL, caches

'''
#test集预测
def predict(X, parameters):
    """
    该函数用于预测L层神经网络的结果，当然也包含两层

    参数：
     X - 测试集
     parameters - 训练模型的参数

    返回：
     p - 给定数据集X的预测
    """

    m = X.shape[1]
    n = len(parameters) // 2  # 神经网络的层数
    p = np.zeros((1, m))
    t=1
    # 根据参数前向传播
    probas, caches = L_model_forward(X, parameters)
    for i in range(0, probas.shape[1]):
        if probas[0, i] > 0.5:
            p[0, i] = 1
        else:
            p[0, i] = 0
        print("Number: "+t+"Predict: "+p)
        t+=1
    #print("准确度为: " + str(float(np.sum((p == y))/m)))
'''

def predict(X, parameters):

    probas, caches = L_model_forward(X, parameters)
    #print(probas[0][0])
    #print('{:.5f}'.format(probas[0][0]))
    if probas[0][0]>0.5:
        p=1
    else:
        p=0
    return p


#取参数
with open('W_parameters.pkl', 'rb') as f:
    parameters = pickle.load(f)

#遍历预测文件夹
#my_image = "14.jpg"
t=1
Not=0
Yes=0
dir="/home/li/DataSet/cat/No/"
for file in os.listdir(dir):
    #print(file)
    fname = dir+file
    image = np.array(imageio.imread(fname))
    my_image = transform.resize(image, (64, 64)).reshape((64*64*3, 1))
    #print(my_image.shape)
    my_predicted_image = predict(my_image, parameters)
    if my_predicted_image==0:
        Not+=1
    else:
        Yes+=1
    #print("Number: %s Predict：%s"%(t,my_predicted_image))
    t+=1
print("Yes: %s"%(float(Yes/t)))
print("Not: %s"%(float(Not/t)))