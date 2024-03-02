# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/03_convolutions.ipynb.

# %% auto 0
__all__ = ['def_device', 'conv', 'to_device', 'collate_device']

# %% ../notebooks/03_convolutions.ipynb 2
import torch
import torch.nn.functional as F
from torch import nn

from torch.utils.data import default_collate
from typing import Mapping

from .training import *
from .datasets import *

# %% ../notebooks/03_convolutions.ipynb 13
def conv(ni, nf, ks=3, stride=2, act=True):
    res = nn.Conv2d(ni, nf, stride=stride, kernel_size=ks, padding=ks//2)
    if act: res = nn.Sequential(res, nn.ReLU())
    return res

# %% ../notebooks/03_convolutions.ipynb 17
def_device = 'cuda' if torch.cuda.is_available() else 'cpu'

def to_device(x, device=def_device):
    if isinstance(x, torch.Tensor): return x.to(device)
    if isinstance(x, Mapping): return {k:v.to(device) for k, v in x.items()}
    return type(x)(to_device(o, device) for o in x)

def collate_device(b): return to_device(default_collate(b))
