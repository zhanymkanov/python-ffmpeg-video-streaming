"""
ffmpeg_streaming.streams
~~~~~~~~~~~~

Useful methods


:copyright: (c) 2020 by Amin Yazdanpanah.
:website: https://www.aminyazdanpanah.com
:email: contact@aminyazdanpanah.com
:license: MIT, see LICENSE for more details.
"""
import logging
import os
import re
import warnings
from sys import platform


def get_path_info(path):
    """
    @TODO: add documentation
    """
    dirname = os.path.dirname(path)
    name = str(os.path.basename(path).split('.')[0])

    return dirname, name


def mkdir(dirname: str) -> None:
    """
    @TODO: add documentation
    """
    try:
        os.makedirs(dirname)
    except OSError as exc:
        logging.info(exc)
        pass


def clean_args(args: list) -> list:
    """
    @TODO: add documentation
    """
    clean_args_ = []
    for arg in args:
        if " " in arg:
            arg = '"' + arg + '"'
        clean_args_.append(arg.replace("\\", "/"))

    return clean_args_


def convert_to_sec(time):
    """
    @TODO: add documentation
    """
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def get_time(key, string):
    """
    @TODO: add documentation
    """
    time = re.search('(?<=' + key + ')\w+:\w+:\w+', string)
    if time:
        return convert_to_sec(time.group(0))


def deprecated(func):
    """
    @TODO: add documentation
    """
    def deprecated_fun(*args, **kwargs):
        warnings.warn('The {} method is deprecated and will be removed in a future release'.format(func.__name__)
                      , DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)
    return deprecated_fun


def get_os():
    """
    @TODO: add documentation
    """
    if platform == "linux" or platform == "linux2":
        os_name = 'linux'
    elif platform == "darwin":
        os_name = 'os_x'
    elif platform == "win32" or platform == "Windows":
        os_name = 'windows'
    else:
        os_name = 'unknown'

    return os_name


def cnv_options_to_args(options: dict):
    """
    @TODO: add documentation
    """
    args = []
    for k, v in options.items():
        args.append('-{}'.format(k))
        if v is not None:
            args.append('{}'.format(v))

    return args