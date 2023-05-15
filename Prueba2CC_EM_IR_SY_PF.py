#Solicitudes de incorporacion
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "jSD6yPYWFBOFE0kaWwUyLxK5u8yQP2cR"

while True:
	orig = input('Ciudad de origen: ')
	if orig == 'quit' or orig == 'q':
		print('Saliendo del programa')
		break
	dest = input('Ciudad de Destino: ')
	if dest == 'quit' or dest == 'q':
		print('Saliendo del programa')
		break
	url = main_api + urllib.parse.urlencode ({'key':key, 'from':orig, 'to':dest, 'unit':'k'})
	json_data = requests.get (url) .json ()
	json_status = json_data ['info'] ['statuscode']

	if json_status == 0:
    		print('API Status: ' + str(json_status) + ' = A successful route call.\n')
	if 'fuelUsed' in json_data['route']:
		print ('Se encuentra parametro fuelUsed en "route"')
	else:
		print ('NO se encuentra parametro fuelUsed en "route"')
	print ('================================')
	print ('Distancia desde '+ orig + ' hasta ' + dest)
	print ('Duraccion del viaje ' + (json_data ['route'] ['formattedTime']))
	print ('Kilometros ' + str ('{:.2f}' .format(json_data ['route'] ['distance'])))
	print ('================================')
	print ('Instrucciones para llegar a ' + dest + ' :\n')
	for each in json_data['route']['legs'][0]['maneuvers']:
		print(each['narrative'] + ' (' + str('{:.2f}'.format(each['distance'])) + ' km)')
	print (' ')
