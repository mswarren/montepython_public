#!/usr/bin/env python
"""
.. module:: MontePython
   :synopsis: Main module
.. moduleauthor:: Benjamin Audren <benjamin.audren@epfl.ch>

Monte Python, a Monte Carlo Markov Chain code (with Class!)
"""
import sys
import warnings

import io_mp       # all the input/output mechanisms
from run import run


#-----------------MAIN-CALL---------------------------------------------
if __name__ == '__main__':
    # Default action when facing a warning is being remapped to a custom one
    warnings.showwarning = io_mp.warning_message

    sys.exit(run())
