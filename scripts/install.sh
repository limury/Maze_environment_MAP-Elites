#!/bin/bash

cd ..

mkdir -p libs
cd libs

git clone https://github.com/alexendy/pyfastsim.git
cd pyfastsim

git clone https://github.com/jbmouret/libfastsim.git
cd libfastsim

patch -p1 < ../fastsim-boost2std-fixdisplay.patch

./waf configure
./waf build

cd ..
pip3 install .

cd ..
