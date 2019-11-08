#!/usr/bin/python3

from socket import *
import student_pb2

student = student_pb2.Student() #Creo un objeto del tipo studen pero sin datos

ip = "172.19.194.240" #Defino la ip y el puerto
puerto = 2000


sock = socket(AF_INET,SOCK_DGRAM) #Creo el socket para el cliente
destino=((ip,puerto)) #Creo una tupla que representa el destinatario

#Añado mis datos como usuario student
student.DNI = "02598787V"
student.firstname = "Rosa"
student.lastname = "Sacedon Ortega"
student.grade = student_pb2.Student.PASS

#Serializo el mensaje para poder enviarlo posteriormente
msj = student.SerializeToString()
#Envio el mensaje con mis datos
sock.sendto(msj, destino)

sock.close()
