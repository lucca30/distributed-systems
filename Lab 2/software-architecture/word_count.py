

def user_layer(processing_call, data_access_call):
    file_name = input("Enter the file name:")
    print(processing_call(file_name, data_access_call))

def processing_layer(file_name, data_access_call):
    import re
    from collections import defaultdict

    data = data_access_call(file_name)
    rgx = re.compile("([\w][\w']*\w)")
    words = rgx.findall(data)
    
    word_count = {}
    word_count = defaultdict(lambda:0,word_count)
    
    for word in words:
        word_count[word] += 1
    
    occurrences_and_words = [(word_count[x], x) for x in word_count.keys()]

    occurrences_and_words.sort(reverse=True)
    top_words = occurrences_and_words[0:10]

    response = "Top words:\n\n"
    response += "\n".join([ ( x[1].ljust(10) + " -> " + str(x[0]).ljust(3) + " occurrences") for x in top_words])
    return response



def data_access_layer(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data


user_layer(processing_layer, data_access_layer)