#SOLVER

option solver gurobi_ampl;
option gurobi_options 'outlev=1 mipgap 0.01 bestbound 1 logfile "./logfile.txt"'; 

#PARAMETROS

param cli;
param fab;
param dep;

#Costo asociado a cada fabrica
param fCOST{1 .. fab};

#Costo asociado a cada depositos
param dCOST{1 .. dep};

#Capacidad operacional de las fabricas
param fCOP {1 .. fab};

#Capacidad operacional de los depositos
param dCOP {1 .. dep};

#Demanda de los clientes
param dem{1 .. cli};

#Costo de transporte (por 1 unidad) desde la fabrica a un deposito
param cFD{1 .. fab, 1 .. dep};

#Costo de transporte (por 1 unidad) desde el deposito a un cliente
param cDC{1 .. dep, 1 .. cli};


#VARIABLES

#arreglo de tamaño = la cantidad de fabricas, donde cada una esta abierta o cerrada (1-0)
var x {1 .. fab} integer >=0 <=1;

#arreglo de tamaño = la cantidad de depositos, donde cada uno esta abierta o cerrada (1-0)
var y {1 .. dep} integer >=0 <=1;

#Cantidad de productos de transportados desde la fabrica a un deposito(Xij)
var canFD{1 .. fab, 1 .. dep} >=0;

#Cantidad de productos de transportados desde el deposito a un cliente (Sjk)
var canDC{1 .. dep, 1 .. cli}  >=0 ;

#FUNCION OBJETIVO

minimize Total_Cost: ((sum { i in 1..fab } x[i] * fCOST[i])) + ((sum { j in 1..dep } y[j] * dCOST[j]))  + ((sum { i in 1..fab } (sum { j in 1..dep } cFD[i,j] * canFD[i,j])))  +  ((sum { j in 1..dep } (sum { k in 1..cli } cDC[j,k]*canDC[j,k] ) )) ;

#RESTRICCIONES

s.t.
#Los productos transportados por cada deposito debe ser mayor o igual a la demanda de cada cliente
    demand_capacity {k in 1..cli}:          sum{j in 1..dep} canDC[j,k] >= dem[k];

#La cantidad de productos transportados desde la planta al deposito deben ser mayor a los productos transportados desde el deposito a los clientes
    transport_capacity {j in 1..dep}:       sum{i in 1..fab} canFD[i,j] >= sum{k in 1..cli} canDC[j,k];

#La capacidad operacional de las fabricas abiertas debe ser mayor a la cantidad de productos transportados
    operational_capacity1{i in 1..fab}:   sum{j in 1..dep}canFD[i,j] <= x[i]*fCOP[i];

#La capacidad operacional de los depositos abiertos debe ser mayor a la cantidad de productos transportados
    operational_capacity2 {j in 1 .. dep}:   sum{k in 1 .. cli} canDC[j,k] <= y[j]*dCOP[j];
