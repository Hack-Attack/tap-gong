"""Tests standard tap features using the built-in SDK tests library."""

import os

from singer_sdk.testing import get_standard_tap_tests
from tap_gong.tap import TapGong

SAMPLE_CONFIG = {
    "start_date": "2024-05-29T00:00:00Z",
    "end_date": "2024-05-30T00:00:00Z",
    "access_key": os.getenv("TAP_GONG_ACCESS_KEY", "foo"),
    "access_key_secret": os.getenv("TAG_GONG_ACCESS_KEY_SECRET", "bar"),
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapGong, config=SAMPLE_CONFIG)
    for test in tests:
        test()
