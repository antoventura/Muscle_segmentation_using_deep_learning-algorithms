import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from torchvision import transforms

'''
Class built to construct a database that works with Tensors

Antonio Ventura -  Maria Morandini
'''



class CustomDataset(Dataset):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __len__(self):
        return len(self.x)
    def __getitem__(self, idx):
        a,b = self.x[idx],self.y[idx]

        a = transforms.ToTensor()(a).type(torch.FloatTensor)
        b = transforms.ToTensor()(b).type(torch.FloatTensor)
        return (a, b)