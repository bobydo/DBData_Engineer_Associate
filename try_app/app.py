import streamlit as st
from databricks import sql

st.set_page_config(page_title="Databricks Employees OAuth Test", page_icon="🧪")
st.title("Databricks Employees — SQL Connector Test")
st.write("Connect to a Databricks SQL Warehouse and retrieve sample employee records.")

st.markdown("""
**Connection details**
1. In Databricks, open **SQL Warehouses → Serverless Starter Warehouse → Connection details**.
2. Copy the **Server hostname** and **HTTP path**.
3. In Catalog Explorer, confirm the catalog, schema, and table names.
4. This app uses the SQL Connector's interactive OAuth support. The separate OAuth URL field is not needed here.
""")

with st.form("connection_form"):
    hostname = st.text_input(
        "Server hostname",
        placeholder="dbc-xxxxxxxx-xxxx.cloud.databricks.com",
        help="Copy only the hostname, without https://."
    )
    http_path = st.text_input(
        "HTTP path",
        placeholder="/sql/1.0/warehouses/...",
        help="Copy the complete HTTP path from the warehouse's Connection details."
    )
    catalog = st.text_input("Catalog", value="dbacademy")
    schema = st.text_input("Schema", value="get_started_de")
    table = st.text_input("Table", value="employees")
    limit = st.number_input("Maximum rows", min_value=1, max_value=1000, value=20, step=10)
    submitted = st.form_submit_button("Sign in with Databricks OAuth and retrieve rows", type="primary")

if submitted:
    if not hostname.strip() or not http_path.strip():
        st.error("Enter the Server hostname and HTTP path.")
        st.stop()

    if not catalog.strip() or not schema.strip() or not table.strip():
        st.error("Catalog, schema, and table must all be filled in.")
        st.stop()

    host = hostname.strip().removeprefix("https://").removeprefix("http://").rstrip("/")
    parts = [catalog.strip(), schema.strip(), table.strip()]
    identifier = ".".join("`" + p.replace("`", "``") + "`" for p in parts)
    query = f"SELECT * FROM {identifier} LIMIT {int(limit)}"

    try:
        with st.spinner("Starting Databricks OAuth sign-in and running the query..."):
            with sql.connect(
                server_hostname=host,
                http_path=http_path.strip(),
                auth_type="databricks-oauth",
            ) as connection:
                with connection.cursor() as cursor:
                    st.code(query, language="sql")
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    columns = [column[0] for column in cursor.description] if cursor.description else []

        st.success(f"Connected successfully. Retrieved {len(rows)} row(s).")
        if rows:
            st.dataframe([dict(zip(columns, row)) for row in rows], use_container_width=True)
        else:
            st.warning("The query succeeded but returned no rows.")
    except Exception as exc:
        st.error("Connection or query failed.")
        st.exception(exc)
        st.markdown("""
**Common checks**
- Confirm the warehouse is running and you copied the hostname and HTTP path from that warehouse.
- Confirm your Databricks account has permission to use the warehouse and read the table.
- Confirm the table's full name is `dbacademy.get_started_de.employees`.
- Update packages with `python -m pip install -U databricks-sql-connector`.
""")

st.divider()
st.caption("This demo uses interactive OAuth sign-in. It does not ask you to paste an access token or client secret.")
