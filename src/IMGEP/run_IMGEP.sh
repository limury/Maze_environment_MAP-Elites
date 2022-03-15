#!/bin/bash


python3 run.py $1 0 none random False rmb 100000 5000
python3 run.py $1 0 none random False FRGB 100000 5000
python3 run.py $1 0 none random False RMB 100000 5000
python3 run.py $1 0 none random False AMB 100000 5000

python3 run.py $1 0 none gaussian False rmb 100000 5000
python3 run.py $1 0 none gaussian False FRGB 100000 5000
python3 run.py $1 0 none gaussian False RMB 100000 5000
python3 run.py $1 0 none gaussian False AMB 100000 5000

python3 run.py $1 0 none full False rmb 100000 5000
python3 run.py $1 0 none full False FRGB 100000 5000
python3 run.py $1 0 none full False RMB 100000 5000
python3 run.py $1 0 none full False AMB 100000 5000

python3 run.py $1 0 none random True rmb 100000 5000
python3 run.py $1 0 none random True FRGB 100000 5000
python3 run.py $1 0 none random True RMB 100000 5000
python3 run.py $1 0 none random True AMB 100000 5000

python3 run.py $1 0 none gaussian True rmb 100000 5000
python3 run.py $1 0 none gaussian True FRGB 100000 5000
python3 run.py $1 0 none gaussian True RMB 100000 5000
python3 run.py $1 0 none gaussian True AMB 100000 5000

python3 run.py $1 0 none full True rmb 100000 5000
python3 run.py $1 0 none full True FRGB 100000 5000
python3 run.py $1 0 none full True RMB 100000 5000
python3 run.py $1 0 none full True AMB 100000 5000
