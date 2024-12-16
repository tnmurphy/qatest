import os
import sys
from pathlib import Path

# add the parent directory so that we can import 
# the modules that we want to test
test_root = str(Path(__file__).absolute().parents[1])
sys.path.append(test_root)
if "PYTHONPATH" not in os.environ:
    os.environ["PYTHONPATH"] = test_root
else:
    os.environ["PYTHONPATH"] += ":" + test_root

