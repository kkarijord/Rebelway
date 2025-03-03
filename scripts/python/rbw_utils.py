
def reload_package(kwargs):
    """
    Reloads the Houdini package and all Python modules in a specified directory.
    This function performs the following steps:
    1. Reloads the Houdini package specified by the path in the Houdini user preferences directory.
    2. Recursively walks through the specified directory and reloads all Python modules, except for "__init__.py".
    The paths for the Houdini package and the Python scripts directory are expanded using Houdini's text expressions.
    Raises:
        Exception: If there is an error importing or reloading a module, the error is caught and printed.
    Example:
        reload_package()
    """




    import hou
    import importlib
    import os
    import sys

    #reload the package
    package_path = hou.text.expandString("$HOUDINI_USER_PREF_DIR/packages"+ "/rebelway_tools.json")
    hou.ui.reloadPackage(package_path)
    #print(package_path)

    # reload the python modules
    folder_path = hou.text.expandString("$RBW/scripts/python")
    #print(folder_path)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.join(root, file).replace(os.sep,"/")
                module_name = os.path.relpath(module_path,folder_path).replace(os.sep,".").replace(".py","")
                # print(module_name)
                
                try: 
                    if module_name in sys.modules:
                        if kwargs["altclick"]:
                            importlib.reload(sys.modules[module_name])
                            print(f"Reloaded module: {module_name}")
                    else:
                        importlib.import_module(module_name)
                        print(f"{module_name} was imported")
                except Exception as error:
                    print(f"Failed to import or reload module {module_name}: {error}")

    #reload shelves
    shelves= hou.shelves.shelves()
    path_shelves = hou.text.expandString("$RBW/toolbar")

    for root, dir, files in os.walk(path_shelves):
        for file in files:
            if file.endswith(".shelf"):
                shelf_path = os.path.join(root, file).replace(os.sep,"/")
                hou.shelves.loadFile(shelf_path)
                #print(shelf_path)


def is_clicked(kwargs):
    if kwargs["altclick"]:
        print("Alt key was clicked")
    else:
        print("Alt key was NOT clicked")