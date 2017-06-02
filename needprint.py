with open('20k') as f:
    content = f.readlines()
content=[x.strip() for x in content]
for k in range(len(content)):
    p=k*3
    open_string =str(p)+".{:<17} "+str(p+1)+".{:<17} "+str(p+2)+".{:<17} "
    #print open_string
    print(open_string.format(content[p],content[p+1],content[p+2]))
    #print(content[p],content[p+1],content[p+2])
    if p>19993:
        break





