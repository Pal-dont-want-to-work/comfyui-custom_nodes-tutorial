import random

import torch

import comfy.model_management

class runnable_node:

    def __init__(self):
        pass
        
    ##############################
    # 2. 使用关键的标识符来表示该节点
    ##############################
    CATEGORY = "😀😀😀my custom plugin:runnable_node_example😀😀😀"

    ###############
    # 3.节点左侧输入
    ###############
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {"default": 256, "min": 128, "max": 2048, "step": 128}),
                "height": ("INT", {"default": 256, "min": 128, "max": 2048, "step": 128}),
            },
        }
    
    ###############
    # 4.节点右侧输出
    ###############
    OUTPUT_NODE = True  # 表明它是一个输出节点
    # 输出的数据类型，需要大写
    RETURN_TYPES = ("IMAGE",)
    # 自定义输出名称
    RETURN_NAMES = ("IMAGE",)

    ##############################
    # 5. 节点的核心功能逻辑在这里定义
    ##############################
    FUNCTION = "run" # 核心功能函数名称，将运行这个类中的这个方法

    def run(self, width, height):
        # 加载模型
        # 清空所有加载模型
        comfy.model_management.unload_all_models()
        # 加载模型略过，因为需要引入额外的包


        seed = random.randint(0, 10)
        torch.manual_seed(seed)

        # 进行推理
        noise = torch.randn((1, 3, width, height), device="cuda")

        # 数据格式处理
        # 注意：图片大部分都是一个PIL.image的数据类型，需要把图片数据转化成torch.Tensor数据类型才可以被comfyui中的preview image节点接收

        # [PIL.Image.Image]->[torch.Tensor]
        # torch.Tensor列表 = [ToTensor()(img) for img in 图片列表]

        # [torch.Tensor]->torch.Tensor
        # 合并的torch.Tensor = torch.stack(torch.Tensor列表)

        # (batch_size, channels, height, width) -> (batch_size, height, width, channels)
        # 调整维度顺序(1, 3, 1024, 1024)->(1, 1024, 1024, 3)
        tensor=noise.permute(0, 2, 3, 1)


        # 输出格式必须是tuple
        return (tensor,)

    # 注意：以上代码，只代表了该节点的功能，还需要通过__init__.py引入