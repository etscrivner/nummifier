#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_nummifier
----------------------------------

Tests for `nummifier` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from nummifier import nummifier
from nummifier import cli



class TestNummifier(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, ["test"])
        assert result.exit_code == 0
        assert 'test' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
