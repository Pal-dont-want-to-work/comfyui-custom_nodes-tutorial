# from custom_nodes.comfyui_myplugin.amzqr.amzqr import run
import os

from typing import Optional

import numpy as np
import torch

from torchvision import transforms
from PIL import Image

from .amzqr.amzqr import run

class QR_node:
    def __init__(self) -> None:
        pass
    
    CATEGORY = "😀😀😀my custom plugin:QR_example😀😀😀"
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "url_sentence": ("STRING",
                                  {"default": "https://github.com/", 
                                   }),
                                   
                "version": ("INT", {
                                    "default": 5,
                                    "min": 1,
                                    "max": 40,
                                    "step": 1
                                    }),
                                    
                "level": (["L", "M", "Q", "H"], 
                          {
                            "default": "H"
                            }),
                            
                "colorized": ("BOOLEAN", {"default": False}),
                "contrast": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 3.0, "step": 0.01}),
                "brightness": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 3.0, "step": 0.01}),
            },
            "optional": {
                "IMAGE": ("IMAGE", {"default": None}),
            }
        }
    
    OUTPUT_NODE = True

    RETURN_TYPES = ("IMAGE", )
    # 自定义输出名称
    RETURN_NAMES = ("IMAGE", )
    

    # FUNCTION的名称与函数名对应
    FUNCTION = "generate_QR"

    def generate_QR(self, url_sentence, version, level, colorized, contrast, brightness, IMAGE: Optional[torch.tensor]=None):
        """
            参数与上面的INPUT_TYPES函数的return对应
            IMAGE格式的图片必须转成tensorg格式，维度(N, H, W, C)例如(1, 1024, 1024, 3)
            
        """
        if IMAGE is not None:
            IMAGE = IMAGE.permute(0, 3, 1, 2)


            transform = transforms.ToPILImage()
            IMAGE = transform(IMAGE.squeeze(0))

        current_file_path = os.path.abspath(__file__)
        directory = os.path.dirname(current_file_path)
        _, _, image_name = run(url_sentence, version, level, IMAGE, colorized, contrast, brightness, save_name="qr_code.png", save_dir=directory)
        image = Image.open(os.path.join(directory, image_name)).convert("RGB")
        
        image_tensor = transforms.ToTensor()(image)
        image_tensor = image_tensor.unsqueeze(0)
        image_tensor = image_tensor.permute(0, 2, 3, 1)
        
        # 输出格式必须是tuple
        return (image_tensor, )
    