#!/usr/bin/env python

import os
import sys
import subprocess as sps
from ..assemble.utils import IPyradError


class Bins(object):
    """
    Get binaries that should be shipped with ipyrad
    """
    def __init__(self):
        self._getbins()
        self._testbins()

    def _getbins(self):
        "Find path to software versions"
    
        # Return error if system is 32-bit arch.
        if not sys.maxsize > 2 ** 32:
            raise IPyradError("ipyrad requires 64bit architecture")

        ## get binary directory
        ipyrad_path = os.path.dirname(os.path.dirname(
            os.path.abspath(os.path.dirname(__file__))))
        bin_path = os.path.join(ipyrad_path, "bin")

        ## get the correct binaries
        if 'linux' in sys.platform:
            self.vsearch = os.path.join(
                os.path.abspath(bin_path), "vsearch-linux-x86_64")
            self.muscle = os.path.join(
                os.path.abspath(bin_path), "muscle-linux-x86_64")
            self.bwa = os.path.join(
                os.path.abspath(bin_path), "bwa-linux-x86_64")
            self.samtools = os.path.join(
                os.path.abspath(bin_path), "samtools-linux-x86_64")
            self.bedtools = os.path.join(
                os.path.abspath(bin_path), "bedtools-linux-x86_64")
        else:
            self.vsearch = os.path.join(
                os.path.abspath(bin_path), "vsearch-osx-x86_64")
            self.muscle = os.path.join(
                os.path.abspath(bin_path), "muscle-osx-x86_64")
            self.bwa = os.path.join(
                os.path.abspath(bin_path), "bwa-osx-x86_64")
            self.samtools = os.path.join(
                os.path.abspath(bin_path), "samtools-osx-x86_64")
            self.bedtools = os.path.join(
                os.path.abspath(bin_path), "bedtools-osx-x86_64")


    def _testbins(self):
        # Test for existence of binaries
        for cmd in ['muscle', 'vsearch', 'bwa', 'samtools', 'bedtools']:
            cmdcall = self.__getattribute__(cmd)
            assert self._cmd_exists(cmdcall), ("{} not found here: {}"
                .format(cmd, cmdcall))


    def _cmd_exists(self, cmd):
        """ check if dependency program is there """
        return sps.call("type " + cmd,
                        shell=True,
                        stdout=sps.PIPE,
                        stderr=sps.PIPE) == 0
