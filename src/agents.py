import numpy as np


def functional_NN(x, NN_params, sizes, bias=True):
    y = x.copy() 
    ind = 0
    if bias:
        for i in range(len(sizes)-2):
            # select weights and biases of this layer
            ind_new = ind+(sizes[i] * sizes[i+1])
            w = NN_params[ ind : ind_new].reshape((sizes[i], sizes[i+1]))
            ind = ind_new
            ind_new += sizes[i+1]
            b = NN_params[ ind : ind_new].reshape((1, sizes[i+1]))
            ind = ind_new

            # perform forward pass
            y = np.matmul( y, w ) + b
            y = 1.0 / (1.0 + np.exp(-y))
        
        ind_new = ind+(sizes[-2] * sizes[-1])
        w = NN_params[ ind : ind_new].reshape((sizes[-2], sizes[-1]))
        ind = ind_new
        ind_new += sizes[-1]
        b = NN_params[ ind : ind_new].reshape((1, sizes[-1]))
        ind = ind_new
        y = np.matmul( y, w ) + b
        y = np.tanh(y)
    return y

def random_NN(sizes, bias=True):
    size = 0        
    if bias:
        for i in range(len(sizes)-1):
            size += (sizes[i] +1) * sizes[i+1]
    else:
        for i in range(len(sizes)-1):
            size += sizes[i] * sizes[i+1]
    
    return np.random.uniform(low=-1, high=1, size=size)

class NNAgent():
    # initialization calculates the indeces to use when forward passing. The weights and biases are not actually stored, only passed as a parameter
    def __init__(self, layer_sizes, bias=True):
        self.NN = [] 
        ind = 0
        if bias:
            for i in range(len(layer_sizes)-1):
                ind_new = ind+(layer_sizes[i] * layer_sizes[i+1])
                w = {"start": ind, "end": ind_new, "shape": (layer_sizes[i], layer_sizes[i+1])}
                ind = ind_new
                ind_new += layer_sizes[i+1]
                b = {"start": ind, "end": ind_new, "shape": (1, layer_sizes[i+1])}
                ind = ind_new

                self.NN.append( [w, b] ) 
        else:
            raise(NotImplementedError)

    def size(self,sizes):
        size = 0        
        for i in range(len(sizes)-1):
            size += (sizes[i] +1) * sizes[i+1]

        return size 

    def forward_pass(self, x, data):
        y = x
        # use sigmoid for activation for all layers except for last one in which we use tanh
        for (w,b) in self.NN[:-1]:
            y = np.matmul(y, data[w['start']: w['end']].reshape(w['shape'])) + data[ b['start']: b['end']].reshape(b['shape'])
        y = np.matmul(y, data[ self.NN[-1][0]['start']: self.NN[-1][0]['end']].reshape(self.NN[-1][0]['shape'])) + data[ self.NN[-1][1]['start']: self.NN[-1][1]['end']].reshape(self.NN[-1][1]['shape'])
        y = np.tanh( y )
        return y
    
    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-x))
    
    def get_genotype(self):
        return self.data.view()



class DMPAgent():
    def __init__(self, data, sizes):
        pass