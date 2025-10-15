# test_firebasesync.py
"""
Tests for FirebaseSync module.
"""

import unittest
from firebasesync import FirebaseSync

class TestFirebaseSync(unittest.TestCase):
    """Test cases for FirebaseSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FirebaseSync()
        self.assertIsInstance(instance, FirebaseSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FirebaseSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
