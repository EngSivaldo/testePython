from main import calcular_lucro, calcular_faturamento
import pytest


def test_calcular_lucro():
  faturamento = calcular_faturamento()
  assert calcular_lucro(faturamento, 500) > 0


#faturamento(marcador)
@pytest.mark.faturamento
def test_calcular_faturamento():
  assert calcular_faturamento() > 0