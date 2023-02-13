mesConsumo ="Enero"
valorKw= 315.6
TotalKw= 994
estrato=1

consumoTotal= TotalKw*valorKw 
if estrato==1:
    descuento=consumoTotal*0.6
if estrato==2:
    descuento=consumoTotal*0.5
if estrato==3:
    descuento=consumoTotal*0.15


consumoTotal1= consumoTotal*0.6


print("El valor a total a pagar durante el mes de",  mesConsumo, "es de COP$", consumoTotal1)