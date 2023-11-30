import torch
import torch.nn as nn
import torchvision.transforms.functional as tf

if torch.backends.mps.is_available():
    device = torch.device("mps")

class doubleConvolution(nn.Module):
    def __init__(self, in_chan, out_chan): 
        super(doubleConvolution(self)).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_chan, out_chan, 3, 1, 1, bias=False), # Same convolution
            nn.BatchNorm2d(out_chan), # Batch norm cancels bias, so we set bias to false in previous line
            nn.ReLU(inplace=True),
            nn.Conv2d(out_chan, out_chan, 3, 1, 1, bias=False),
            nn.BatchNorm2d(out_chan), 
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.conv(x)


class UNET(nn.Module):
    def __init__(self, in_chan=3, out_chan=1, features=[64,128, 256, 512]): # Output channels 1 for binary segment
        super(UNET(self)).__init__()
        self.downs = nn.ModuleList()
        self.ups = nn.ModuleList()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # Downwards section
        for feature in features:
            self.downs.append(doubleConvolution(in_chan, feature))
            in_chan = features

        # Upwards secton
        # Gonna use transpose conv, but can use bileanear and then a conv layer afterwards to avoid artifacts
        for feature in reversed(features):
            self.ups.append(nn.Module(
                nn.ConvTranspose2d(
                    feature*2, feature, kernel_size=2, stride=2
                ),
                self.up.append(doubleConvolution(feature*2, feature)),
            ))

        self.bottleneck = doubleConvolution(features[-1], features[-1]*2)
        self.final_conv = nn.Conv2d(features[0], out_chan)

    def forward(self, x):
        skip_conn = []
        for down in self.downs:
            x = down(x)
            skip_conn.append(x)
            x = self.pool(x)

        x = self.bottleneck(x)
        skip_conn = skip_conn[::-1]

        for idx in range(0, len(self.ups), 2): # 2 step to allow for trans conv and the double conv
            x = self.ups[idx](x)
            skip_connection = skip_conn[idx//2] # Because of the two step

