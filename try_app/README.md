# Databricks Employees: SQL Connector + REST API examples

This folder contains two separate ways to query the same `employees` table.

## Files

- `app.py` — Streamlit form using the Databricks SQL Connector and interactive OAuth.
- `api_call.py` — command-line example using the Databricks SQL Statement Execution REST API through the Databricks Python SDK and a saved CLI authentication profile.
- `config.py` — shared settings (CLI profile, warehouse ID / HTTP path, table), overridable via environment variables.
- `requirements.txt` — Python dependencies.

## Install dependencies

Run in PowerShell from this folder. Activate the virtual environment first, otherwise `python` is the system interpreter and you will see `ModuleNotFoundError: No module named 'databricks'`:

```powershell
python -m venv .venv          # only the first time
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If importing the SDK fails with `DLL load failed while importing _cffi_backend: An Application Control policy has blocked this file`, Windows Smart App Control is blocking the newest `cffi` binary. Pin older, widely used builds:

```powershell
python -m pip install "cffi==1.17.1" "cryptography<46"
```

## Run the Streamlit app

```powershell
python -m streamlit run app.py
```

Enter the server hostname and HTTP path from SQL Warehouse → Connection details. The app defaults to:

- Catalog: `dbacademy`
- Schema: `get_started_de`
- Table: `employees`

## Run the REST API example

First install the Databricks CLI if you have not already, then log in once to create a saved profile. Pass `--profile` explicitly so the profile name matches `config.py`:

```powershell
databricks auth login --host https://dbc-7f54ec2c-6cd5.cloud.databricks.com --profile dbc-7f54ec2c-6cd5
databricks auth profiles     # the profile should show Valid = YES
```

You only need to log in once. The login saves two things in your user folder (`C:\Users\<username>`):

| File                             | Contents                                                                                                                                                             |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.databrickscfg`               | The profile: a`[dbc-7f54ec2c-6cd5]` section with the workspace host and `auth_type = databricks-cli`. No secrets. Open it with `notepad $HOME\.databrickscfg`. |
| `.databricks\token-cache.json` | The OAuth token the SDK refreshes automatically. Do not share or commit it.                                                                                          |

`config.py` defaults to the host and profile above. If you used a different profile name, set it before running:

```powershell
$env:DATABRICKS_CONFIG_PROFILE = "YOUR_PROFILE_NAME"
```

Then run:

```powershell
python api_call.py
```

The script uses the SQL Statement Execution REST API via the Databricks SDK. It takes the warehouse ID from the end of the HTTP path:
`/sql/1.0/warehouses/9c1e27ef43724108`

All settings live in `config.py` (profile, warehouse, catalog/schema/table, row limit). Edit the defaults there, or override them with environment variables. If your warehouse differs, set either the ID or the full HTTP path before running (the ID wins if both are set):

```powershell
$env:DATABRICKS_WAREHOUSE_ID = "YOUR_WAREHOUSE_ID"
# or
$env:DATABRICKS_HTTP_PATH = "/sql/1.0/warehouses/YOUR_WAREHOUSE_ID"
```

Other overrides: `DATABRICKS_CATALOG`, `DATABRICKS_SCHEMA`, `DATABRICKS_TABLE`, `DATABRICKS_ROW_LIMIT`.

## Why there is no OAuth URL field in `api_call.py`

The SDK uses the saved CLI authentication profile to discover the workspace and obtain authentication. You generally do not manually pass the `/oidc` URL into each API request. The OAuth endpoint is used as part of the authentication flow, not as the REST API's base URL.

## Streamlit and production

Streamlit is the product name (not an acronym). It is good for internal tools, demos, data apps, and lightweight production apps. For production, configure authentication/access control, secrets management, deployment, monitoring, and resource limits. For complex public-facing apps or highly customized UX, a dedicated frontend/backend architecture may be a better fit.

Do not commit access tokens, client secrets, or other credentials to source control.
