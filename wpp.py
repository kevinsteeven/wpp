import pywhatkit
numerodestino=input("Ingresar numero de destino del mensaje: ")
pywhatkit.sendwhatmsg(numerodestino,".",22,36,15,True,2)#primer parametro numero de cel, segundo y tercer hora y minuto en el que se enviara el mensaje, cuarto parametro tiempo de espera entre la escritura del mensaje y el envio, 5 parametro para el cierre de la venta y 6 tiempo de espera para cierre de la ventana