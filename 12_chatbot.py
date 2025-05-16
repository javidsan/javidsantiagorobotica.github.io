print("hola soy tu asistente virtual")
print("ingrese el numero --1-- para saber que grado de pirotecnia manejamos")
print("ingrese el numero --2-- para saber que pirotecnia manejamos")
print("ingrese el numero --3-- para saber si manejamos la linea de muñecos en plastico")
print("ingrese el numero --4-- para saber ¿donde estamos ubicados?")
print("ingrese el numero --5-- para saber ¿tienen redes sociales?")
print("ingrese el numero --6-- para saber ¿como los buscamos en su pagina wed?")
print("ingrese el numero --7-- para saber ¿manejamos fusiles?")
print("ingrese el numero --8-- para matar el chatbot")


answer={
    1: "tenemos pirotecnia de 1 a 10 grado",
    2: "tenemos: volcanes, dinamitas, TNT, bombas nucleares",
    3: "tambien manejamos toda la linea de presidentes en plastico",
    4: "estamos ubicados en la transversal 15 #6372-8e",
    5: "nos puedes encontrar en nuestras redes como @losmassapos_123",
    6: "entra a www.perrossapos.com",
    7: "manejamos armas de costa, media y larga distancia",
    8: "mataste el chatbot",
}




while True:
    respuesta= input("ingrese el numero correspondiente a su pregunta\n")

    if respuesta in answer:
     print(f"si claro,{answer[respuesta]}")
           
    else:
     print("no encontramos tu respuesta")
      
   
  
      
      
      