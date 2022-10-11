import numpy as np
# import tensorflow as tf
import tensorflow.keras as keras
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
# mport tensorflow as tf
from tensorflow.python.client import device_lib
# tf.__version__
# tf.config.list_physical_devices('GPU')
def getGpuName():
    local_device_protos = device_lib.list_local_devices()
    return[x.name for x in local_device_protos if x.device_type =='GPU']

local_device_protos = device_lib.list_local_devices()
# for x in local_device_protos:
#     if x.device_type=='GPU':
#         print(x.name[1:])
# print(getGpuName())

# local_device_protos = device_lib.list_local_devices()
# for x in local_device_protos:
#     if x.device_type=='GPU':
#         print(x.name.find('NVIDIA'))

# aModel= keras.Sequential([
#     keras.Input(28*28),
#     keras.layers.Dense(200, activation= 'relu'),    
#     keras.layers.Dense(10,  activation= 'softmax')
#     ])

# aModel.compile(
#     loss=     'sparse_categorical_crossentropy',
#     metrics= ['accuracy']
#     )
# aModel.summary()

# keras.utils.plot_model(aModel,
#     to_file="model2.png", 
#     show_shapes= True, 
#     show_layer_activations= True)

