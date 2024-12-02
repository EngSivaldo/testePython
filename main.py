#sistema gerencial

#calcular o faturamento
def calcular_faturamento():
  vendas = [100,300,400,500,600]
  faturamento = sum(vendas)
  return faturamento

#calcular custo(em dolar)
def calcular_custo(cotacao_dolar):
  custo = 1000 * cotacao_dolar
  return custo

#calcular lucro
def calcular_lucro(faturamento, custo):
  lucro = faturamento - custo
  return lucro


# print(calcular_lucro(1000, 500))
print(calcular_faturamento())
