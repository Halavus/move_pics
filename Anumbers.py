art = open('Anb.txt', 'rb')
l = list(art)                  

def replace(lst):
    counter = 0
    for i in lst:                    
        lst[counter]=i.replace('\n','')
        counter+=1

replace(l)
