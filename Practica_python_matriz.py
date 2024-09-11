from statistics import mean
#FUNCION RESPUESTA AL EJERCICIO
def process_matrix(matrix):
    """Función que procesa una matriz para hacer el promedio de cada número y sus vecinos"""
    lm=len(matrix)-1 
    ll=len(matrix[0])-1
    New_matrix=[]#LISTA VACIA PARA ACUMULAR MATRIZ NUEVA
    for i in range(len(matrix)): #BUCLE DE LISTA EN MATRIZ 
        New_list=[]#LISTA VACIA PARA ACUMULAR LAS LISTAS DE LA NUEVA MATRIZ
        y=1 
        for j in range(len(matrix[0])):#BUCLE DE ELEMENTO EN LISTA
            if i==0: 
                if j==0:#ESQ SUP IZQ 
                    Sol=[matrix[0][0],matrix[0][1],matrix[1][0]]
                elif j==ll:#ESQ SUP DER 
                    Sol=[matrix[0][j],matrix[0][j-1],matrix[1][j]]
                else:#LADO ARRIBA
                    Sol=[matrix[0][j],matrix[0][j-1],matrix[0][j+1],matrix[1][j]]
                    y+=1
            elif i==lm: 
                if j==0:#ESQ INF IZQ
                    Sol=[matrix[i][0],matrix[i-1][0],matrix[i][1]]
                elif j==ll:#ESQ INF DER
                    Sol=[matrix[i][j],matrix[i][j-1],matrix[i-1][j]]
                else:#LADO ABAJO 
                    Sol=[matrix[i][j],matrix[i][j-1],matrix[i][j+1],matrix[i-1][j]]
                    y+=1
            else:
                if j==0:#LADO IZQ
                    Sol=[matrix[i][0],matrix[i-1][0],matrix[i+1][0],matrix[i][1]]
                elif j==ll:#LADO DER
                    Sol=[matrix[i][j],matrix[i+1][j],matrix[i-1][j],matrix[i][j-1]]
                else:#ELEM MEDIO
                    Sol=[matrix[i][j],matrix[i-1][j],matrix[i+1][j],matrix[i][j+1],matrix[i][j-1]]
                    y+=1
                
            New_list.append(round(mean(Sol),1))
        New_matrix.append(New_list)
    return New_matrix

#FUNCION QUE TRANSPONE LA MATRIZ NUEVA 
def transpose(New_matrix):
    matrizN=[]
    i=0
    while i<len(New_matrix[0]):
        listaN=[]
        for lista in New_matrix:
            listaN.append(lista[i])
        matrizN.append(listaN)
        i+=1
    return matrizN

#FUNCION QUE IMPRIME LA MATRIZ
def print_matrix(matrizN):
    col=0
    row=0
    while col<len(matrizN):
        print("|", end="")
        while row<len(matrizN[col]):
            print(" " +format(matrizN[col][row]), end=" ")
            print(" ", end="")
            row+=1
        print("|")
        row=0
        col+=1

print_matrix(transpose(process_matrix([[3,2],
                                       [4,1],
                                       [2,3]])))
print_matrix(transpose(process_matrix([[0,1,2],
                                       [0,1,2],
                                       [0,1,2]])))
print_matrix(transpose(process_matrix([[0,1,2,4,5],
                                        [4,1,2,5,5],
                                        [0,4,2,2,5],
                                        [0,1,2,4,5],
                                        [0,1,2,9,5],
                                        [3,1,2,4,5],
                                        [0,1,2,1,5],
                                        [0,1,2,2,5],
                                        [8,1,2,2,5],
                                        [4,1,2,9,5]])))
print_matrix(transpose(process_matrix([[0,1,2,4],
                                       [0,1,2,5], 
                                       [0,1,2,2]])))
