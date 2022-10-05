# copy pasted, couldn't write one for this repo cuz lazy

import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    if plugin_name.startswith("__"):
    	pass
    else:
    	path = Path(f"MeshRenameBot/{plugin_name}.py")
    	name = "MeshRenameBot.{}".format(plugin_name)
    	spec = importlib.util.spec_from_file_location(name, path)
    	load = importlib.util.module_from_spec(spec)
    	load.logger = logging.getLogger(plugin_name)
    	spec.loader.exec_module(load)
    	sys.modules["MeshRenameBot." + plugin_name] = load
    	logging.info("✨ MeshRenameBot has Imported " + plugin_name)
