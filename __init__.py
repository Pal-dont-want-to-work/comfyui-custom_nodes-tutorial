from .example1 import A
from .example2 import B
from .example3 import C
from .example4 import runnable_node
from .QR import QR_node

NODE_CLASS_MAPPINGS = {
    # "ui界面搜索节点名称": 对应实现的代码（类）
    "funtion A": A,
    "funtion B": B,
    "funtion C": C,
    "runnable_node": runnable_node,
    "QR_node": QR_node,
}