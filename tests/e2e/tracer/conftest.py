import pytest

from tests.e2e.tracer.infrastructure import TracerStack


@pytest.fixture(autouse=True, scope="module")
def infrastructure():
    """Setup and teardown logic for E2E test infrastructure


    Yields
    ------
    Dict[str, str]
        CloudFormation Outputs from deployed infrastructure
    """
    stack = TracerStack()
    try:
        yield stack.deploy()
    finally:
        stack.delete()
