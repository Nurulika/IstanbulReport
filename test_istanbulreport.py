# test_istanbulreport.py
"""
Tests for IstanbulReport module.
"""

import unittest
from istanbulreport import IstanbulReport

class TestIstanbulReport(unittest.TestCase):
    """Test cases for IstanbulReport class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IstanbulReport()
        self.assertIsInstance(instance, IstanbulReport)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IstanbulReport()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
