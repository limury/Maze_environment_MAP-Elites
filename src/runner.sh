#!/bin/bash

#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 uniform iso_dd                            $1
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 uniform polynomial                        $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 uniform sbx                               $1 
./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 uniform polynomial+sbx                    $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 uniform iso_dd+polynomial                 $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 uniform iso_dd+sbx                        $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 uniform iso_dd+polynomial+sbx             $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity iso_dd                          $1
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity polynomial                      $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity sbx                             $1 
./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity polynomial+sbx                  $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity iso_dd+polynomial               $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity iso_dd+sbx                      $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity iso_dd+polynomial+sbx           $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity-child iso_dd                    $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity-child polynomial                $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity-child sbx                       $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity-child polynomial+sbx            $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity-child iso_dd+polynomial         $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity-child iso_dd+sbx                $1 
#./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 curiosity-child iso_dd+polynomial+sbx     $1 
./run_map_elites.py ./worlds/LS_maze_hard.xml 500000 200 20000 random_search iso_dd+polynomial+sbx     $1 
