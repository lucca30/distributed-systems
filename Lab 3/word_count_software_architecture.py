from shared_layers import processing_layer, data_access_layer

# I'll pass the data_access_call as a kind of dependency injection to allow decoupled layers
def user_layer(processing_call, data_access_call):
    file_name = input("Enter the file name:")
    word = input("Enter the word to be counted:")
    print(processing_call(file_name, word,data_access_call))


user_layer(processing_layer, data_access_layer)