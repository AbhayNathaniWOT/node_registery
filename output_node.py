from node_factory import NodeFactory
import torch.nn as nn

@NodeFactory.register("outputnode")
class OutputNode:

    def __init__(self) -> None:
        print("This Is a output Node")

    @classmethod
    def module(cls):
        return nn.LeakyReLU

