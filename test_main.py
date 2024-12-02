from main import calcular_lucro, calcular_faturamento, calcular_custo
import pytest


def test_calcular_lucro():
  faturamento = calcular_faturamento()
  assert calcular_lucro(faturamento, 500) > 0


#faturamento(marcador)
@pytest.mark.faturamento
def test_calcular_faturamento():
  assert calcular_faturamento() > 0

@pytest.fixture
def cotacao_dolar():
  #requsicao pra api para pegar a cotacao do dolar
  return 5


#fixtures
def test_calcular_custo(cotacao_dolar):
  assert calcular_custo(cotacao_dolar) > 0