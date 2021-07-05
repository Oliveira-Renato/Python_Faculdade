def copa(pais, *args):
    print('Pais: ', pais)
    for t in args:
        print('ano: ', t)
        
copa('Espanha', '2010')
print()

copa('Inglaterra', '1966')
print()

copa('Brasil', '1958', '1962', '1970', '1994', '2002')
print()