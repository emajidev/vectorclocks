#Declaracion de veriables
inc=0
#Funciones

#Comparacion de valor maximo entre vectores
def vector_compare(vector1,vector2):
    vector = [max(value) for value in zip(vector1,vector2)]
    return vector
#carreo de estado
def carreo_estado_1(resvNro,np):
    for i in range(resvNro,np):
        pros[0][i][1] = pros[0][i-1][1]
        pros[0][i][2] = pros[0][i-1][2]
def carreo_estado_2(resvNro,np):
    for i in range(resvNro,np):
        pros[1][i][0] = pros[1][i-1][0]
        pros[1][i][2] = pros[1][i-1][2]
def carreo_estado_3(resvNro,np):
    for i in range(resvNro,np):
        pros[2][i][0] = pros[2][i-1][0]
        pros[2][i][1] = pros[2][i-1][1]

#Menu de seleccion
np1 = int(raw_input("ingresa el Nro nodos del proceso p1: "))
np2 = int(raw_input("ingresa el Nro nodos del proceso p2: "))
np3 = int(raw_input("ingresa el Nro nodos del proceso p3: "))
nlcom = int(raw_input("ingresa el Nro lineas de comunicacion:"))

#procesos 
#todos los vectores inicializan en cero
class p1:
    vp=[]
    for i in range(np1):
        n = i+1
        vn = [n,0,0] 
        vp.append(vn)  
    node = vp
class p2:
    vp=[]
    for i in range(np2):
        n = i+1
        vn = [0,n,0]
        vp.append(vn)  
    node = vp
class p3:
    vp=[]
    for i in range(np3):
        n = i+1
        vn = [0,0,n]
        vp.append(vn)
    node = vp
p1 = p1()
p2 = p2()

# objeto de procesos
pros = [
    p1.node,
    p2.node,
    p3.node
]
while inc < nlcom:
    send = int(raw_input("ingresa el Nro proceso a enviar: "))
    resv = int(raw_input("ingresa el Nro proceso a recibir: "))
    send_Nro = int(raw_input("ingresa el Nro evento a enviar: "))
    resv_Nro = int(raw_input("ingresa el Nro evento a recibir: "))
    if send <=3 and resv <=3:
        print ("P{} --> P{}".format(send,resv))
        vector_send = pros[send-1][send_Nro-1]
        vector_resv = pros[resv-1][resv_Nro-1]
        #Envio de msg
        new_vector = vector_compare(vector_send,vector_resv)
        #Llamada de funcion para carreo de estado
        pros[resv-1][resv_Nro-1] = new_vector  
        if resv == 1:
            carreo_estado_1(resv_Nro,np1) 
        if resv == 2:
            carreo_estado_2(resv_Nro,np2) 
        if resv == 3:
            carreo_estado_3(resv_Nro,np2) 
    inc += 1
# Impresion de vector clock
for i in range(3):
    print("p{}".format(i+1),pros[i])
