# Pangu

import pseudocode
from pseudocode import PanguModel as Pangu

import torch

if __name__ == '__main__':
    B = 1  # batch_size
    surface = torch.randn(B, 4, 721, 1440)  # B, C, Lat, Lon
    surface_mask = torch.randn(3, 721, 1440)  # topography mask, land-sea mask, soil-type mask
    upper_air = torch.randn(B, 5, 13, 721, 1440)  # B, C, Pl, Lat, Lon

    pangu_weather = Pangu()

    

    output_surface, output_upper_air = pangu_weather(surface, surface_mask, upper_air)