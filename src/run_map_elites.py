#!/usr/bin/env python3

import sys
import numpy as np
import time
from pyfastsim import *
import agents

from pymap_elites.map_elites import cvt as cvt_map_elites


def eval( geno ):
    # get new map and robot
    env_map = settings.map()
    robot = settings.robot()
    geno = geno * 2.0 - 1.0
    # time loop
    for i in range(500):
        # get current laser reading
        laser_reading = np.array([ x.get_dist() for x in robot.get_lasers() ] )
        laser_reading = laser_range - laser_reading
        #for i, num in enumerate(laser_reading):
            #laser_reading[i] = laser_range - num
        laser_reading /= laser_range
        laser_reading = np.append(laser_reading, np.array([i/200]))
        # calculate move from neural network
        move = NN.forward_pass(laser_reading, geno).flatten() * 5
        robot.move(move[0], move[1], env_map, sticky_walls = True)
    pos = robot.get_pos()
    x = float(pos.x()) / 600
    y = float(pos.y()) / 600
    BD = [(x, y)]

    return 0, BD

   


if __name__ == "__main__":
    sizes = [6, 5, 2]
    NN = agents.NNAgent(sizes)
    laser_range = 100 
    if(len(sys.argv) < 2):
    	print("This program cannot run: you need to provide a XML file (e.g.,%s worlds/example.xml)" % sys.argv[0])
    	sys.exit(1)

    settings = Settings(sys.argv[1])

    gui = False # Plot environment animation ?
    n = 10000 # Number of iterations

    # storage directory for results
    log_dir = sys.argv[7]
    # num evals
    n_evals = int(sys.argv[2])
    # additional mutations
    variant = "" 
    if len(sys.argv) > 8:
        variant = sys.argv[8:]
    
    t = time.time()
    px = \
        {
            # more of this -> higher-quality CVT
            "cvt_samples": 25000,
            # we evaluate in batches to parallelize
            "batch_size": int(sys.argv[3]),
            # proportion of niches to be filled before starting
            "random_init": 0.02,
            # batch for random initialization
            "random_init_batch": int(sys.argv[3]),
            # when to write results
            "dump_period": int(sys.argv[4]),
            # do we use several cores?
            "parallel": True,
            # do we cache the result of CVT and reuse?
            "cvt_use_cache": False,
            # min/max of parameters
            "min": 0,
            "max": 1,
            # probability of mutating each number in the genotype
            "mutation_prob": 0.5,
            # selector ["uniform", "curiosity", "random_search"]
            "selector" : sys.argv[5],
            # mutation operator ["iso_dd", "polynomial", "sbx", "gaussian"]
            "mutation" : sys.argv[6],
            "variant" : variant, 
            "eta_m" : 50.0,
            "iso_sigma": 0.01,
            "line_sigma": 0.1,
            "std_dev" : 0.01
            }

    with open(log_dir+"/config.txt", 'w') as f:
        f.write(str(px) + "\n\nNetwork size: " + str(sizes) + "\n\nEvals: " + str(n_evals) + "\n\nLaser Range: " + str(laser_range))
    
    archive = cvt_map_elites.MapElites(2, NN.size(sizes), eval, n_niches=130*130, max_evals=n_evals, log_file=None, params=px, bins=[130, 130], log_dir=log_dir)
    
    

