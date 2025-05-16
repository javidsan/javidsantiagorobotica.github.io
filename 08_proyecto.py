def conversor_fc(temp):
    celcius = (temp - 32 )/1.8
    print(celcius)
    
conversor_fc("temp")
    
def conversor_cf(temp):
    farenheit = (temp * 1.8)+32
    print(farenheit)
    
conversor_cf("temp")
   
topo= input ("digite c para odtener celcius y F paran odtener farenheit")

if topo == "c":
    temp= float(input("ingrese la temperatura en celcius"))
    print(conversor_fc)
    
elif topo == "f": 
   temp= float(input("ingrese la temperatura en farenheit"))
   print(conversor_cf)
   
else:
    print("el valor ingresado no existe" )
 






     

   
   