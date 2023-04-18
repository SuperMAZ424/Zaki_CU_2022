
# a program to identify RE in a seq. specially EcoRI, XbaI, SpeI, PstI
# identify variables (RE, pref, suf & scars)
# preffix: first with ATG , second without ATG
pref = ['GAATTCGCGGCCGCTTCTAG', 'GAATTCGCGGCCGCTTCTAGAG']
suf = 'TACTAGTAGCGGCCGCTGCAG'
EcoRI = 'GAATTC'
NotI = 'GCGGCCGC'
XbaI = 'TCTAGA'
SpeI = 'ACTAGT'
PstI = 'CTGCAG'
enzymelist = [EcoRI, NotI, XbaI, SpeI, PstI]
scar1 = 'TACTAGAG'
scar2 = 'TACTAG'
enzymechicker = False
suffixexist = False
preffixexist = False
seq = input('Enter seq:')

# identify wheither the prefix exist or not
if pref[0] in seq:
    print('pref is ok')
    preffixexist = True
elif pref[1] in seq:
    print('pref is ok')
    preffixexist = True

# tells you that you need to insert preffix
if preffixexist is False:
    print('you need to insert RFC [10] prefix before the sequence')

# identify wheither the suffix exist or not
if suf in seq:
    print('suffix is ok ')
    suffixexist = True

# tells you that you need to insert the suffix
if suffixexist is False:
    print('you need to insert RFC [10] suffix after the sequence')

# search for the enzymes
for x in range(len(enzymelist)):
    if suffixexist is True and preffixexist is True:
        if enzymelist[x] in seq[len(pref[0]):(- len(suf))]:
            print('insert contains incompatible restriction enzyme')
            enzymechicker = True
            break
    if suffixexist is False and preffixexist is False:
        if enzymelist[x] in seq:
            print('insert contains incompatible restriction enzyme')
            enzymechicker = True
            break
    if suffixexist is False and preffixexist is True:
        if enzymelist[x] in seq[len(pref[0]):]:
            print('insert contains incompatible restriction enzyme')
            enzymechicker = True
            break
    if suffixexist is True and preffixexist is False:
        if enzymelist[x] in seq[:-len(suf)]:
            print('insert contains incompatible restriction enzyme')
            enzymechicker = True
            break
# tells you if the sequence contains RFC[10] enzymes or not
if enzymechicker is False:
    print('seq is ok')
# tells you what to do if seq is RFC[10] incompatible
else:
    print('Your sequence contains one of RFC[10] preffix or suffix enzymes ')
    print('if you want to solve the problem remove the enzyme recognition site')
