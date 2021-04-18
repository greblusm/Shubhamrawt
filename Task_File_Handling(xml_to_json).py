import xml.etree.ElementTree as ET    
tree = ET.parse("C:\\users\\Shubham Rawat\\Desktop\\xmlfile.xml")  #parsing the file
root = tree.getroot()

for child in root:   
    print(child.tag)  #return the two nodes of the parent tree

for n in root.findall('{http://s3.amazonaws.com/doc/2006-03-01/}Buckets'):
    print(n[2])   #return the memory location of the 2nd child of the buckets  

for child in root:
    print(child.tag)  #return the two nodes of the parent tree
        



#extracting name and creation dates and storing these in a different list 
list1=[]        # creating two empty list   
list2=[]
for child in root:  #geeting each and every node of the tree whether its a parent, nodes or subnodes 
    if(child.tag == '{http://s3.amazonaws.com/doc/2006-03-01/}Buckets'):  #condition for checking buckets node of the tree
        for attr in child: #getting every subnodes(Bucket) of node(Buckets)
            dir(attr)
            list1.append(attr[0].text)  #returning text inside subnodes(name) of bucket and appending it to a list 1
            list2.append(attr[1].text)  #returning text inside subnode(creation date) of bucket and appending it to a list 2
print(list1) #printing list 1 holding all name data
print(list2) #printing list 1 holding all creation date data




#printing and writing the bucket name start with t6 into a file
f = open('C:\\users\\Shubham Rawat\\Desktop\\sample1.txt','w+') #creating a txt file name as sample1 in a read and write mode
f.write("the bucket name start with 't6' : \n")  #write inside the file
for num in list1: #returning every element in a list 1
    if(num[0:2] == 't6'):  #condition for element in a list 1 starts with t6
        print(num)         #printing the name starts with t6
        f.write(f'{num} \n') #writing the name starts with t6 inside the file




#printing and writing data by using dictionary into the file created above
dict1 = dict(zip(list1,list2)) #ziping the object of the two list by similar index (iterator of tuples)  
print(dict1) #printing created dictionary
#f = open('C:\\users\\Shubham Rawat\\Desktop\\sample1.txt','w+')  #if file is already created and opened above then it is not necessary otherwise a file with read and write mode created and open
f.write('\n "Printing by using dictionary" \n\n')
f.write('Bucket name:                              Creation date: \n') #writing inside the same file opened above
for v,k in dict1.items(): # returning every single values and keys inside dictionary(dict1)
    f.write(f'{v:20}-----    {k} \n')   #writing in a file
    



#printing and writing data by using list into the file created above
f.write('\n "Printing by using list" \n\n')    
f.write('Bucket name:                              Creation date:\n\n')
for i in range(len(list1)):
    print('{}                {}\n'.format(list1[i],list2[i])) #printing in a console
    f.write('{}                {}\n'.format(list1[i],list2[i])) #writing output in a file opened above

f.close()  #closing the file



#printing data by using list in a list form
#f.write('\n printing by using list in a list form \n')  
for i in range(len(list1)):
    list3 = [list1[i],list2[i]]
    print(list3)
    #f.write(list3)   #type error write() argument must be str, not list

#creating a txt file and storing data as json
import json
dict1
app_json = json.dumps(dict1)
print(app_json)

#creating a json file and storing above extracted data into a json file
import json
dict1
with open('person.json', 'w') as json_file:
  json.dump(dict1, json_file)
