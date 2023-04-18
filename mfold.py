import os

path_of_the_directory= input('enter files directory: ')
path_of_the_directory += '\\'
name_list = ''
energy_list = ''
sec_energy = ''
base_number = ''

for filename in os.listdir(path_of_the_directory):
#    ext = (".txt")
    if filename.endswith(".txt"):
        z = path_of_the_directory + filename
        file = open(z, 'r')
        file_list = file.readlines()
# file= open('C:\\Users\\Mostafa Zaki\\Desktop\\2022_18_9\\str1.txt', 'r')

        file.close()
    counter = 1

    for n in file_list:
        if counter == 1:
            if (len(name_list) <1):
                name_list += n.replace('\n','')
            else:
                name_list += ',' + n.replace('\n','')
        if counter == 3:
            if (len(energy_list) <1) or (energy_list[-1] == '/'):
                energy_list += n[6:].replace('\n','')
            else:
                energy_list += ',' + n[6:].replace('\n','')

        if n[0:5] == "Helix":
            if (len(sec_energy) <1) or (sec_energy[-1] == '/'):
                sec_energy += n[6:12].replace('\t','')
            else:
                sec_energy += ',' + n[6:12].replace('\t', '')
            if (len(base_number) < 1) or (base_number[-1] == '/'):
                m= n[12:16].replace('\t', "")
                m= m.replace('b', '')
                m= m.replace('a','')
                base_number += m
            else:
                m = ',' + n[12:16].replace('\t', "")
                m = m.replace('b', '')
                m = m.replace('a', '')
                base_number += m

        counter += 1
    name_list += '/'
    sec_energy += '/'
    base_number += '/'

print(name_list)
print(energy_list)
print(sec_energy)
print(type(sec_energy))
base_number = base_number.replace(' ', '')
print(base_number)
print(type(base_number))



