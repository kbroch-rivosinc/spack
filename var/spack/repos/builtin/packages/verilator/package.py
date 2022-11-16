# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Verilator(AutotoolsPackage):
    """Verilator is the fastest free Verilog HDL simulator.

    It compiles synthesizable Verilog (not test-bench code!), plus some PSL,
    SystemVerilog and Synthesis assertions into C++ or SystemC code. It is
    designed for large projects where fast simulation performance is of primary
    concern, and is especially well suited to generate executable models of
    CPUs for embedded software design teams.

    Please do not download this program if you are expecting a full featured
    replacement for NC-Verilog, VCS or another commercial Verilog simulator
    or Verilog compiler for a little project! (Try Icarus instead.) However, if
    you are looking for a path to migrate synthesizable Verilog to C++ or
    SystemC, and writing just a touch of C code and Makefiles doesn't scare you
    off, this is the free Verilog compiler for you.

    Verilator supports the synthesis subset of Verilog, plus initial
    statements, proper blocking/non-blocking assignments, functions, tasks,
    multi-dimensional arrays, and signed numbers. It also supports very simple
    forms of SystemVerilog assertions and coverage analysis. Verilator supports
    the more important Verilog 2005 constructs, and some SystemVerilog
    features, with additional constructs being added as users request them.

    Verilator has been used to simulate many very large multi-million gate
    designs with thousands of modules."""

    homepage = "https://www.veripool.org/projects/verilator"
    url = "https://github.com/verilator/verilator/archive/refs/tags/v5.002.tar.gz"

    version("5.002", sha256="72d68469fc1262e6288d099062b960a2f65e9425bdb546cba141a2507decd951")
    version("4.228", sha256="be6af6572757013802be5b0ff9c64cbf509e98066737866abaae692fe04edf09")
    version("4.226", sha256="70bc941d86e4810253d51aa94898b0802d916ab76296a398f8ceb8798122c9be")
    version("4.224", sha256="010ff2b5c76d4dbc2ed4a3278a5599ba35c8ed4c05690e57296d6b281591367b")
    version("4.222", sha256="15c60175807c0f3536c3c5b435f131c2b1e8725aefd30645efd946bf401b4c84")
    version("4.220", sha256="e00e0c31a0c00887bebbaf7a8c771efa09420a4d1fbae54d45843baf50df4426")
    version("4.218", sha256="ef7b1e6ddb715ddb3cc998fcbefc7150cfa2efc5118cf43ddb594bf41ea41cc7")
    version("4.216", sha256="64e5093b629a7e96178e3b2494f208955f218dfac6f310a91e4fc07d050c980b")
    version("4.214", sha256="e14c7f6ffb00a6746ae2a8ea0424e90a1a30067e8ae4c96b8c42689ca1ca0b1f")
    version("4.212", sha256="7b655859e4e75c9673141aede8f5a20f47e4c380055d1a588d5be60cbbc73619")
    version("4.210", sha256="3a2e6f27a5d80116a268ba054a3be61aca924bc54c5556ea25e75ee974201abb")
    version("4.204", sha256="dbad9bd3cac34e63bbd945fff9a59eaabe31dae1e1c93c847d0f894db9919498")
    version("4.202", sha256="a60c02f299ddb5bb8e963dc7d81983c55c293d97718685c1cd4b66638a33d98e")
    version("4.200", sha256="2cd0fd48152f152d0487eaac23803d35ff75e924734435b366a523deb1185407")
    version("4.110", sha256="603c23944577a5d53a2e09191d04d5c61740a77b58f3a590a70e56f4526a5a0b")
    version("4.108", sha256="ce521dc57754e5a325ff7000c434ce23674c8e1de30e1f2a6506dc3a33bd7c55")
    version("4.106", sha256="023327b30b68268c6cbf2debf8e8587ea5340b1b0e8b119776a3e7a9e5124140")
    version("4.104", sha256="6d42fa468234461e4a0c3154d5602cdded7b22d57f14be92c27a65d418a4a010")
    version("4.102", sha256="4e4f4aff00af9a15a61c94b67ed070cd6312ddcc0f0d340a6df2199480064cef")
    version("4.100", sha256="031ddd24be38a996e9dc3cf8591fca7cd06b7d21b88e5648ead386d3ec445ba3")
    version("4.040", sha256="40cf8d2e14a17a94c92b3e731b4a9793935f01a2e68b8657ffc778c7b74d9c5d")
    version("4.038", sha256="0a4a11ae9ca64aa995b1c5895e4367043a72fa4cf89a6781b6877b0f78b27863")
    version("4.036", sha256="856b365ffb803f211960761dee263bb06d893a780bee3cbc8c2575a6c0030da1")
    version("4.034", sha256="17a087fc74fd1ab035a43ba38d6f6198150ee11b20077855404ddb4c1620c6b7")
    version("4.032", sha256="c1f1d4083a05313d9e8f254c322668246a66ede4910843ddb2c7b6b9ba4b147e")
    version("4.030", sha256="04894d06785e2e9b6b504d21e551a62436bff0526fd766100ed8beff94afdeac")
    version("4.028", sha256="cb13e4f54920e6e35ef51a96476d0547d2a60fdc0c61198df4bcd4d29c246680")
    version("4.026", sha256="d3961e83f2e9e7fa28d23e04624fe8b92b1182349d8afae7c7639fc333d9d38e")
    version("4.024", sha256="4feaf8fb950a5ccc0fc495cc4349d251af5a7575ac76df9d20d015793db8bf14")
    version("4.022", sha256="8577c09c1d65af830a9017232b4934a6e9c84c5ee9839d8914d85bef19e60270")
    version("4.020", sha256="e19ccbaad305d7aa2a0e56fc1a1629c4db1b4abd7f4530b9c035ee715217f3f2")
    version("4.018", sha256="8cbbc939310edb5ed33ea1a41b9b3c5b57e397e4d913ff183c6e6ae90faa8c8d")
    version("4.016", sha256="dc0291f2d503816ed464afc38d346bbc75d248109ef5c6fec2a0bad40c5b2c5d")
    version("4.014", sha256="a54c8c88f2cf15f8f56f5b0eba56d03fc8d9302a3462652001d7cc96203db678")
    version("4.012", sha256="c41b3e4d2ef33f0b4da6c606ce18a31baac72f89b0f8c5916f5ced33a1b05c54")
    version("4.010", sha256="3c67f1adaf72de9e78fc6a8e840da2b902fd5ef4df331888f0382987e4f80e8c")
    version("4.008", sha256="d2146be974506613be233aff3f3a7ec5a34847d7d2bbd5e08697af9e44819fe8")
    version("4.006", sha256="10273c9adbe8a581f39ed9c8f7a2d837d98438295ecfb3ce153868ffe03c1361")
    version("4.004", sha256="54b1219cb086d0490931871e03f2a98a571008bca8530c6a5ebacce72d7cd64a")
    version("4.002", sha256="135ce322766f6a0526c9a34641b242bb140b0107288b20bf534fc9614edbf530")
    version("3.926", sha256="63f3607e9517851dc1b2263f3400390d850b30b46095f0f0df648c6762d8a2cf")
    version("3.924", sha256="5eb4484362b1bcca0001bd2d8ed4a84b87331c05b22b4ab1099c8f003d8c285a")
    version("3.922", sha256="9b44e3c1a90c2cf78a8bb533aca57a61628717948ef4811e757b54464f625b33")
    version("3.920", sha256="9490496ad3deeef39a8b57d0e0474a8aee20732732c5aa458cc50a049c7c74e1")
    version("3.918", sha256="05fbf9f8b65ea4bb1052a178d2977216c3ce6b936c1984e61d7f99e18f483760")
    version("3.916", sha256="a9e6a573cb41aff5411ce3e02618b8efecc9805e1531846f4baf310b27a40585")
    version("3.914", sha256="0550d0cedfedaff82871353fd5137890b9eafd5ef1d3a43b721d2c8d8bbb6590")
    version("3.912", sha256="e0d6c336ec60e91d79f99ddd0bc5014449e0bccfb1ede34939173016259cab72")
    version("3.910", sha256="06c084905216aa7f38177a50811cf6e52cf6955863429c76e6118047e89e17bf")
    version("3.908", sha256="e48c3ba42bf01c6ff3b604fe77df081f82ff865dac279abaab87ff0585f282c6")
    version("3.906", sha256="dca2c0aa58e2b4dca83a536ea3c40e0cbaca05d82f87d55d4f22907651a962f3")
    version("3.904", sha256="a0100b6c620cdf96a968099b60ada8e183dec385483ece74f0936aebb1990d93")
    version("3.902", sha256="6606cb67f3c425c749d722e1141372429b6bcb678062d5ddc83df31df518cc03")
    version("3.900", sha256="69537d7c4859ac6256613262523ea545f150c7afd892e2a731ffff2603eceb8e")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("bison", type="build")
    depends_on("flex")
    depends_on("libtool", type="build")
    depends_on("perl", type=("build", "run"))

    # def setup_run_environment(self, env):
    #     env.prepend_path("VERILATOR_ROOT", self.prefix)

    def autoreconf(self, spec, prefix):
        which("bash")("autoconf")

    # verilator requires access to its shipped scripts (bin) and include
    # but the standard make doesn't put it in the correct places
    # @run_before("install")
    # def install_include(self):
    #     install_tree("include", prefix.include)
    #     install_tree("bin", prefix.bin)

    # we need to fix the CXX and LINK paths, as they point to the spack
    # wrapper scripts which aren't usable without spack
    # @run_after("install")
    # def patch_cxx(self):
    #     filter_file(
    #         r"^CXX\s*=.*",
    #         "CXX = {0}".format(self.compiler.cxx),
    #         join_path(self.prefix.include, "verilated.mk"),
    #     )
    #     filter_file(
    #         r"^LINK\s*=.*",
    #         "LINK = {0}".format(self.compiler.cxx),
    #         join_path(self.prefix.include, "verilated.mk"),
    #     )
