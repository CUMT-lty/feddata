import torch

# flag = torch.cuda.is_available()
# print(flag)

a = torch.ones((3, 1))
a = a.cuda(0)
b = torch.ones((3, 1)).cuda(0)
c = a + b
print(c)
