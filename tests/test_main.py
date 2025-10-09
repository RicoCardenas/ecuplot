import pytest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_main_imports():
    """Test que se pueden importar los módulos principales"""
    try:
        import main
        assert hasattr(main, 'bot')
        assert hasattr(main, 'plugins')
    except ImportError as e:
        pytest.fail(f"No se pudo importar main: {e}")

def test_plugins_configuration():
    """Test que los plugins están configurados correctamente"""
    import main
    
    assert main.plugins == dict(root='plugins')
    assert 'root' in main.plugins
    assert main.plugins['root'] == 'plugins'

@patch('pyrogram.Client')
def test_bot_configuration(mock_client):
    """Test que el bot se configura correctamente"""
    # Mock del cliente de Pyrogram
    mock_bot_instance = MagicMock()
    mock_client.return_value = mock_bot_instance
    
    if 'main' in sys.modules:
        del sys.modules['main']
    
    import main
    
    # Verificar que Client fue llamado
    mock_client.assert_called_once()
    
    # Verificar los argumentos básicos
    call_args = mock_client.call_args
    assert call_args[0][0] == "EcuPlotBot"
    assert 'api_id' in call_args[1]
    assert 'api_hash' in call_args[1]
    assert 'bot_token' in call_args[1]
    assert call_args[1]['lang_code'] == 'es'
    assert call_args[1]['plugins'] == dict(root='plugins')

def test_bot_instance_exists():
    """Test que la instancia del bot existe"""
    import main
    assert main.bot is not None
    assert hasattr(main.bot, 'start')
    assert hasattr(main.bot, 'run')

def test_main_module_structure():
    """Test que verifica la estructura básica del módulo main"""
    import main
    
    assert hasattr(main, 'plugins')
    assert hasattr(main, 'bot')
    
    assert isinstance(main.plugins, dict)
    assert main.plugins.get('root') == 'plugins'
    
    # Verificar que el bot no es None
    assert main.bot is not None