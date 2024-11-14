from .node_class import Node

LOGGGING = False
MEMORY_LOGGING = True

#---------------------------------- Алогритм Хаффмана ----------------------------------#
def get_freq_dict(input:str):
    freq_dict={}

    for character in input:
        if not freq_dict.__contains__(character):
            freq_dict[character] = 1
        else:
            freq_dict[character] += 1

    return sort_dict_by_value(freq_dict)

def build_huffman_tree(freq_dict:dict): 
    if len(freq_dict.keys()) > 1:
        keys = list(freq_dict.keys())
        first_key, second_key = keys[0], keys[1]

        tree_node = Node(first_key, second_key, freq_dict[first_key], freq_dict[second_key])
        freq_dict.pop(first_key), freq_dict.pop(second_key), 

        combined_freq = tree_node.freq

        freq_dict.update({tree_node  : combined_freq})
        freq_dict = sort_dict_by_value(freq_dict)
        
        return build_huffman_tree(freq_dict)
    
    return freq_dict

def get_elements_codes(parent_node:Node, code='',): 
    if type(parent_node) is str:
        return{parent_node:code}
    
    left_child, right_child = parent_node.left_node, parent_node.right_node
    codes_dict = dict()
    codes_dict.update(get_elements_codes(left_child, code + '0'))
    codes_dict.update(get_elements_codes(right_child, code + '1'))
    return codes_dict

def get_codes_dict(input):
    dict = get_freq_dict(input)
    tree = build_huffman_tree(dict)
    res = get_elements_codes(next(iter(tree)))

    log(res, 'get_codes_dict')

    return res

def extract_freq_dict(encrypted_str:str):
    res = dict()
    current =''
    index = 0

    for char in encrypted_str:
        if(char != '/'):
            current += char
            index += 1
        else:
            res.update({current.split('&')[0] : current.split('&')[1] })  
            if encrypted_str[index+1] == '0' or encrypted_str[index+1] == '1':
                break
            else:
                current =''
                index +=1


    log(res, 'extract_freq_dict')
    log(encrypted_str[index+1:], 'extract_freq_dict')

    return res, encrypted_str[index+1:]

def read_encrypted_str(codes_dict:dict, encrypted_str):
    result = ''
    current_susbtr = ''
    codes = list(codes_dict.values())

    for char in encrypted_str:
        current_susbtr += char
        if codes.__contains__(current_susbtr):
            result += list(codes_dict.keys())[list(codes_dict.values()).index(current_susbtr)]
            current_susbtr = ''

    log(result, 'read_encrypted_str')
    return result


#---------------------------------- Функции кодировани и декодирования ----------------------------------#

def decrypt_data(encrypted_str):
    codes_dict, clear_str = extract_freq_dict(encrypted_str)
    return read_encrypted_str(codes_dict, clear_str)

def encrypt_data(input):
    log(input, 'encrypt_data')
    codes_dict = get_codes_dict(input)
    result_str = ''

    for k,v in codes_dict.items():
        result_str += f'{k}&{v}/'

    for char in input:
        result_str += codes_dict[char]

    log(result_str, 'encrypt_data')

    memory_difference(input,codes_dict)

    return result_str

#---------------------------------- Вспомогательные функции ----------------------------------#

def log(item, method_name):
    if(LOGGGING):
        print(f'LOGGING FROM {method_name} : {item} \n')

def sort_dict_by_value(dictionary:dict):
    dictionary = dict(sorted(dictionary.items(), key=lambda x:x[1]))
    return dictionary

def memory_difference(the_data, codes_dict:dict):
    if(MEMORY_LOGGING):  
        beforeCompression = len(the_data) * 8  
        afterCompression = 0  
        the_symbols = codes_dict.keys()  

        for symbol in the_symbols:  
            the_count = the_data.count(symbol)  
            afterCompression += the_count * len(codes_dict[symbol])  
            
        print(f'Использовано места до сжатия: {beforeCompression} бит')  
        print(f'Использовано места после сжатия: {afterCompression} бит')  
