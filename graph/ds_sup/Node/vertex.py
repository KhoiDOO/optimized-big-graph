import os, sys
from typing import Any
sys.path.append(os.getcwd())
sys.path.append(os.pardir(os.getcwd()))

from node import Node

class Vertex(Node):
    def __init__(self, item) -> None:
        super().__init__(item)
        self_item = item