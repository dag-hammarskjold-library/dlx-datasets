# DLX-Datasets
This is a package for of modules (usually in the form of srcipts) for generating reports and datasets from the DLX data (the database of the library catalague).

### Installation
Install this package into an active Python virtual environment using Pip:

`pip install dlx-datasets @ git+https://github.com/dag-hammarskjold-library/dlx-datasets@v1.0`

For developing against this repo, clone the repo, navigate to the root of the directory, and install it from the local source code in the virtual environment:

`pip install .`

### Scripts

#### eth-extract
Creates a custom dataset based on specified criteria and extracted data and writes it to JSON file.

##### Usage:
Fom the command line:

`eth-extract --help`
