Setting Up
----
First, make sure you have Python 3.\* and the latest pip >= 20.\* (Check the `Notes & FAQ` section below if you're having trouble with this). Then, here is the preferred way to set up (if you have another way, feel free to do it):

1. Install [anaconda](https://docs.anaconda.com/anaconda/install/) to set up a virtual environment
2. `conda create -n sudoku python=3.10`
3. `conda activate sudoku`
4. To install PyGame, `pip install pygame`. 
 
You can run `conda deactivate` to deactivate the environment. The next time you want to work on the game, type `conda activate sudoku` first to use the exact same environment with PyGame installed.

Usage
----
In the main.py on `line 211`, replace the prop_tc text string with your unique Sudoku problem. From left to right to top to bottom, type the numbers in and for the blank spots put a period `.`. Save the file. 

Simply run `python main.py`

Tips & FAQ
------

**I'm having trouble loading up Pygame after installing it on MacOS.**
- If you encounter difficulty loading things after installing Pygame, this post https://stackoverflow.com/questions/52718921/problems-getting-pygame-to-show-anything-but-a-blank-screen-on-macos-mojave (in particular, the second answer by "Rafael") may likely help you. 

**Why does `python` show up as Python 2.\* instead of Python 3.\*?**
- If `python --version` shows Python 2.\*, but `python3 --version` shows Python 3.\*, you will either need to run all your commands with `python3` (e.g. `python3 main.py`) or change your default `python` to Python 3.\*. All `python` commands we make going forward will be assumed to be Python 3.\*. Here's a [link](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3) that shows you how to set `python` to Python 3.\* by default instead of Python 2.\*. 

**My pip shows a version lower than 20.\*; how do I update it?**
- First, check if you have the right Python version; your pip version should be up to date if you have the correct Python. If this isn't the case, check [this](https://pip.pypa.io/en/stable/installation/#upgrading-pip) out.

**My system says `pip not found` when I try to run `pip`. What do I do?**
- First, check that you have Python 3.\* installed correctly. If you can't find any problems there, here's a [resource](https://pip.pypa.io/en/stable/installing/) you can check out. Again, all `pip` commands we make going forward are assumed with the latest `pip` version (>=20.\*).
