from main import calcular_lucro, calcular_faturamento


def test_calcular_lucro():
  faturamento = calcular_faturamento()
  assert calcular_lucro(faturamento, 5000) > 0