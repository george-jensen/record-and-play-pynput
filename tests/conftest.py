import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, MagicMock


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test use."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def temp_file(temp_dir):
    """Create a temporary file in the temp directory."""
    file_path = temp_dir / "test_file.txt"
    file_path.write_text("test content")
    yield file_path


@pytest.fixture
def mock_file():
    """Mock file object for testing."""
    mock = MagicMock()
    mock.read.return_value = "mock file content"
    mock.write.return_value = None
    mock.__enter__.return_value = mock
    mock.__exit__.return_value = None
    return mock


@pytest.fixture
def mock_config():
    """Mock configuration object."""
    config = Mock()
    config.debug = False
    config.timeout = 30
    config.retries = 3
    config.log_level = "INFO"
    return config


@pytest.fixture
def sample_data():
    """Sample data for testing."""
    return {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }


@pytest.fixture
def mock_logger():
    """Mock logger for testing."""
    logger = Mock()
    logger.info = Mock()
    logger.error = Mock()
    logger.warning = Mock()
    logger.debug = Mock()
    return logger


@pytest.fixture(autouse=True)
def clean_environment(monkeypatch):
    """Clean environment variables for consistent testing."""
    env_vars_to_remove = [
        "DEBUG", 
        "TEST_MODE", 
        "CONFIG_PATH",
        "LOG_LEVEL"
    ]
    for var in env_vars_to_remove:
        monkeypatch.delenv(var, raising=False)


@pytest.fixture
def mock_response():
    """Mock HTTP response object."""
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"status": "success"}
    response.text = '{"status": "success"}'
    response.headers = {"Content-Type": "application/json"}
    return response


@pytest.fixture(scope="session")
def session_temp_dir():
    """Session-scoped temporary directory."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)