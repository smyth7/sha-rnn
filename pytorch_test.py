from __future__ import print_function
import torch
x = torch.rand(5, 3)
print(x)

if torch.cuda.is_available():
	dev = "cuda:0"
else:
	dev = "cpu"

device = torch.device(dev)
print(device)

x = x.to(device)  

print(x)