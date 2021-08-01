
def processing_layer(file_name, word,data_access_call):
    import re
    from collections import defaultdict

    # calling dependency to access data (probably the function implemented below)
    data = data_access_call(file_name)
    if(data == "Failed to access the data"):
        return "Failed to access the data. No existing file"
    rgx = re.compile("([\w][\w']*\w)")
    words = [w.lower() for w in rgx.findall(data)]

    response = "\t" + word + " -> " + str(words.count(word.lower())) + " occurrences" 
    return response



def data_access_layer(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
    except:
        data = "Failed to access the data"
    return data
