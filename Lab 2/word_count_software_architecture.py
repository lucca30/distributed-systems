from shared_layers import processing_layer, data_access_layer

def user_layer(processing_call, data_access_call):
    file_name = input("Enter the file name:")
    print(processing_call(file_name, data_access_call))


user_layer(processing_layer, data_access_layer)