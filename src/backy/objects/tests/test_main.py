import pytest

from backy.objects.main import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert capsys.readouterr().out == "Hello from backy.objects!\n"
