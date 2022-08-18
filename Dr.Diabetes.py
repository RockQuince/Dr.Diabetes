#Atividade Machine-Learning realizada por Lucas Rocha RM93963

#Começamos importando a função desejada da biblioteca, no caso, função tree da biblioteca sklearn
#Certifique-se de tela instalada
from sklearn import tree
#Aqui definimos os dados que serão avaliados, sendo eles Glicemia em Jejum, Pós-Sobrecarga e Casual, respectivamente
dados = [[90, 130, 100], [80, 120, 110], [110, 150, 140], [140, 220, 210], [130, 210, 200],
[120, 160, 140], [80, 120, 110], [95, 135, 130], [100, 135, 120], [135, 215, 205],
[95, 135, 115], [70, 110, 105], [99, 139, 119], [140, 230, 220], [100, 140, 120],
[130, 205, 200], [150, 250, 220], [105, 145, 125], [60,110,105], [85, 155, 110],
[125,195,165], [145,220,210], [130,165,150 ], [115, 150, 130], [140, 210, 205],
[75,115, 110], [130,185,160], [140, 195,170], [60,110,105], [160, 205, 200]]
#labels = [Normal, Normal, Tolerancia, Diabetes, Diabetes, Tolerancia, Normal, Normal, Tolerancia, Diabetes, Normal, Tolerancia, Normal, Diabetes, Tolerancia, Diabetes, Diabetes, Tolerancia, Normal, Normal, Tolerancia, Diabetes, Tolerancia, Tolerancia, Diabetes, Normal, Tolerancia, Tolerancia, Normal, Diabetes]
#Uma avanliação de Glicemia normal é designada como 1, de Tolerancia a glicose diminuica como 2 e por fim o diagnostico de Diabetes Mellistus
#Criterios
#Jejum: abaixo 100 normal, de 100 a 126 tolerancia, acima ou igual a 126 diabetes
#Pós-Sobrecarga: abaixo de 140 normal, de 140 a 200 tolerancia, acima ou igual 200 diabetes
#Casual: abaixo 120 normal, de 120 a 200 tolerancia, acima ou igual a 200 diabetes
#Definindo tipos de avaliação para o programa começar a distinção
avaliacao =[
0, 0, 1, 2, 2,
1, 0, 0, 1, 2,
0, 1, 0, 2, 1,
2, 2, 1, 0, 0,
1, 2, 1, 1, 2,
0, 1, 1, 0, 2]
classif = tree.DecisionTreeClassifier() #Classificador
classif.fit(dados, avaliacao)
print(" ___   ___        ___   _    __    ___   ____ _____  ____  __  ")
print("| | \ | |_)  __  | | \ | |  / /\  | |_) | |_   | |  | |_  ( (` ")
print("|_|_/ |_| \ (_() |_|_/ |_| /_/--\ |_|_) |_|__  |_|  |_|__ _)_) ")
jejum = (input("Digite sua glicemia nos periodos de Jejum em mg/dL:"))
try:
	float(jejum)
except ValueError: 
	print("Por favor, digite apenas numeros")
pos = (input("Digite sua glicemia nos periodos de pós-sobrecarga, em mg/dL:"))
try:
	float(pos)
except ValueError:
	print("Por favor, digite apenas numeros")
casual = (input("Digite sua glicemia casual em mg/dL:"))
try:
	float(casual)
except ValueError:
	print("Por favor, digite apenas numeros")
x = classif.predict([[jejum, pos, casual]])
if x == 0:
    print("\nATENÇÃO")
    print("\nNão tire conclusões precipitadas, sempre consulte a avaliação e consulta de um proficional especializado, se voce suspeita que esta com sistomas de Diabetes, va diretamente a um proficional")
    print("\nO Resultado da sua avaliação foi: Glicemia está normal")
elif x == 1:
    print("\nATENÇÃO")
    print("\nNão tire conclusões precipitadas, sempre consulte a avaliação e consulta de um proficional especializado, se voce suspeita que esta com sistomas de Diabetes, va diretamente a um proficional")
    print("O Resultado da sua avaliação foi: Tolerancia a glicose diminuida")
else:
    print("\nATENÇÃO")
    print("\nNão tire conclusões precipitadas, sempre consulte a avaliação e consulta de um proficional especializado, se voce suspeita que esta com sistomas de Diabetes, va diretamente a um proficional")
    print("\nO Resultado da sua avaliação foi: sinais de Diabetes mellitus")
exit
