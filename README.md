# TelloPilot

TelloPilot is a collection of experiments using DJI's Tello SDK to communicate with the Tello drone. For ease of use, the [TelloPy](https://github.com/hanyazou/TelloPy) package is used for the communication protocol.

Currently, the supported features include:

* Controlling the drone with a keyboard
* Face detection using computer vision

## Setup
This project was implemented and run on a Windows machine. To setup the project:

1. Create a Python virtual environment:
```
python -m venv venv
```

2. Activate the virtual environment:
```
source venv/Scrips/activate   (Windows)

or

source venv/bin/activate      (Mac/Linux)
```

2. Install the requirements:
```
pip install -r requirements.txt
```

For Windows, use instead
```
pip install -r requirements-windows.txt
```
This is due to issues with installing `PyAV` on Windows. To resolve this, the package must be installed manually.

### Installing PyAV (Windows only)

PyAV depends on `ffmpeg` to work, and so they must be downloaded first.

1. Download `ffmpeg` (both the [shared and dev packages](https://ffmpeg.zeranoe.com/builds/)).
2. Unpack both packages somewhere on your local machine (e.g. `C:\ffmpeg`).
3. Clone or download the zip of [PyAV](https://github.com/mikeboers/PyAV) in this project's directory. If the zip is downloaded, make sure to unpack it.
4. `cd` into the `PyAV` directory and run `python setup.py build --ffmpeg=\\path\\to\\ffmpeg`. Make sure your Python virtual environment is activated first.
5. Install `PyAV` with `python setup.py install`. Once this is done, you can safely remove the cloned `PyAV` repo.

## Running the project
To get the project started, run `python main.py` in the `src` directory.