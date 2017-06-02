with open('20k') as f:
    content = f.readlines()
content=[x.strip() for x in content]
for k in range(len(content)):
    p=k*5
    open_string =str(p)+".{:<17} "+str(p+1)+".{:<17} "+str(p+2)+".{:<17} "+str(p+3)+".{:<17} "
    #print open_string
    print(open_string.format(content[p],content[p+1],content[p+2],content[p+3]))
    #print(content[p],content[p+1],content[p+2])
    if p==19995:
        break





