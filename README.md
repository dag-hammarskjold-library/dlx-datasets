# python-package-template
Template for creating Python packages. 

This template provides a skeleton directory structure for creating a [Python package](https://docs.python.org/3/tutorial/modules.html#packages). Python packages are collections of one or more [Python modules](https://docs.python.org/3/tutorial/modules.html). The package is configured in the file `setup.py`.

Packages are meant to be installed into a Python environent uisng [`pip`](https://pypi.org/project/pip/). These packages can be installed directly from the GitHub source code, i.e. `pip install git+<repository URL>`

Once the package is installed, the modules in the package can be imported into another Python file using [`import`](https://docs.python.org/3/reference/import.html). Modules can also be command-line applications or scripts. 