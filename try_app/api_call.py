"""
Run a Databricks SQL query through the Databricks REST API using the Python SDK.

Prerequisites:
  1. Install the Databricks CLI and run `databricks auth login --host https://YOUR_WORKSPACE_HOSTNAME`.
  2. Install dependencies: `python -m pip install -r requirements.txt`
  3. Confirm the profile name in config.py matches the profile created by `databricks auth login`.

This script uses the SQL Statement Execution REST API through the Databricks SDK.
It does not use the SQL Connector's browser-based OAuth flow, and it does not need the
separate OAuth URL field. The SDK reads the saved CLI profile and manages authentication.
"""
import sys

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.sql import StatementState

from config import CATALOG, HOST, PROFILE, ROW_LIMIT, SCHEMA, TABLE, WAREHOUSE_ID, quoted_table_name

SQL = f"""
SELECT *
FROM {quoted_table_name()}
LIMIT {ROW_LIMIT}
""".strip()


def main():
    try:
        client = WorkspaceClient(profile=PROFILE)
        print(f"Workspace: {client.config.host}")
        print(f"CLI profile: {PROFILE}")
        print(f"Warehouse ID: {WAREHOUSE_ID}")
        print(f"SQL: {SQL}\n")

        response = client.statement_execution.execute_statement(
            warehouse_id=WAREHOUSE_ID,
            statement=SQL,
            wait_timeout="50s",
        )

        state = response.status.state if response.status else None
        if state != StatementState.SUCCEEDED:
            print(f"Statement did not complete successfully. State: {state}")
            if response.status and response.status.error:
                print(response.status.error)
            if response.statement_id:
                print(f"Statement ID: {response.statement_id}")
                print("If it is still running, check the statement in Databricks Query History.")
            sys.exit(1)

        columns = []
        if response.manifest and response.manifest.schema and response.manifest.schema.columns:
            columns = [column.name for column in response.manifest.schema.columns]

        rows = response.result.data_array if response.result and response.result.data_array else []
        print(f"Success — retrieved {len(rows)} row(s).")
        if columns:
            print("Columns:", " | ".join(columns))
        for row in rows:
            print(dict(zip(columns, row)) if columns else row)

    except Exception as exc:
        print("Databricks API call failed.")
        print(f"{type(exc).__name__}: {exc}")
        if "default credentials" in str(exc):
            print("\nNo saved login token for this profile. Log in once with:")
            print(f"  databricks auth login --host {HOST} --profile {PROFILE}")
        print("\nCheck that:")
        print(f"- The CLI profile '{PROFILE}' exists (`databricks auth profiles`).")
        print("- You can access the workspace and use the SQL warehouse.")
        print(f"- You have SELECT permission on {CATALOG}.{SCHEMA}.{TABLE}.")
        print("- The warehouse ID matches the ID at the end of your HTTP path.")
        sys.exit(1)


if __name__ == "__main__":
    main()
