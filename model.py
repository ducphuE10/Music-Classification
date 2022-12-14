import torch
from torch import nn
# from torchsummary import summary


class MLPNetwork(nn.Module):

    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear = nn.Sequential(
            nn.Linear(1* 64* 79, 1048), # I got the number (1 * 64 * 79) as input size from the code above
            nn.Sigmoid(),
            nn.Linear(1048, 256),
            nn.Sigmoid(),
            nn.Linear(256, 128),
            nn.Sigmoid(),
            nn.Linear(128, 1),
        )

    def forward(self, input_data):
        x = self.flatten(input_data)
        logits = self.linear(x)
        predictions = torch.sigmoid(logits)
        return predictions
        # return x

