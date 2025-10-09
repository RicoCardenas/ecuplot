import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def test_config_imports():
    """Test que las configuraciones se pueden importar correctamente"""
    try:
        from configs import API_ID, API_HASH, TOKEN
        assert API_ID is not None
        assert API_HASH is not None
        assert TOKEN is not None
    except ImportError as e:
        pytest.fail(f"No se pudieron importar las configuraciones: {e}")

def test_config_types():
    """Test que las configuraciones tienen los tipos correctos"""
    from configs import API_ID, API_HASH, TOKEN
    
    assert isinstance(API_ID, int), "API_ID debe ser un entero"
    assert isinstance(API_HASH, str), "API_HASH debe ser una cadena"
    assert isinstance(TOKEN, str), "TOKEN debe ser una cadena"

def test_config_values_not_empty():
    """Test que las configuraciones no están vacías"""
    from configs import API_HASH, TOKEN
    
    assert len(API_HASH) > 0, "API_HASH no debe estar vacío"
    assert len(TOKEN) > 0, "TOKEN no debe estar vacío"
