def find_last(str, s):
    index = str.find(s)
    while str.find(s,index+1) >= 0:
        if str[index:] == '':
            break
        index += str.find(s,index+1) + 1
    return index
    
# find Method
    
def find_last(str, s)
	last_pos = -1
	while True:
		pos = str.find(s, last_pos + 1)
		if pos == -1:
			return last_post
		last_pos = pos