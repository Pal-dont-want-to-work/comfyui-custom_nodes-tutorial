##############################################################
# 1.定义一个C，一个节点就是一个类。comfyui会引入这个类作为一个节点
##############################################################
class C:
    def __init__(self):
        pass
        
    ##############################
    # 2. 使用关键的标识符来表示该节点
    ##############################
    CATEGORY = "😀😀😀my custom plugin:C_example😀😀😀"

    ###############
    # 3.节点左侧输入
    ###############
    @classmethod
    def INPUT_TYPES(s):
        return {
            # 以下是节点中大部分的输入类型，包括必选输入（required），可选输入（optional），隐藏输入（hidden）。这些输入会传递给函数，作为参数
            # 如果不知道输入类型，可以参考ComfyUI_windows_portable\ComfyUI\extra_model_paths.yaml.example和ComfyUI_windows_portable\ComfyUI\nodes.py
            
            # 必选输入
            "required": {

                "pipe": ("PIPE_LINE",),

                "参数：整数": ("INT", {
                    "default": 20,  # 默认
                    "min": 1,
                    "max": 10000,
                    "step": 2,  # 步长
                    "display": "number"}),  # 数值调整

                "参数：浮点数": ("FLOAT", {
                    "default": 1.0,
                    "min": -10.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001,  # 精度
                    "display": "slider"}),  # 滑动调整

                "参数：字符串": ("STRING", {
                    "default": "Pal教你自定义custom_node https://h0zkh0f8v2a.feishu.cn/wiki/KUnlwgJxSidQi7k0Iq3cUvGpnLS?from=from_copylink",  # 默认存在内容
                    "multiline": True}),  # 是否允许多行输入

                "参数：布尔值": ("BOOLEAN", {
                    "default": True}),

                "下拉选择框": (["None"] + ["enable", "disable"],),  # 括号里是一个列表
            },

            # 可选输入
            "optional": {
                "model": ("MODEL",),
                "vae": ("VAE",),
                "clip": ("CLIP",),

                "latent": ("LATENT",),
                "image": ("IMAGE",),

                "pos": ("CONDITIONING",),
                "neg": ("CONDITIONING",),

                "xyPlot": ("XYPLOT",),
            },

            # 隐藏输入
            "hidden": {"my_unique_id": "UNIQUE_ID"},  # comfyui内部任务id
        }

    # 以下是节点中大部分的输出类型。输出类型必须大写，ui显示名称可自定义
    OUTPUT_NODE = True
    # 输出的数据类型，需要大写
    RETURN_TYPES = ("0.PIPE_LINE","1.MODEL","2.VAE","3.CLIP","4.LATENT","5.IMAGE","6.CONDITIONING","7.CONDITIONING","8.INT", "9.FLOAT", "10.STRING",)
    # 自定义输出名称
    RETURN_NAMES = ("0.pipe_line","1.model","2.vae","3.clip","4.latent","5.image","6.pos","7.neg","8.整数","9.浮点数","10.字符串",)

    ##############################
    # 5. 节点的核心功能逻辑在这里定义
    ##############################
    FUNCTION = "test" # 核心功能函数名称，将运行这个类中的这个方法

    def test(self,):
        pass

    # 注意：以上代码，只代表了该节点的功能，还需要通过__init__.py引入