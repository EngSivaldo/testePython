from main import calcular_faturamento
import pytest

#faturamento(marcador)
@pytest.mark.faturamento
def test_calcular_faturamento():
  assert type(calcular_faturamento()) == int