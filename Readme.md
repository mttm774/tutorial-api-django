commando para ejecutar los tests

python3 manage.py test AppVehiculos.tests    


comando para cobertura

coverage run --source='AppVehiculos' manage.py test AppVehiculos.tests 
coverage report    
coverage html    


.github
