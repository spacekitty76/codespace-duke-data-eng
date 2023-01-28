"""Doc String"""
from click.testing import CliRunner
from hello import search

# `make test` to run locally
# search(path, ftype):


def test_search():
    """Doc String."""
    runner = CliRunner()
    result = runner.invoke(search, ["--path", ".", "--ftype", "py"])
    assert result.exit_code == 0
    assert "hello" in result.output
