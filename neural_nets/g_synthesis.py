

from torch.nn import Sequential, ConvTranspose2d
from torch import rand

import attention_module
import residual_bottleneck


def Model(in_channels, N):
    return Sequential(
        ConvTranspose2d(in_channels, N, kernel_size=5,
                        stride=2, padding=2, output_padding=1),
        residual_bottleneck.Model(N),
        ConvTranspose2d(N, N, kernel_size=5, stride=2,
                        padding=2, output_padding=1),
        residual_bottleneck.Model(N),
        ConvTranspose2d(N, N, kernel_size=5, stride=2,
                        padding=2, output_padding=1),
        residual_bottleneck.Model(N),
        ConvTranspose2d(N, 3, kernel_size=5, stride=2,
                        padding=2, output_padding=1),
    )


if __name__ == "__main__":
    test_data = rand((1, 192, 64, 64))
    model = Model(192, 192)
    y_hat = model(test_data)
    print(test_data.shape)
    print(y_hat.shape)
