import serial, time
ser = serial.Serial()

ser.port = "COM11"

ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
try:
    ser.open()
except Exception:
    print("error al abrir el puerto serial ")
    exit()

if ser.isOpen():

    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output
                 #and discard all that is in buffer

        #escribir un dato
        ser.write(b'S')
        print("write data: S")
        #leer un dato
        time.sleep(0.5)  #give the serial port sometime to receive the data
        datos_recibidos = ser.read(3)
        print(datos_recibidos)



        ser.close()

    except Exception:
        print("error de comunicacion...: ")

else:
    print("no se puede abrir el puerto ")
