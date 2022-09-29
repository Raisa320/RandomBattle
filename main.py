import random
import time
###CONSTANTES DE COLORES
RED = '\033[31m'
GREEN = '\033[32m'
PURPLE = '\033[0;95m'
RESET = '\033[0m'
#COLORES CON NEGRITA
B_RED = "\033[1;31m"  # Red
B_GREEN = "\033[1;32m"  # Green
B_YELLOW = "\033[1;33m"  # Yellow
B_BLUE = "\033[1;34m"  # Blue
B_PURPLE = "\033[1;35m"  # Purple
B_CYAN = "\033[1;36m"  # Cyan
#COLORES CON SUBRAYADO
URED = "\033[4;31m"  # Red
UGREEN = "\033[4;32m"  # Green
UYELLOW = "\033[4;33m"  # Yellow
UBLUE = "\033[4;34m"  # Blue
#COLORES CON BACKGROUND
BG_CYAN = "\033[0;106m"  # Cyan
####FIN DE CONSTANTES#####

#######COMIENZO DEL PROGRAMA EN CONSOLA
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(B_YELLOW + "\t★★★★★" + GREEN + " Bienvenido a Random Battle" + RESET + B_YELLOW + " ★★★★★" + RESET)

########Variables#####
jugadores=[]
puntajesJugador1=[] #posicion 0 será puntaje inicial  
puntajesJugador2=[]
####fin variables#####

# Es importante dar instrucciones sobre cómo jugar:
print(GREEN + "=====================================================")
print("|| INDICACIONES:                                   ||")
print("|| 1. El jugador activo debera elegir un número    ||")
print("||    de maletin y ese maletin tendra cuanto se le ||")
print("||    restará de puntaje, puede ser 5 máx o 0 min  ||")
print("|| 2. El juego termina cuando alguien llegue a 0   ||")
print("=====================================================\n" + RESET)

#Ingreso de nicknames de jugadores
print(B_BLUE+"Jugador 1:"+RESET)
jugador1=input("\tIngrese su nickname: ").capitalize()
print(B_GREEN+"\nJugador 2:"+RESET)
jugador2=input("\tIngrese su nickname: ").capitalize()

#Agregar jugadores lista
jugadores.append(jugador1)
jugadores.append(jugador2)

#Puntaje ronda 0
puntajesJugador1.append(20)
puntajesJugador2.append(20)
###Puntos iniciales
print(B_YELLOW+"\n==============================================")
print("|| PUNTAJES INICIALES                       ||")
print("=============================================="+RESET)
print(B_BLUE+"\t -> "+jugador1+" inicia con: ",puntajesJugador1[0]," puntos"+RESET)
print(B_GREEN+"\t -> "+jugador2+" inicia con: ",puntajesJugador2[0]," puntos"+RESET)

##JUEGO
###Funciones###
def jugadorActivoUpdate(index):
  if(index==0):
    print(B_BLUE+"Jugador Activo: "+jugadores[index]+RESET)
    index+=1
  else:
    print(B_GREEN+"Jugador Activo: "+jugadores[index]+RESET)
    index-=1
  return index
  
def puntajesUpdate(jugador,puntajeRestado,ronda):
  juegoI=True
  if(jugador==0):
    puntaje=puntajesJugador1[ronda-1]-puntajeRestado
    puntajesJugador1.append(puntaje)
    if puntaje<=0:
      juegoI=False
  else:
    puntaje=puntajesJugador2[ronda-1]-puntajeRestado
    puntajesJugador2.append(puntaje)
    if puntaje<=0:
      juegoI=False
  
  print(B_YELLOW + "=========================================================")
  print("||", jugadores[jugador], "tu puntaje actual es de:", puntaje, "puntos ||")
  print("=========================================================\n" + RESET)
  return juegoI
    
def juegoPrincipal(jugadorActivo,ronda):
  print(B_YELLOW+"\t|1| \t |2| \t |3| \t |4| \t |5|"+RESET)
  valoresMaletin=[]
  for x in range(0,5):
    valor=random.randint(0,5)
    valoresMaletin.append(valor)
  eleccionUsuario=int(input("Elija una maletin [1-5]: "))
  while(eleccionUsuario<0 or eleccionUsuario>5):
    print(B_RED+"¡Por favor elija una opción en el rango indicado del 1 al 5!"+RESET)
    eleccionUsuario=int(input("Elija un maletin [1-5]: "))
  print(B_YELLOW+"*** Se abrirán los maletines *** "+RESET)
  for x in range(0,5):
    print("\tMaletin",(x+1),":",valoresMaletin[x],"puntos")
    time.sleep(1)
  
  print(B_RED+"*** Bueno "+jugadores[jugadorActivo]+" se te restarán:",valoresMaletin[eleccionUsuario-1],"puntos ***"+RESET)
  juego=puntajesUpdate(jugadorActivo,valoresMaletin[eleccionUsuario-1],ronda)
  return juego
  
##fin funciones###
while (True):
  ronda=len(puntajesJugador1)
  print(B_RED+"\n========= INICIO RONDA",ronda,"========="+RESET)
  jugadorActivo=random.randint(0,1)
  jugadorSiguiente=jugadorActivoUpdate(jugadorActivo) #imprime y modifica el jugador activo asi juega el otro jugador
  juegoP=juegoPrincipal(jugadorActivo,ronda)
  
  jugadorActivoUpdate(jugadorSiguiente)#Juega el siguiente jugador que no fue elegido al azar, así juega cada uno en una ronda
  juegoP=juegoPrincipal(jugadorSiguiente,ronda)
  if not juegoP:
    break
  print(B_CYAN+"Ningún jugador ha perdido, Pasamos a la siguiente ronda!"+RESET)

print(B_CYAN+"======RESUMEN DE RONDAS======="+RESET)
c=0
print(B_BLUE+"\t*** JUGADOR "+jugadores[0]+" ***"+RESET)
for jugadas in puntajesJugador1:
  print("\t\tRonda",c,": ",jugadas,"puntos")
  c+=1
c=0

print(B_GREEN+"\t*** JUGADOR "+jugadores[1]+" ***"+RESET)
for jugadas in puntajesJugador2:
  print("\t\tRonda",c,": ",jugadas)
  c+=1

if(len(puntajesJugador1)<len(puntajesJugador2)):
  print(B_YELLOW + "=====================================================")
  print("|| FELICIDADES", jugadores[0], "HAS GANADO!!!")
  print("======================================================\n" + RESET) 
else:
  print(B_YELLOW + "======================================================")
  print("|| FELICIDADES", jugadores[1], "HAS GANADO!!!")
  print("=======================================================\n" + RESET)