import sys

import requests


def main() -> None:
    print("Hello from learn-b!")
    print("解释器:", sys.executable)
    print("requests 版本:", requests.__version__)
