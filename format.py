with open('20k') as f:
    content = f.readlines()
content=[x.strip() for x in content]
for k in range(len(content)):
    p=k*5
    open_string =str(p)+".{:<20} "+str(p+1)+".{:<20} "+str(p+2)+".{:<20} "+str(p+3)+".{:<20} "+str(p+4)+".{:<20}"
    #print open_string
    print(open_string.format(content[p],content[p+1],content[p+2],content[p+3],content[p+4]))
    #print(content[p],content[p+1],content[p+2])
    if p+2>19990:
        break





