import numpy as np
import csv
import pandas as pd

text_file = open("wea.txt","w")
results = []
with open('primeros-parametros.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

print("param fab := 50;\nparam dep := 100;\nparam cli := 200;",file=text_file)

results2 = []
with open("demandas.txt", "r") as ins:
    reader = csv.reader(ins, delimiter=",")
    for row in reader:
        results2.append(row)
    results2 = results2[0]

print("param dem := ",end="",file=text_file)
#print("%d %s" % (1,results2[0]),end="\t")
for i in range(0,len(results2)):
    if(i!=len(results2)-1):
        print("%d %s" % (i+1,results2[i]),end="\t",file=text_file)
    else:
        print("%d %s" % (i+1,results2[i]),end="",file=text_file)
print(";",file=text_file)

results3 = pd.read_csv("capacidades-costo-fabricas.txt",header=None)
x,y = results3.shape
results3 = np.array(results3)

print("param fCOST := ",end="",file=text_file)
for i in range(0,x):
    if(i!=x-1):
        print("%d %s" % (i+1,results3[i][0]),end="\t",file=text_file)
    else:
        print("%d %s" % (i+1,results3[i][0]),end="",file=text_file)

print(";",file=text_file)

print("param fCOP := ",end="",file=text_file)
for i in range(0,x):
    if(i!=x-1):
        print("%d %s" % (i+1,results3[i][1]),end="\t",file=text_file)
    else:
        print("%d %s" % (i+1,results3[i][1]),end="",file=text_file)
print(";",file=text_file)

results3 = pd.read_csv("capacidades-costo-depositos.txt",header=None)
x,y = results3.shape
results3 = np.array(results3)

print("param dCOST := ",end="",file=text_file)
for i in range(0,x):
    if(i!=x-1):
        print("%d %s" % (i+1,results3[i][0]),end="\t",file=text_file)
    else:
        print("%d %s" % (i+1,results3[i][0]),end="",file=text_file)

print(";",file=text_file)

print("param dCOP := ",end="",file=text_file)
for i in range(0,x):
    if(i!=x-1):
        print("%d %s" % (i+1,results3[i][1]),end="\t",file=text_file)
    else:
        print("%d %s" % (i+1,results3[i][1]),end="",file=text_file)
print(";",file=text_file)

results3 = pd.read_csv("costo-deposito-cliente.txt",header=None, delimiter="\n")
results3 = np.array(results3)
x,y = results3.shape

matriz = []

for i in range(0,x):
    matriz.append(results3[i][0].split(","))



print("param cDC : ",end="",file=text_file)
for i in range(0,x):
    if(i!=x-1):
        print("%d" % (i+1),end="\t",file=text_file)
print(":=",file=text_file)
for i in range(0,x):
    print("%d" % (i+1),end="\t",file=text_file)
    for j in range(0,y):
        print("%s" % matriz[i][j], end="\t",file=text_file)
    print("\n",file=text_file)
print(";",file=text_file)



#print("param cDC := ",end="",file=text_file)
#for i in range(0,x):
#    for j in range(0,y):
#        if(i!=x-1):
#            print("%d %s" % (i+1,results3[i][j]),end="\t",file=text_file)
#        else:
#            print("%d %s" % (i+1,results3[i][j]),end="",file=text_file)
#print(";",file=text_file)


