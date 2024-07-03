"""
Test Earth Data Store authentification module.
Credentials must be defined in environment variables or
in the default credentials in order for the test to work.
"""

import json
import os
import unittest
import tempfile
import toml
from pathlib import Path

from earthdaily.earthdatastore import Auth
from earthdaily import EarthDataStore

class TestAuth(unittest.TestCase):

    def setUp(self) -> None:
        self.credentials = Auth.read_credentials()
        self.temporary_directory = Path(tempfile.mkdtemp())

        # Create JSON credentials
        self.json_path = self.temporary_directory / "credentials.json"
        with self.json_path.open('w') as f:
            json.dump(data, self.credentials)

        # Create TOML credentials
        self.toml_path = self.temporary_directory / "credentials.toml"
        with self.toml_path.open('w') as f:
            toml_credentials = {
                "default" : self.credentials,
                "test_profile" : self.credentials
            }
            toml.dump(toml_credentials, f)

    def test_from_json() -> None:
        eds = EarthDataStore(json_path = self.json_path)

    def test_from_environment() -> None:
        # Ensure environment variables are set
        os.environ["EDS_AUTH_URL"] = self.credentials["EDS_AUTH_URL"]
        os.environ["EDS_SECRET"] = self.credentials["EDS_SECRET"]
        os.environ["EDS_CLIENT_ID"] = self.credentials["EDS_CLIENT_ID"]

        eds = EarthDataStore()

    def test_from_default_profile() -> None:
        # Ensure environment variables are unset
        if "EDS_AUTH_URL" in os.environ:
            del os.environ["EDS_AUTH_URL"]
        if "EDS_SECRET" in os.environ:
            del os.environ["EDS_SECRET"]
        if "EDS_CLIENT_ID" in os.environ:
            del os.environ["EDS_CLIENT_ID"]

        eds = EarthDataStore()

    def test_from_input_profile() -> None:
        # Ensure environment variables are unset
        if "EDS_AUTH_URL" in os.environ:
            del os.environ["EDS_AUTH_URL"]
        if "EDS_SECRET" in os.environ:
            del os.environ["EDS_SECRET"]
        if "EDS_CLIENT_ID" in os.environ:
            del os.environ["EDS_CLIENT_ID"]
        eds = EarthDataStore(profile = "test_profile")
        

if __name__ == "__main__":
    unittest.main()
