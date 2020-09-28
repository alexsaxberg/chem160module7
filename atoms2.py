names=["H", "He", "Li", "Be"]
masses=[1.088,4.033,6.941,9.012]
Dict2={}
for i in range(len(names)):
    Dict2[names[i]]=masses[i]
print(Dict2)
print(Dict2["He"])
print("O" in Dict2)
