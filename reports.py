
# Report functions
def count_games(file_name):  
    # file = open(file_name)  
    with open (file_name, 'r') as reader: 
        count = 0
        for line in reader.readlines():  
            count +=1  
    return count 
    


def decide(file_name, year): 
    result = False  
    file = open(file_name)  
    try:
        for line in file: 
            fields = line.split('\t')   
            if int(fields[2]) == year: 
                result = True  
    finally: 
        file.close()              
    return result
    


def get_latest(file_name): 
    result = '' 
    relase_date = 0
    file = open(file_name)
    try: 
        for line in file: 
            fields = line.split('\t')  
            if int(fields[2]) > relase_date: 
                relase_date = int(fields[2]) 
                result = fields[0] 
    finally: 
        file.close()   
    return result   


def count_by_genre (file_name, genre): 
    file = open(file_name)  
    count = 0 
    try:
        for line in file:  
            fields = line.split('\t')   
            if fields[3] == genre: 
                count +=1 
    finally: 
        file.close()   
    return count


def get_line_number_by_title(file_name, title): 
    file = open(file_name)  
    try: 
        for num, line in enumerate(file,1): 
            fields = line.split('\t') 
            if title == fields[0]: 
                return num
    finally: 
        file.close()
    raise ValueError