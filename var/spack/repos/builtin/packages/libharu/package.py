##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import os


class Libharu(AutotoolsPackage):
    """libharu - free PDF library.

    Haru is a free, cross platform, open-sourced software library for
    generating PDF."""

    homepage = "http://libharu.org"
    url      = "https://github.com/libharu/libharu/archive/RELEASE_2_3_0.tar.gz"

    version('2.3.0', '4f916aa49c3069b3a10850013c507460')
    version('2.2.0', 'b65a6fc33a0bdad89bec6b7def101f01')
    version('master', branch='master',
            git='https://github.com/libharu/libharu.git')

    def autoreconf(self, spec, prefix):
        """execute their autotools wrapper script"""
        if os.path.exists('./buildconf.sh'):
            bash = which('bash')
            bash('./buildconf.sh', '--force')

    def url_for_version(self, version):
        url = 'https://github.com/libharu/libharu/archive/RELEASE_{0}.tar.gz'
        return url.format(version.underscored)
