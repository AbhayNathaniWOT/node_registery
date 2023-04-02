from node_factory import NodeFactory
import torch.nn as nn

@NodeFactory.register("inputnode")
class InputNode:

    def __init__(self) -> None:
        print("This Is a Input Node")
    
    @classmethod
    def module(cls):
        return nn.AvgPool2d




    