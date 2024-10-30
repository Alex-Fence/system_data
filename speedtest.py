from speedtest import Speedtest
inet = Speedtest
download = float(str(inet.download()) [0:2] + "." + str(round(inet.download(), 2)) [1]) * 0.125
uploads = float(str(inet.upload()) [0:2] + "." + str(round(inet.download(), 2)) [1]) * 0.125
print(f'{download:} {uploads:}')

