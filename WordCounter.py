line = open(r'D:\\python\\note.txt',"r")
x=line.readline()
z=x.split()
List=[]
list=['0']
for word in z:
    List.append(word)
#print(List)
i=0
#print(leng)
find=List[0]
next=List[2]
cnt=0
for find in List:
    for next in List:
            i=i+1
            if List.index(find)==List.index(next):
                cnt=cnt+1
            else:
                continue
    if List.index(find)!=list:
        print("word=", find, " ", cnt)
        List.remove(next)
    list.append(find)

    cnt = 0

