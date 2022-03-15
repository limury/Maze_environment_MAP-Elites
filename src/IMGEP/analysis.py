import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
import imageio
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import ImageGrid
import seaborn as sns

ARCHIVE_PATH = "./" #"../results/"

filenames = []
new_dir = "./Cmaps_scatter"
try:
    os.mkdir(new_dir)
except OSError as error:
    pass



names = [ "cmd_1", "cmd_2", "cmd_3", "cmd_4", "hand_x", "hand_y", "gripper", "tool1_x", "tool1_y", "tool2_x", "tool2_y", "magnet1_x", "magnet1_y", "magnet2_x", "magnet2_y", "magnet3_x", "magnet3_y", "scratch1_x", "scratch1_y", "scratch2_x","scratch2_y", "scratch3_x", "scratch3_y", "distractor1_x", "distractor1_y", "distractor2_x", "distractor2_y", "static1_x", "static1_y", "static2_x", "static2_y", "static3_x", "static3_y", "static4_x", "static4_y"]
BD_names = ["hand_x", "hand_y", "tool1_x", "tool1_y", "tool2_x", "tool2_y", "magnet1_x", "magnet1_y", "magnet2_x", "magnet2_y", "magnet3_x", "magnet3_y", "scratch1_x", "scratch1_y", "scratch2_x","scratch2_y", "scratch3_x", "scratch3_y", "distractor1_x", "distractor1_y", "distractor2_x", "distractor2_y", "static1_x", "static1_y", "static2_x", "static2_y", "static3_x", "static3_y", "static4_x", "static4_y"]
all_names = [ x +"_t"+ str(t) for t in range(5) for x in names ]

# for i in range(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])):
   
data = pd.read_csv("20-none-full-True-AMB-100000-data.csv", \
            names = all_names)
data = data.drop( [ x +"_t"+ str(t) for t in range(4) for x in names ]\
            , axis = 1)
data = data.drop(["cmd_1_t4", "cmd_2_t4", "cmd_3_t4", "cmd_4_t4", "gripper_t4"], axis = 1)

# normalize to [0, 1]
for name in BD_names:
    data[name+"_t4"] = data[name+"_t4"].apply(lambda x: x/4 + 0.5)
# discretizing the data into bins
for name in BD_names:
    data[name + "_bin"] = pd.cut(x = data[name + "_t4"],
                                bins = [ p/100 for p in range(101) ],
                                labels = [ p for p in range(100)] )


arr = np.empty((15, 100, 100))
arr[:] = np.NaN

graph_data = {
    "hand"          : np.empty((100, 100)),
    "tool1"         : np.empty((100, 100)),
    "tool2"         : np.empty((100, 100)),
    "magnet1"       : np.empty((100, 100)),
    "magnet2"       : np.empty((100, 100)),
    "magnet3"       : np.empty((100, 100)),
    "scratch1"      : np.empty((100, 100)),
    "scratch2"      : np.empty((100, 100)),
    "scratch3"      : np.empty((100, 100)),
    "distractor1"   : np.empty((100, 100)),
    "distractor2"   : np.empty((100, 100)),
    "static1"       : np.empty((100, 100)),
    "static2"       : np.empty((100, 100)),
    "static3"       : np.empty((100, 100)),
    "static4"       : np.empty((100, 100))
}
for key in graph_data:
    graph_data[key][:] = np.NaN

for index, row in data.iterrows(): 
    
    graph_data["hand"       ] [int(row["hand"       + "_x_bin"]), int(row["hand"       + "_y_bin"])] = 0   
    graph_data["tool1"      ] [int(row["tool1"      + "_x_bin"]), int(row["tool1"      + "_y_bin"])] = 0   
    graph_data["tool2"      ] [int(row["tool2"      + "_x_bin"]), int(row["tool2"      + "_y_bin"])] = 0   
    graph_data["magnet1"    ] [int(row["magnet1"    + "_x_bin"]), int(row["magnet1"    + "_y_bin"])] = 0   
    graph_data["magnet2"    ] [int(row["magnet2"    + "_x_bin"]), int(row["magnet2"    + "_y_bin"])] = 0   
    graph_data["magnet3"    ] [int(row["magnet3"    + "_x_bin"]), int(row["magnet3"    + "_y_bin"])] = 0   
    graph_data["scratch1"   ] [int(row["scratch1"   + "_x_bin"]), int(row["scratch1"   + "_y_bin"])] = 0   
    graph_data["scratch2"   ] [int(row["scratch2"   + "_x_bin"]), int(row["scratch2"   + "_y_bin"])] = 0   
    graph_data["scratch3"   ] [int(row["scratch3"   + "_x_bin"]), int(row["scratch3"   + "_y_bin"])] = 0   
    graph_data["distractor1"] [int(row["distractor1"+ "_x_bin"]), int(row["distractor1"+ "_y_bin"])] = 0   
    graph_data["distractor2"] [int(row["distractor2"+ "_x_bin"]), int(row["distractor2"+ "_y_bin"])] = 0   
    graph_data["static1"    ] [int(row["static1"    + "_x_bin"]), int(row["static1"    + "_y_bin"])] = 0   
    graph_data["static2"    ] [int(row["static2"    + "_x_bin"]), int(row["static2"    + "_y_bin"])] = 0   
    graph_data["static3"    ] [int(row["static3"    + "_x_bin"]), int(row["static3"    + "_y_bin"])] = 0   
    graph_data["static4"    ] [int(row["static4"    + "_x_bin"]), int(row["static4"    + "_y_bin"])] = 0   
    

labels = ["hand", "tool1", "tool2", "magnet1", "magnet2", "magnet3", "scratch1", "scratch2", "scratch3", "distractor1", "distractor2", "static1", "static2", "static3", "static4"]

for k in range(15):

    fig, ax = plt.subplots(figsize=(12,10)) 

    #mynorm = mpl.colors.Normalize(vmin=-1.5, vmax=0, clip = 0.1)
    plt.imshow(graph_data[labels[k]], plt.cm.get_cmap('viridis'), interpolation='nearest')
    cbar = plt.colorbar()
    
    

    plt.savefig(new_dir + "/img"+"_"+labels[k]+".png", dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format='png',
            transparent=False, bbox_inches="tight", pad_inches=0.1, metadata=None)
    filenames.append(new_dir + "/img"+"_"+labels[k]+".png")


images = []
for i in filenames:
    images.append(imageio.imread(i))
    

imageio.mimwrite(new_dir + '/MAP_Robox2D.gif', images, fps = 3)
