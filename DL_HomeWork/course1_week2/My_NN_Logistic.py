import numpy as np
import matplotlib.pyplot as plt
import h5py
import numpy as np
import scipy.optimize as opt


# 首先导入数据并对数据做预处理
def load_dataset():
    """
    目标：将64*64RGB照片
    """

    train_dataset = h5py.File('./datasets/train_catvnoncat.h5', "r")
    # 获取训练样本的数据与标签
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])
    train_set_y_orig = np.array(
        train_dataset["train_set_y"][:])

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    # 获取测试样本的数据与标签
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])
    test_set_y_orig = np.array(
        test_dataset["test_set_y"][:])

    classes = np.array(test_dataset["list_classes"][:])
    # 将标签二阶张量　shape=(1,50)
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
# print(test_set_x_orig.shape[3])

# 将训练集测试数据的维度降至二维（二阶张量）
train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1)
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1)
train_set_y = train_set_y.reshape(-1)
print(train_set_y)
'''
print(train_set_x_flatten[0])
print(train_set_x_flatten.shape)
print(test_set_x_flatten.shape)
'''
# 数据标准化
train_set_x = train_set_x_flatten / 255
test_set_x = test_set_x_flatten / 255
theta = np.zeros(train_set_x_flatten.shape[1])
# print(theta.shape)


def sigmoid(x):
    """
    定义sigmoid函数
    """
    return 1/(1+np.exp(-x))


def gradient_func(theta, x, y):
    """
    定义梯度下降函数（前向传播，反向传播，梯度）
    """
    DataSize = x.shape[0]
    return 1/DataSize*(sigmoid(x@theta)-y).T@x


def cost_func(theta, x, y):
    """
    定义损失函数
    """
    DataSize = x.shape[0]
    return -1/DataSize*(y@np.log(sigmoid(x@theta))+(1-y)@np.log(1-sigmoid(x@theta)))


# 方法一 BFGS
theta1, cost1, *unused1 = opt.fmin_bfgs(f=cost_func, fprime=gradient_func,
                                        x0=theta, args=(train_set_x, train_set_y), maxiter=400, full_output=True)

# 方法二 牛顿共轭梯度
theta2, cost2, *unused2 = opt.fmin_ncg(f=cost_func, fprime=gradient_func,
                                       x0=theta, args=(train_set_x, train_set_y), maxiter=400, full_output=True)

# 方法三 L-BFGS-B
theta3, cost3, *unused3 = opt.fmin_l_bfgs_b(
    func=cost_func, fprime=gradient_func, x0=theta, args=(train_set_x, train_set_y), maxiter=400)
