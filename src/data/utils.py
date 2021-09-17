from pathlib import Path
import yaml


def get_project_root():
    """Get the path of the project root directory.

    Returns
    -------
    pathlib.PosixPath
    """
    return Path(__file__).parents[2]


def load_config(*args):
    """Load the contents of a configuration file to a dictionary.

    Parameters
    ----------
    *args : str
        Directories and targeted configuration file.

    Returns
    -------
    dict
    """
    with open(get_project_root().joinpath(*args)) as file:
        config = yaml.safe_load(file)
    return config
