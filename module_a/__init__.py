import glob
import importlib.util
from pathlib import Path
import sys


# dynamically import all files matching pattern + extract function
pattern = Path(__file__).parent / "create_*"
files = glob.glob(str(pattern))
for file in files:
    module_name = Path(file).stem
    spec = importlib.util.spec_from_file_location(module_name, file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    globals()[module_name] = module.execute


# cleanup namespace
del file
del files
del module
del module_name
del spec
