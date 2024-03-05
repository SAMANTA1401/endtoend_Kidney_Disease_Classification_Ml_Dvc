import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns
 
    Args:
        path_to_yaml(str):path like input

    Raised:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content) ##root_dir=config.root_dir,source_URL = config.source_URL,local_data_file = config.local_data_file,unzip_dir = config.unzip_dir
    except BoxValueError:
        raise Exception("yaml file has no value")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories(list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created,
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """save dictionary into a json file
    Args:
    path (Path): path where the json file will be saved
    data (dict): data that needs to be stored in json format
    """
    with open(path,"w") as f: #write mode
        json.dump(data,f,format=4) ##The `json.dump()` function is used to write JSON data to a file. The `data` parameter contains the JSON data you want to write, while `f` is the file object where you want to write the JSON data. The `format=4` parameter specifies the indentation level for formatting the JSON output. In this case, `format=4` means the JSON data will be indented with 4 spaces for readability.

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path) -> ConfigBox:
    """Load JSON from a given path and returns it as a ConfigBox object
    Args:
    path (Path): path to the json file
    
    Returns:
    ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from:{path}")
    return ConfigBox(content)
    
@ensure_annotations
def save_bin(data:Any, path:Path):
    """save binarry file

    Args:
    data(Any): data to be saved as binary
    path(Path): apath to binary file

    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    """ load binary data
    Args:
    path(Path): path to binary file

    Returns:
    Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from:{path}")

@ensure_annotations
def get_size(path:Path) -> str:
    """get size in kb
    Args:
    path(Path): path of the file
    Returns:
    str: size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} kb"

def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)  ##This line of code decodes the base64 encoded string `imgstring` into binary data and assigns it to the variable `imgdata`. This is commonly used when dealing with images encoded in base64 format, as it allows you to convert the encoded data back into its original binary form for further processing or display.
    with open(filename, 'wb') as f: #write in binary mode
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f: #read in binary mode
        return base64.b64decode(f.read())

##A binary file is a type of computer file that stores data in a format composed of 0s and 1s, representing different types of information. Unlike text files, which store data using characters, binary files store data in a form that is directly understandable by the computer's hardware.
##Binary files can contain any type of data, including text, images, audio, video, executables, or any other type of information. Because binary files store data in a raw format, they are often more compact and efficient than text files, especially for storing complex data structures or multimedia content.