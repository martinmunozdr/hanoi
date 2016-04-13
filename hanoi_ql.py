import random
import time

torre1 = [4,1,0,0]
torre2 = [2,0,0,0]
torre3 = [3,0,0,0]

q = []
for i in range(16*16*16*6):
    q.append(0)


def indice_estado_torre(torre):
    if torre[0]==4 and torre[1]==3 and torre[2]==0:
        return 0

    if torre[0]==4 and torre[1]==2 and torre[2]==0:
        return 1

    if torre[0]==4 and torre[1]==1 and torre[2]==0:
        return 2

    if torre[0]==3 and torre[1]==2 and torre[2]==0:
        return 3

    if torre[0]==3 and torre[1]==1 and torre[2]==0:
        return 4

    if torre[0]==2 and torre[1]==1 and torre[2]==0:
        return 5

    if torre[0]==4 and torre[1]==0:
        return 6

    if torre[0]==3 and torre[1]==0:
        return 7

    if torre[0]==2 and torre[1]==0:
        return 8

    if torre[0]==1 and torre[1]==0:
        return 9

    if torre[0]==4 and torre[1]==3 and torre[2]==2 and torre[3]==0:
        return 10

    if torre[0]==4 and torre[1]==3 and torre[2]==2 and torre[3]==1:
        return 11

    if torre[0]==4 and torre[1]==2 and torre[2]==1 and torre[3]==0:
        return 12

    if torre[0]==3 and torre[1]==2 and torre[2]==1 and torre[3]==0:
        return 13

    if torre[0]==0:
        return 14

    if torre[0]==4 and torre[1]==3 and torre[2]==1 and torre[3]==0:
        return 15

    return "ERROR GRAVE"

def indice_accion(org, dst):
    if org==1 and dst==2:
        return 0

    if org==2 and dst==1:
        return 1

    if org==1 and dst==3:
        return 2

    if org==3 and dst==1:
        return 3

    if org==3 and dst==2:
        return 4

    if org==2 and dst==3:
        return 5

    return "ERROR GRAVE"

def accion_de_indice(i):
    if i==0:
        return 1,2

    if i==1:
        return 2,1

    if i==2:
        return 1,3

    if i==3:
        return 3,1

    if i==4:
        return 3,2

    if i==5:
        return 2,3

    return "ERROR_GRAVE"
  
def dibujar_torres():
     print "-----------TORRES--------------"
     
     i=3
     while(i>=0):
         print " "
         for j in range(torre1[i]):
             print torre1[i],
         i -= 1
     print " "
     
     print "----------------------------------"

     i=3
     while(i>=0):
         print " "
         for j in range(torre2[i]):
             print torre2[i],
         i -= 1
     print " "
     
     print "----------------------------------"

     i=3
     while(i>=0):
         print " "
         for j in range(torre3[i]):
             print torre3[i],
         i -= 1
     
     print " "
     print "----------------------------------"

 
def obtener_mayor_indice(torre, k):
     i=3
     while(i>=0):
         if torre[k][i]!=0:
             return i
         i -= 1
     
     return -1  #torre vacia

 
def obtener_menor_vacio(torre, k):
     for i in range(4):
         if torre[k][i]==0:
             return i
     
     return -1  #torre llena

 
def reinicializar_torres():
     torre1[0]=4
     torre1[1]=1
     torre1[2]=0
     torre1[3]=0
     
     torre2[0]=2
     torre2[1]=0
     torre2[2]=0
     torre2[3]=0
       
     torre3[0]=3
     torre3[1]=0
     torre3[2]=0
     torre3[3]=0     

def reiniciar_aleatorio():
    mistorres = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    indice_toca = [0,0,0]

    for i in range(4):
        torre_llenar = random.randint(0,2) #del 0 al 2 incluyendo estos
        disco = 4-i #de 4 a 1

        while True:
            if indice_toca[torre_llenar]==3: 
                torre_llenar += 1
                if torre_llenar>2:
                    torre_llenar = 0
            else:
                mistorres[torre_llenar][indice_toca[torre_llenar]] = disco
                indice_toca[torre_llenar] += 1
                break
     
    for k in range(4):
         torre1[k] = mistorres[0][k]
         torre2[k] = mistorres[1][k]
         torre3[k] = mistorres[2][k]
        
  
def mover(origen, destino, dibujar):
     mistorres = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
     
     for k in range(4):
         mistorres[0][k] = torre1[k]
         mistorres[1][k] = torre2[k]
         mistorres[2][k] = torre3[k]
     
     if origen==destino:
         return "ERROR"


     i_mayor = obtener_mayor_indice(mistorres,origen-1)
     if i_mayor<0:
         return "ERROR"
         
     valor_arriba = mistorres[origen-1][i_mayor]
         
     mayor_vacio = obtener_menor_vacio(mistorres,destino-1)
     if mayor_vacio<0:
         return "ERROR"
         

     if mayor_vacio!=0 and mistorres[origen-1][i_mayor]> \
        mistorres[destino-1][mayor_vacio-1]:
         return "ERROR"
         

     mistorres[origen-1][i_mayor] = 0
     mistorres[destino-1][mayor_vacio] = valor_arriba
         
     
     for k in range(4):
         torre1[k] = mistorres[0][k]
         torre2[k] = mistorres[1][k]
         torre3[k] = mistorres[2][k]
     
     if dibujar:
         dibujar_torres()
     
     if torre1[0]==4 and torre1[1]==3 and torre1[2]==2 and torre1[3]==1:
         reiniciar_aleatorio()
         if dibujar:
             time.sleep(1)
             dibujar_torres()
         return "FIN"

     if torre2[0]==4 and torre2[1]==3 and torre2[2]==2 and torre2[3]==1:
         reiniciar_aleatorio()
         if dibujar:
             time.sleep(1)
             dibujar_torres()
         return "FIN"

     if torre3[0]==4 and torre3[1]==3 and torre3[2]==2 and torre3[3]==1:
         reiniciar_aleatorio()
         if dibujar:
             time.sleep(1)
             dibujar_torres()
         return "FIN"
     
     return "VALIDO"

def seleccionar_acc(q_acs):
    indices_iguales = []

    maximo = q_acs[0]
    #i_max = 0
    for i in range(1,6):
        if q_acs[i] > maximo:
            maximo = q_acs[i]
            #i_max = i

    for i in range(6):
        if q_acs[i] == maximo:
            indices_iguales.append(i)

    if len(indices_iguales) == 1:
        return indices_iguales[0]

    return indices_iguales[random.randint(0,len(indices_iguales)-1)]

def q_learning():
    dibujar = False
    q_acs = []

    indice_grande = indice_estado_torre(torre1)*16*16*6 + \
      indice_estado_torre(torre2)*16*6 + indice_estado_torre(torre3)*6
    for i in range(6):
        q_acs.append(q[indice_grande + i])

    indice_acc = seleccionar_acc(q_acs)
    acc = accion_de_indice(indice_acc)

    #print acc
    contador = 0
    while True:
        rpta = mover(acc[0],acc[1], dibujar)

        #print rpta
        r=0
        if rpta == "ERROR":
            r = -10000
        elif rpta == "VALIDO":
            r = -1
        else:
            r = 100

        sig_indice_grande = indice_estado_torre(torre1)*16*16*6 + \
             indice_estado_torre(torre2)*16*6 + indice_estado_torre(torre3)*6
        sig_q_acs = []
        for i in range(6):
            sig_q_acs.append(q[sig_indice_grande + i])

        sig_indice_acc = seleccionar_acc(sig_q_acs)
        sig_acc = accion_de_indice(sig_indice_acc)

        q[indice_grande + indice_acc] = r + \
              0.9*q[sig_indice_grande + sig_indice_acc]

        acc = sig_acc
        indice_grande = sig_indice_grande
        indice_acc = sig_indice_acc

        #print acc

        if contador>50000:
            dibujar = True
            time.sleep(1)

        contador += 1

q_learning()
