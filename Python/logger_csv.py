import serial


ser = serial.Serial('/dev/ttyUSB1')
ser.flushInput()

while True:
    ser_bytes = ser.readline()
    if len(ser_bytes) > 2:
        print(ser_bytes.decode("utf-8"))
    with open('data.csv', 'a') as f:
        if len(ser_bytes) > 2:
            f.write(ser_bytes.decode("utf-8"))
        f.close()
