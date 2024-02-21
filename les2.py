import random
import string

# generate randon number of dictionaries
num_dicts = random.randint(2, 10)
list_of_dicts = []

# generate each dictionary
for i in range(num_dicts):
    # generate random values
    num_keys = random.randint(1, 10)
    new_dict = {}
    # generate random keys and values
    for k in range(num_keys):
        key = random.choice(string.ascii_lowercase) # random letter
        value = random.randint(0, 100) # random number [0,100]
        new_dict[key] = value
    list_of_dicts.append(new_dict)

#print(list_of_dicts)
result_dict={}

# add first dictionary from list to result dictionary as is
for k, v in list_of_dicts[0].items():
    result_dict[k] = v

# iterate list of dictionaries starting from second dict in list
for i, d in enumerate(list_of_dicts[1:], 2):
    for k, v in d.items():
        new_key = f"{k}_{i}"  # add prefix to key with max value
        if k in result_dict:#if key is already in result dict
            if v > result_dict[k]: #and value this key > key in result dict
                result_dict[k] = v  #then assign bigger value to this key
                result_dict[new_key] = v #write key with prefix to result dict
        else:
            result_dict[k] = v #otherwise just add new pair to result dict

print(result_dict)




