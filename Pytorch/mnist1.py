import torch 
from torch import nn
import pandas as pd

data = pd.read_csv("/Users/duongphamminhdung/Documents/GitHub/DATA SETS/mnist/mnist_train.csv")
mnist = data.values
label = torch.from_numpy(mnist[:, 0])
digits = torch.from_numpy(mnist[:, 1:])

class MnistModel(nn.Module):
    def __init__(self):
        super(MnistModel, self).__init__()
        self.linear1 = nn.Linear(784, 256)
        self.actfunc1 = nn.Sigmoid()
        self.linear2 = nn.Linear(256, 64)
        self.actfunc2 = nn.Sigmoid()
        self.linear3 = nn.Linear(64, 10)
        self.softmax = nn.Softmax()

    def forward(self, x):
        x = self.linear1(x)
        x = self.actfunc1(x)
        x = self.linear2(x)
        x = self.actfunc2(x)
        x = self.linear3(x)
        x = self.softmax(x)
        return x
    

model = MnistModel()

# inp = torch.randn(10, 784)
# oup = model(inp)
# print(oup.shape)
