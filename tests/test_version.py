"""Unit tests for __version__.py."""

import diffpy.pairdistancemetric  # noqa


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(diffpy.pairdistancemetric, "__version__")
    assert diffpy.pairdistancemetric.__version__ != "0.0.0"
