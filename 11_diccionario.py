persona ={
    "nombre":"carlos",
    "edad":30,
    "ciudad":"bogota"
    
}

clave= input("ingrese la clave")
if clave in persona:
 print(f"{clave} existe y su valor es {persona[clave]}") 
else:
 print(f"{clave} no existe en el diccionario")



