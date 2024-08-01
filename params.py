"""Parameters file"""

import os
import logging
from dotenv import load_dotenv
from infisical_api import infisical_api


load_dotenv(override=True)
service_token = os.getenv("SERVICE_TOKEN")
app_env = os.getenv("APP_ENV")
creds = infisical_api(
    service_token=service_token, infisical_url="https://creds.kumpeapps.com"
)


class Params:
    """Parameters"""

    app_env = os.getenv("APP_ENV")

    def log_level():  # pylint: disable=no-method-argument
        """Returns Log Level"""
        if os.getenv("LOG_LEVEL") == "info":
            return logging.INFO
        elif os.getenv("LOG_LEVEL") == "warning":
            return logging.WARNING
        elif os.getenv("LOG_LEVEL") == "error":
            return logging.ERROR
        elif os.getenv("LOG_LEVEL") == "debug":
            return logging.DEBUG
        elif os.getenv("LOG_LEVEL") == "critical":
            return logging.CRITICAL
        else:
            return logging.INFO

    class SQL:
        """SQL Parameters for Web_3d User"""

        username = creds.get_secret(  # pylint: disable=no-member
            secret_name="USERNAME", environment=app_env, path="/MYSQL/"
        ).secretValue
        password = creds.get_secret(  # pylint: disable=no-member
            secret_name="PASSWORD", environment=app_env, path="/MYSQL/"
        ).secretValue
        server = creds.get_secret(  # pylint: disable=no-member
            secret_name="SERVER", environment=app_env, path="/MYSQL/"
        ).secretValue
        port = creds.get_secret(  # pylint: disable=no-member
            secret_name="PORT", environment=app_env, path="/MYSQL/"
        ).secretValue
        database = creds.get_secret(  # pylint: disable=no-member
            secret_name="DATABASE", environment=app_env, path="/MYSQL/"
        ).secretValue

        def dict():  # pylint: disable=no-method-argument
            """returns as dictionary"""
            return {
                "user": Params.SQL.username,
                "passwd": Params.SQL.password,
                "host": Params.SQL.server,
                "port": Params.SQL.port,
                "db": Params.SQL.database,
            }

    class Web:
        """Pushover API Parameters"""

        ka_api_key = creds.get_secret(  # pylint: disable=no-member
            secret_name="KA_API_KEY", environment=app_env, path="/WEB/"
        ).secretValue


if __name__ == "__main__":
    print(
        """Error: This file is a module to be imported and has no functions
          to be ran directly."""
    )
