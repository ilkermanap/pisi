#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()
    #autotools.configure("--with-linux=/usr/src/linux-headers-%s --with-gcc=%s --with-g++=%s"  % (kerneltools.getKernelVersion(), get.CC(), get.CXX())))

def build():
    autotools.make()

def install():
    autotools.install()

    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
