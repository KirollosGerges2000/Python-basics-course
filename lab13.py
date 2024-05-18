#lab13 "Libraries lab13"
#scripted by: Eng/Kirollos Gerges

#using for bytes and integers
import random

print(random.gauss())

#for more modules  visit
#https://docs.python.org/3/py-modindex.html
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

import queue
check=queue.Full()
print(check)
