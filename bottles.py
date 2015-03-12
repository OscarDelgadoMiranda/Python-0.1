#Funcion con la cancion
def MySong(bottles):
	for i in range(bottles):
		print bottles-i, "bottles of beer on the wall,", bottles-i, "bottles of beer."
		print "Take one down, pass it around,", bottles-i-1, "bottles of beer on the wall."
		
#Llamada a la funcion con el numero de bolletas que quieras
MySong(10)
