import torch
print("CUDA available:", torch.cuda.is_available())
print("Device:", torch.device("cpu"))
