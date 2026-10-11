# Databricks Certified Data Engineer Associate (2026) — Practice Questions

**Questions only — answer key is in a separate file.**

**Scope:** Course Sections 02–25, based on the section/lesson organization in the uploaded transcript ZIP. Questions are original practice material, not actual exam questions or verified exam recalls.

**How to use:** Finish a section's lessons, then answer that section without opening the separate answer key. Select the answer option(s) that you believe are correct for each question. Some questions may have more than one correct option. Keep your answers in a separate scratch sheet.

**Exam alignment note:** The current exam guide effective May 4, 2026 describes 45 scored multiple-choice questions and 90 minutes. This section bank is for learning and is not a prediction of exact exam weighting.

## Answer sheet template

Copy this template into your notes and record the option letter(s) you believe are correct before opening the answer key:

| Section | Answers |
|---|---|
| 02 — Databricks Building Blocks | 1: __  2: __  3: __  4: __  5: __ |
| 03 — Lakehouse Architecture Fundamentals | 1: __  2: __  3: __  4: __  5: __ |
| 04 — Data Governance & Unity Catalog | 1: __  2: __  3: __  4: __  5: __ |
| 05 — Getting Started with ETL Apache Spark | 1: __  2: __  3: __  4: __  5: __ |
| 06 — Data Engineering with Apache Spark – Bronze Layer | 1: __  2: __  3: __  4: __  5: __ |
| 07 — Data Engineering with Apache Spark – Silver Layer | 1: __  2: __  3: __  4: __  5: __ |
| 08 — Data Engineering with Apache Spark – Gold Layer | 1: __  2: __  3: __  4: __  5: __ |
| 09 — Real-Time Data Processing with Spark Structured Streaming | 1: __  2: __  3: __  4: __  5: __ |
| 10 — Scalable Data Ingestion with Databricks Auto Loader | 1: __  2: __  3: __  4: __  5: __ |
| 11 — SQL-Based Data Ingestion with COPY INTO and Delta Lake | 1: __  2: __  3: __  4: __  5: __ |
| 12 — Analytics, Dashboards, and AI with Databricks SQL | 1: __  2: __  3: __  4: __  5: __ |
| 13 — Lakeflow Connect- From Raw Data to Delta Tables | 1: __  2: __  3: __  4: __  5: __ |
| 14 — Advanced Lakeflow Jobs- Dynamic, Conditional & Data-Driven Pipelines | 1: __  2: __  3: __  4: __  5: __ |
| 15 — Introduction to Delta Live Tables and Lakeflow Pipelines | 1: __  2: __  3: __  4: __  5: __ |
| 16 — Exploring the DLT Development Environment | 1: __  2: __  3: __  4: __  5: __ |
| 17 — Building and Running Your First DLT Pipeline | 1: __  2: __  3: __  4: __  5: __ |
| 18 — Building Streaming Data Pipelines with Auto Loader | 1: __  2: __  3: __  4: __  5: __ |
| 19 — Building Unified Streaming Tables with Append Flows | 1: __  2: __  3: __  4: __  5: __ |
| 20 — Change Data Capture with Auto CDC Flow | 1: __  2: __  3: __  4: __  5: __ |
| 21 — Managing Slowly Changing Dimensions Type 1 | 1: __  2: __  3: __  4: __  5: __ |
| 22 — Managing Slowly Changing Dimensions Type 2 | 1: __  2: __  3: __  4: __  5: __ |
| 23 — Ensuring Data Quality in Delta Live Tables | 1: __  2: __  3: __  4: __  5: __ |
| 24 — Building Dynamic and Parameterized DLT Pipelines | 1: __  2: __  3: __  4: __  5: __ |
| 25 — Recent Updates in Lakeflow Declarative Pipelines | 1: __  2: __  3: __  4: __  5: __ |

---

## Section 02 — Databricks Building Blocks

### Q1. A data engineer is reviewing the Databricks workspace and its compute options. Which statements are correct?

**Objective:** Databricks architecture and compute

- **A.** The control plane provides workspace and management services.
- **B.** Notebook code executes its distributed computation on the selected compute resources.
- **C.** Editing a notebook cell means its Spark transformations have already executed.
- **D.** Compute selection should consider workload requirements, supported capabilities, and cost.

### Q2. A data engineer is reviewing the Databricks workspace and its compute options. Which statements are correct?

**Objective:** Databricks architecture and compute

- **A.** The control plane provides workspace and management services.
- **B.** Notebook code executes its distributed computation on the selected compute resources.
- **C.** Editing a notebook cell means its Spark transformations have already executed.
- **D.** Compute selection should consider workload requirements, supported capabilities, and cost.

### Q3. A data engineer is reviewing the Databricks workspace and its compute options. Which statements are correct?

**Objective:** Databricks architecture and compute

- **A.** The control plane provides workspace and management services.
- **B.** Notebook code executes its distributed computation on the selected compute resources.
- **C.** Editing a notebook cell means its Spark transformations have already executed.
- **D.** Compute selection should consider workload requirements, supported capabilities, and cost.

### Q4. A notebook contains SQL cells and Python cells. The analyst wants to run a SQL statement from a notebook cell and then use the resulting table in a later cell. Which approach is appropriate?

- **A.** Use a SQL cell or the supported SQL execution mechanism, then reference the resulting table/view or returned result appropriately in the next cell.
- **B.** Use `pip install sql` to turn every Python cell into a SQL warehouse.
- **C.** Rename the notebook `.dbc` so SQL execution is enabled.
- **D.** Run `display()` before the SQL statement; display starts the SQL engine.


### Q5. A team wants to export a notebook with its source and import it into another workspace. Which statement is safest?

- **A.** A `.dbc` archive is always a plain text Python file.
- **B.** Notebook export formats differ; use a supported notebook source or archive format and verify what metadata/content the chosen format preserves.
- **C.** A notebook can only be moved by copying its rendered output.
- **D.** A notebook export automatically transfers its compute, secrets, and Unity Catalog grants.


## Section 03 — Lakehouse Architecture Fundamentals

### Q1. A data engineer is reviewing lakehouse and Delta Lake fundamentals. Which statements are correct?

**Objective:** Lakehouse and Delta Lake

- **A.** Delta Lake uses a transaction log to coordinate table changes and versions.
- **B.** The medallion pattern commonly progresses from Bronze to Silver to Gold.
- **C.** A lakehouse requires all data to be moved into a proprietary row-store before analysis.
- **D.** Time travel and history behavior depends on retained table versions and applicable configuration.

### Q2. A data engineer is reviewing lakehouse and Delta Lake fundamentals. Which statements are correct?

**Objective:** Lakehouse and Delta Lake

- **A.** Delta Lake uses a transaction log to coordinate table changes and versions.
- **B.** The medallion pattern commonly progresses from Bronze to Silver to Gold.
- **C.** A lakehouse requires all data to be moved into a proprietary row-store before analysis.
- **D.** Time travel and history behavior depends on retained table versions and applicable configuration.

### Q3. A data engineer is reviewing lakehouse and Delta Lake fundamentals. Which statements are correct?

**Objective:** Lakehouse and Delta Lake

- **A.** Delta Lake uses a transaction log to coordinate table changes and versions.
- **B.** The medallion pattern commonly progresses from Bronze to Silver to Gold.
- **C.** A lakehouse requires all data to be moved into a proprietary row-store before analysis.
- **D.** Time travel and history behavior depends on retained table versions and applicable configuration.

### Q4. A data engineer is reviewing lakehouse and Delta Lake fundamentals. Which statements are correct?

**Objective:** Lakehouse and Delta Lake

- **A.** Delta Lake uses a transaction log to coordinate table changes and versions.
- **B.** The medallion pattern commonly progresses from Bronze to Silver to Gold.
- **C.** A lakehouse requires all data to be moved into a proprietary row-store before analysis.
- **D.** Time travel and history behavior depends on retained table versions and applicable configuration.

### Q5. A team wants to inspect prior Delta table versions and understand how table changes are tracked. Which concept should it study first?

- **A.** Notebook command history only.
- **B.** The Delta transaction log and table history/versioning features.
- **C.** Spark's `collect()` method.
- **D.** The workspace folder recycle bin.


## Section 04 — Data Governance & Unity Catalog

### Q1. A data engineer is reviewing Unity Catalog access and governance. Which statements are correct?

**Objective:** Unity Catalog

- **A.** Privileges can be granted to groups as well as individual users.
- **B.** Granting SELECT automatically grants MODIFY on the same table.
- **C.** Access can require privileges on parent namespaces as well as the target table.
- **D.** Registering an external table automatically prevents all direct access to its cloud files.

### Q2. A data engineer is reviewing Unity Catalog access and governance. Which statements are correct?

**Objective:** Unity Catalog

- **A.** Privileges can be granted to groups as well as individual users.
- **B.** Granting SELECT automatically grants MODIFY on the same table.
- **C.** Access can require privileges on parent namespaces as well as the target table.
- **D.** Registering an external table automatically prevents all direct access to its cloud files.

### Q3. A data engineer is reviewing Unity Catalog access and governance. Which statements are correct?

**Objective:** Unity Catalog

- **A.** Privileges can be granted to groups as well as individual users.
- **B.** Granting SELECT automatically grants MODIFY on the same table.
- **C.** Access can require privileges on parent namespaces as well as the target table.
- **D.** Registering an external table automatically prevents all direct access to its cloud files.

### Q4. A data engineer is reviewing Unity Catalog access and governance. Which statements are correct?

**Objective:** Unity Catalog

- **A.** Privileges can be granted to groups as well as individual users.
- **B.** Granting SELECT automatically grants MODIFY on the same table.
- **C.** Access can require privileges on parent namespaces as well as the target table.
- **D.** Registering an external table automatically prevents all direct access to its cloud files.

### Q5. A data engineer is setting up access to a Unity Catalog table for an analyst group. Which statements correctly describe access control and governance?

- **A.** `GRANT SELECT` can provide read access to a table when the principal also has the required parent-level privileges.
- **B.** Granting `SELECT` on a table automatically grants `MODIFY` on that table.
- **C.** Unity Catalog privileges can be granted to groups as well as individual users.
- **D.** An external table's underlying cloud files are automatically protected from all direct access solely because the table is registered in Unity Catalog.
## Section 05 — Getting Started with ETL Apache Spark

### Q1. A data engineer is reviewing Spark ETL behavior. Which statements are correct?

**Objective:** ETL and Spark DataFrames

- **A.** Spark DataFrames represent distributed, table-like data.
- **B.** Transformations are generally evaluated lazily until an action requires execution.
- **C.** Calling collect() is always the safest way to inspect a large production dataset.
- **D.** An optimizer can use a logical plan to optimize supported transformations.

### Q2. A data engineer is reviewing Spark ETL behavior. Which statements are correct?

**Objective:** ETL and Spark DataFrames

- **A.** Spark DataFrames represent distributed, table-like data.
- **B.** Transformations are generally evaluated lazily until an action requires execution.
- **C.** Calling collect() is always the safest way to inspect a large production dataset.
- **D.** An optimizer can use a logical plan to optimize supported transformations.

### Q3. A data engineer is reviewing Spark ETL behavior. Which statements are correct?

**Objective:** ETL and Spark DataFrames

- **A.** Spark DataFrames represent distributed, table-like data.
- **B.** Transformations are generally evaluated lazily until an action requires execution.
- **C.** Calling collect() is always the safest way to inspect a large production dataset.
- **D.** An optimizer can use a logical plan to optimize supported transformations.

### Q4. A data engineer is reviewing Spark ETL behavior. Which statements are correct?

**Objective:** ETL and Spark DataFrames

- **A.** Spark DataFrames represent distributed, table-like data.
- **B.** Transformations are generally evaluated lazily until an action requires execution.
- **C.** Calling collect() is always the safest way to inspect a large production dataset.
- **D.** An optimizer can use a logical plan to optimize supported transformations.

### Q5. A DataFrame is very large. A developer wants to inspect a few example records interactively. Which approach is safer than collecting the entire dataset to the driver?

- **A.** Use a bounded display or `limit()`-based inspection.
- **B.** Call `collect()` on every row.
- **C.** Convert all rows to a single Python string.
- **D.** Increase notebook output size until every row is visible.


## Section 06 — Data Engineering with Apache Spark – Bronze Layer

### Q1. A data engineer is designing a Bronze ingestion layer. Which statements are correct?

**Objective:** Bronze layer ingestion

- **A.** Bronze commonly preserves source data with useful ingestion metadata.
- **B.** Bronze should always contain only final business aggregates.
- **C.** Deeper cleansing and conformance commonly happen in later layers.
- **D.** Blind deduplication is safe even when the business key and survivor rule are unknown.

### Q2. A data engineer is designing a Bronze ingestion layer. Which statements are correct?

**Objective:** Bronze layer ingestion

- **A.** Bronze commonly preserves source data with useful ingestion metadata.
- **B.** Bronze should always contain only final business aggregates.
- **C.** Deeper cleansing and conformance commonly happen in later layers.
- **D.** Blind deduplication is safe even when the business key and survivor rule are unknown.

### Q3. A data engineer is designing a Bronze ingestion layer. Which statements are correct?

**Objective:** Bronze layer ingestion

- **A.** Bronze commonly preserves source data with useful ingestion metadata.
- **B.** Bronze should always contain only final business aggregates.
- **C.** Deeper cleansing and conformance commonly happen in later layers.
- **D.** Blind deduplication is safe even when the business key and survivor rule are unknown.

### Q4. A profiling report shows null values in a required customer identifier. What is the best next step before promoting the data to Silver?

- **A.** Ignore all nulls because Spark does not support null values.
- **B.** Quantify the issue, determine whether the source or business rule permits nulls, and apply a documented remediation or quarantine rule.
- **C.** Replace every null with the same arbitrary customer ID.
- **D.** Cast the identifier to a timestamp.


### Q5. A DataFrame is built from a file path that should remain outside the managed table's storage lifecycle. What should the engineer distinguish before creating a table?

- **A.** A DataFrame cannot read external files.
- **B.** Reading files from a path is separate from deciding whether a registered table is managed or external.
- **C.** Any table created from a DataFrame is automatically external.
- **D.** External tables never need governance.


## Section 07 — Data Engineering with Apache Spark – Silver Layer

### Q1. A data engineer is cleaning data for a Silver table. Which statements are correct?

**Objective:** Silver layer transformations

- **A.** Silver transformations may standardize data types and clean invalid values.
- **B.** A left join preserves all rows from its left input, with nulls for unmatched right-side columns.
- **C.** dropDuplicates() guarantees that the newest record is retained.
- **D.** explode can produce one output row per element of an array or map.

### Q2. A data engineer is cleaning data for a Silver table. Which statements are correct?

**Objective:** Silver layer transformations

- **A.** Silver transformations may standardize data types and clean invalid values.
- **B.** A left join preserves all rows from its left input, with nulls for unmatched right-side columns.
- **C.** dropDuplicates() guarantees that the newest record is retained.
- **D.** explode can produce one output row per element of an array or map.

### Q3. A data engineer is cleaning data for a Silver table. Which statements are correct?

**Objective:** Silver layer transformations

- **A.** Silver transformations may standardize data types and clean invalid values.
- **B.** A left join preserves all rows from its left input, with nulls for unmatched right-side columns.
- **C.** dropDuplicates() guarantees that the newest record is retained.
- **D.** explode can produce one output row per element of an array or map.

### Q4. A data engineer is cleaning data for a Silver table. Which statements are correct?

**Objective:** Silver layer transformations

- **A.** Silver transformations may standardize data types and clean invalid values.
- **B.** A left join preserves all rows from its left input, with nulls for unmatched right-side columns.
- **C.** dropDuplicates() guarantees that the newest record is retained.
- **D.** explode can produce one output row per element of an array or map.

### Q5. A Silver table must contain one row per customer, choosing the most recent source record by `updated_at`. Which method is more deterministic than an unordered `dropDuplicates`?

- **A.** Use a window function ordered by `updated_at` and retain the top-ranked record per customer, with a tie-breaker if needed.
- **B.** Call `dropDuplicates()` and assume Spark always keeps the newest record.
- **C.** Sort the display output after writing and assume the stored table changes.
- **D.** Use `union()` to remove duplicates.


## Section 08 — Data Engineering with Apache Spark – Gold Layer

### Q1. A data engineer is preparing a Gold data product for analytics. Which statements are correct?

**Objective:** Gold layer modeling

- **A.** Gold data products commonly provide curated business metrics for consumption.
- **B.** Unexpected row multiplication after a join can indicate non-unique join keys or an incorrect condition.
- **C.** A ratio can be interpreted correctly without defining its denominator.
- **D.** Reusable curated tables can help standardize metric definitions.

### Q2. A data engineer is preparing a Gold data product for analytics. Which statements are correct?

**Objective:** Gold layer modeling

- **A.** Gold data products commonly provide curated business metrics for consumption.
- **B.** Unexpected row multiplication after a join can indicate non-unique join keys or an incorrect condition.
- **C.** A ratio can be interpreted correctly without defining its denominator.
- **D.** Reusable curated tables can help standardize metric definitions.

### Q3. A data engineer is preparing a Gold data product for analytics. Which statements are correct?

**Objective:** Gold layer modeling

- **A.** Gold data products commonly provide curated business metrics for consumption.
- **B.** Unexpected row multiplication after a join can indicate non-unique join keys or an incorrect condition.
- **C.** A ratio can be interpreted correctly without defining its denominator.
- **D.** Reusable curated tables can help standardize metric definitions.

### Q4. A data engineer is preparing a Gold data product for analytics. Which statements are correct?

**Objective:** Gold layer modeling

- **A.** Gold data products commonly provide curated business metrics for consumption.
- **B.** Unexpected row multiplication after a join can indicate non-unique join keys or an incorrect condition.
- **C.** A ratio can be interpreted correctly without defining its denominator.
- **D.** Reusable curated tables can help standardize metric definitions.

### Q5. A Gold table has repeated logic used by several dashboards. What is a key reason to centralize the transformation in a curated data product?

- **A.** It eliminates the need for governance and data quality.
- **B.** It provides consistent, reusable business definitions and reduces duplicated logic across consumers.
- **C.** It guarantees every query is free.
- **D.** It prevents all future schema changes.


## Section 09 — Real-Time Data Processing with Spark Structured Streaming

### Q1. A data engineer is operating a Structured Streaming query. Which statements are correct?

**Objective:** Structured Streaming

- **A.** A streaming DataFrame definition alone does not start the streaming query.
- **B.** Checkpointing can support recovery of progress and state for supported query patterns.
- **C.** Checkpointing guarantees exactly-once effects for every external sink without any sink-specific design.
- **D.** foreachBatch allows processing each micro-batch with user-defined logic.

### Q2. A data engineer is operating a Structured Streaming query. Which statements are correct?

**Objective:** Structured Streaming

- **A.** A streaming DataFrame definition alone does not start the streaming query.
- **B.** Checkpointing can support recovery of progress and state for supported query patterns.
- **C.** Checkpointing guarantees exactly-once effects for every external sink without any sink-specific design.
- **D.** foreachBatch allows processing each micro-batch with user-defined logic.

### Q3. A data engineer is operating a Structured Streaming query. Which statements are correct?

**Objective:** Structured Streaming

- **A.** A streaming DataFrame definition alone does not start the streaming query.
- **B.** Checkpointing can support recovery of progress and state for supported query patterns.
- **C.** Checkpointing guarantees exactly-once effects for every external sink without any sink-specific design.
- **D.** foreachBatch allows processing each micro-batch with user-defined logic.

### Q4. A data engineer is operating a Structured Streaming query. Which statements are correct?

**Objective:** Structured Streaming

- **A.** A streaming DataFrame definition alone does not start the streaming query.
- **B.** Checkpointing can support recovery of progress and state for supported query patterns.
- **C.** Checkpointing guarantees exactly-once effects for every external sink without any sink-specific design.
- **D.** foreachBatch allows processing each micro-batch with user-defined logic.

### Q5. A stream is lagging. Which first step gives the most useful diagnosis?

- **A.** Delete the checkpoint immediately.
- **B.** Inspect query progress, input rate, processing rate, batch duration, state growth and sink latency before changing the design.
- **C.** Increase the number of columns displayed in the notebook.
- **D.** Assume the only possible cause is a bad SQL syntax.


## Section 10 — Scalable Data Ingestion with Databricks Auto Loader

### Q1. A pipeline uses Auto Loader to ingest new files. Which statements are correct?

**Objective:** Auto Loader

- **A.** Auto Loader uses the cloudFiles source format.
- **B.** Auto Loader can track schema information in a schema location.
- **C.** Auto Loader must reprocess every previously discovered file on every run by default.
- **D.** Auto Loader supports streaming ingestion workflows.

### Q2. A pipeline uses Auto Loader to ingest new files. Which statements are correct?

**Objective:** Auto Loader

- **A.** Auto Loader uses the cloudFiles source format.
- **B.** Auto Loader can track schema information in a schema location.
- **C.** Auto Loader must reprocess every previously discovered file on every run by default.
- **D.** Auto Loader supports streaming ingestion workflows.

### Q3. A pipeline uses Auto Loader to ingest new files. Which statements are correct?

**Objective:** Auto Loader

- **A.** Auto Loader uses the cloudFiles source format.
- **B.** Auto Loader can track schema information in a schema location.
- **C.** Auto Loader must reprocess every previously discovered file on every run by default.
- **D.** Auto Loader supports streaming ingestion workflows.

### Q4. A file-ingestion workload is relatively small and runs periodically, while another continuously ingests new files at scale. Which statement is most accurate?

- **A.** `COPY INTO` and Auto Loader have different operating models; choose based on source patterns, incremental behavior, schema requirements, and pipeline needs.
- **B.** Auto Loader and `COPY INTO` are identical in every respect.
- **C.** `COPY INTO` always reloads every file and cannot be incremental.
- **D.** Auto Loader is only for JDBC databases.


### Q5. A pipeline uses Auto Loader to ingest new files arriving in cloud object storage. Which statements about Auto Loader are correct?

- **A.** Auto Loader uses the `cloudFiles` source format.
- **B.** Auto Loader can maintain schema information in a schema location.
- **C.** Auto Loader is designed to reprocess every previously discovered file on every run by default.
- **D.** Auto Loader can be used in streaming ingestion workflows.
## Section 11 — SQL-Based Data Ingestion with COPY INTO and Delta Lake

### Q1. A data engineer is using COPY INTO to load files into a Delta table. Which statements are correct?

**Objective:** COPY INTO

- **A.** COPY INTO can incrementally load files and track files already loaded, subject to its documented behavior.
- **B.** File-level ingestion tracking is the same as deduplication by arbitrary business key.
- **C.** Target schema and parsing options affect whether incoming data is accepted.
- **D.** COPY INTO and Auto Loader have identical discovery, schema evolution, and checkpoint behavior in every respect.

### Q2. A data engineer is using COPY INTO to load files into a Delta table. Which statements are correct?

**Objective:** COPY INTO

- **A.** COPY INTO can incrementally load files and track files already loaded, subject to its documented behavior.
- **B.** File-level ingestion tracking is the same as deduplication by arbitrary business key.
- **C.** Target schema and parsing options affect whether incoming data is accepted.
- **D.** COPY INTO and Auto Loader have identical discovery, schema evolution, and checkpoint behavior in every respect.

### Q3. A data engineer is using COPY INTO to load files into a Delta table. Which statements are correct?

**Objective:** COPY INTO

- **A.** COPY INTO can incrementally load files and track files already loaded, subject to its documented behavior.
- **B.** File-level ingestion tracking is the same as deduplication by arbitrary business key.
- **C.** Target schema and parsing options affect whether incoming data is accepted.
- **D.** COPY INTO and Auto Loader have identical discovery, schema evolution, and checkpoint behavior in every respect.

### Q4. A data engineer is using COPY INTO to load files into a Delta table. Which statements are correct?

**Objective:** COPY INTO

- **A.** COPY INTO can incrementally load files and track files already loaded, subject to its documented behavior.
- **B.** File-level ingestion tracking is the same as deduplication by arbitrary business key.
- **C.** Target schema and parsing options affect whether incoming data is accepted.
- **D.** COPY INTO and Auto Loader have identical discovery, schema evolution, and checkpoint behavior in every respect.

### Q5. A developer wants to use `COPY INTO` for a recurring batch file load and a streaming Auto Loader pipeline for continuous discovery. Which statement is correct?

- **A.** They are interchangeable APIs with identical checkpoint and schema behavior.
- **B.** Both can support incremental ingestion, but the design should match the file-arrival pattern, schema requirements, and orchestration model.
- **C.** Only Auto Loader can read files in cloud storage.
- **D.** Only `COPY INTO` can write to Delta.


## Section 12 — Analytics, Dashboards, and AI with Databricks SQL

### Q1. A data engineer is reviewing SQL analytics features. Which statements are correct?

**Objective:** Databricks SQL

- **A.** Non-aggregated selected columns generally need to be included in GROUP BY when aggregates are used.
- **B.** Query profiles and plans can help identify scans, joins, and execution bottlenecks.
- **C.** A dashboard filter automatically grants users SELECT on the underlying tables.
- **D.** A dashboard, query, and alert are distinct workspace objects with separate behavior and permissions.

### Q2. A data engineer is reviewing SQL analytics features. Which statements are correct?

**Objective:** Databricks SQL

- **A.** Non-aggregated selected columns generally need to be included in GROUP BY when aggregates are used.
- **B.** Query profiles and plans can help identify scans, joins, and execution bottlenecks.
- **C.** A dashboard filter automatically grants users SELECT on the underlying tables.
- **D.** A dashboard, query, and alert are distinct workspace objects with separate behavior and permissions.

### Q3. A data engineer is reviewing SQL analytics features. Which statements are correct?

**Objective:** Databricks SQL

- **A.** Non-aggregated selected columns generally need to be included in GROUP BY when aggregates are used.
- **B.** Query profiles and plans can help identify scans, joins, and execution bottlenecks.
- **C.** A dashboard filter automatically grants users SELECT on the underlying tables.
- **D.** A dashboard, query, and alert are distinct workspace objects with separate behavior and permissions.

### Q4. A data engineer is reviewing SQL analytics features. Which statements are correct?

**Objective:** Databricks SQL

- **A.** Non-aggregated selected columns generally need to be included in GROUP BY when aggregates are used.
- **B.** Query profiles and plans can help identify scans, joins, and execution bottlenecks.
- **C.** A dashboard filter automatically grants users SELECT on the underlying tables.
- **D.** A dashboard, query, and alert are distinct workspace objects with separate behavior and permissions.

### Q5. A SQL query uses a table the user cannot read. The query fails even though the dashboard exists. What is the likely issue to check?

- **A.** The dashboard color palette.
- **B.** The user's effective permissions on the source objects and any required warehouse access.
- **C.** The table's file extension only.
- **D.** The number of notebook markdown cells.


## Section 13 — Lakeflow Connect- From Raw Data to Delta Tables

### Q1. A data engineer is evaluating ingestion through Lakeflow Connect. Which statements are correct?

**Objective:** Lakeflow Connect

- **A.** Supported managed connectors can reduce the operational burden of building ingestion integrations.
- **B.** Source coverage and connector capabilities should be checked against the specific requirement.
- **C.** Destination Unity Catalog privileges automatically supply credentials for the external source system.
- **D.** Source-side access and destination governance are separate concerns.

### Q2. A data engineer is evaluating ingestion through Lakeflow Connect. Which statements are correct?

**Objective:** Lakeflow Connect

- **A.** Supported managed connectors can reduce the operational burden of building ingestion integrations.
- **B.** Source coverage and connector capabilities should be checked against the specific requirement.
- **C.** Destination Unity Catalog privileges automatically supply credentials for the external source system.
- **D.** Source-side access and destination governance are separate concerns.

### Q3. A data engineer is evaluating ingestion through Lakeflow Connect. Which statements are correct?

**Objective:** Lakeflow Connect

- **A.** Supported managed connectors can reduce the operational burden of building ingestion integrations.
- **B.** Source coverage and connector capabilities should be checked against the specific requirement.
- **C.** Destination Unity Catalog privileges automatically supply credentials for the external source system.
- **D.** Source-side access and destination governance are separate concerns.

### Q4. A data engineer is evaluating ingestion through Lakeflow Connect. Which statements are correct?

**Objective:** Lakeflow Connect

- **A.** Supported managed connectors can reduce the operational burden of building ingestion integrations.
- **B.** Source coverage and connector capabilities should be checked against the specific requirement.
- **C.** Destination Unity Catalog privileges automatically supply credentials for the external source system.
- **D.** Source-side access and destination governance are separate concerns.

### Q5. A data engineer must keep connector credentials out of source code. What is the best practice?

- **A.** Hard-code credentials into the notebook and restrict notebook sharing.
- **B.** Use the platform's supported secret/credential management and access controls, following connector-specific guidance.
- **C.** Print credentials to `stdout` for debugging.
- **D.** Store credentials in a public Git branch.


## Section 14 — Advanced Lakeflow Jobs- Dynamic, Conditional & Data-Driven Pipelines

### Q1. A data engineer is configuring a Lakeflow Job with dependent tasks. Which statements are correct?

**Objective:** Lakeflow Jobs

- **A.** Task dependencies can be represented in a DAG-style task graph.
- **B.** Retry settings can help recover from eligible transient failures.
- **C.** A downstream task must always run before its required upstream task.
- **D.** Jobs support scheduled and supported data-driven trigger types.

### Q2. A data engineer is configuring a Lakeflow Job with dependent tasks. Which statements are correct?

**Objective:** Lakeflow Jobs

- **A.** Task dependencies can be represented in a DAG-style task graph.
- **B.** Retry settings can help recover from eligible transient failures.
- **C.** A downstream task must always run before its required upstream task.
- **D.** Jobs support scheduled and supported data-driven trigger types.

### Q3. A data engineer is configuring a Lakeflow Job with dependent tasks. Which statements are correct?

**Objective:** Lakeflow Jobs

- **A.** Task dependencies can be represented in a DAG-style task graph.
- **B.** Retry settings can help recover from eligible transient failures.
- **C.** A downstream task must always run before its required upstream task.
- **D.** Jobs support scheduled and supported data-driven trigger types.

### Q4. A job sometimes fails because a transient upstream service is unavailable. What configuration can improve reliability while keeping failures visible?

- **A.** Configure a reasonable retry policy for transient failures.
- **B.** Set retries to an extremely high number and declare every run successful.
- **C.** Set appropriate timeouts and monitor the final task/run status.
- **D.** Remove task dependencies so tasks race each other.
### Q5. A Lakeflow Job has several dependent tasks and should retry a transient failure before downstream processing proceeds. Which statements are correct?

- **A.** Task dependencies can be represented in a DAG-style task graph.
- **B.** Retry settings can be configured for tasks to handle certain failures.
- **C.** A downstream task with an unmet dependency must always run before its upstream task.
- **D.** Jobs can use supported triggers such as schedules and data-driven triggers.
## Section 15 — Introduction to Delta Live Tables and Lakeflow Pipelines

### Q1. A data engineer is reviewing declarative pipeline concepts. Which statements are correct?

**Objective:** Lakeflow Declarative Pipelines

- **A.** Declarative pipelines describe data transformations while the framework manages execution and dependencies.
- **B.** Successful validation of a definition guarantees that every output record meets business rules.
- **C.** Pipeline logs and flow details can help diagnose runtime failures.
- **D.** Product terminology may change while older course materials still use legacy names.

### Q2. A data engineer is reviewing declarative pipeline concepts. Which statements are correct?

**Objective:** Lakeflow Declarative Pipelines

- **A.** Declarative pipelines describe data transformations while the framework manages execution and dependencies.
- **B.** Successful validation of a definition guarantees that every output record meets business rules.
- **C.** Pipeline logs and flow details can help diagnose runtime failures.
- **D.** Product terminology may change while older course materials still use legacy names.

### Q3. A data engineer is reviewing declarative pipeline concepts. Which statements are correct?

**Objective:** Lakeflow Declarative Pipelines

- **A.** Declarative pipelines describe data transformations while the framework manages execution and dependencies.
- **B.** Successful validation of a definition guarantees that every output record meets business rules.
- **C.** Pipeline logs and flow details can help diagnose runtime failures.
- **D.** Product terminology may change while older course materials still use legacy names.

### Q4. A data engineer is reviewing declarative pipeline concepts. Which statements are correct?

**Objective:** Lakeflow Declarative Pipelines

- **A.** Declarative pipelines describe data transformations while the framework manages execution and dependencies.
- **B.** Successful validation of a definition guarantees that every output record meets business rules.
- **C.** Pipeline logs and flow details can help diagnose runtime failures.
- **D.** Product terminology may change while older course materials still use legacy names.

### Q5. A source schema changes and a pipeline begins failing. What should the engineer check?

- **A.** The pipeline's schema expectations/evolution behavior and event logs, then update the transformation or schema policy intentionally.
- **B.** Only the notebook theme.
- **C.** Whether the SQL warehouse name has spaces.
- **D.** Whether the catalog has enough rows.


## Section 16 — Exploring the DLT Development Environment

### Q1. A data engineer is troubleshooting a pipeline in the development environment. Which statements are correct?

**Objective:** Pipeline development environment

- **A.** Pipeline update logs can help identify where a dataset failed to materialize.
- **B.** Environment-specific configuration can help prevent development output from overwriting production.
- **C.** Renaming a notebook automatically fixes a missing dependency in the pipeline graph.
- **D.** Flow-level events and upstream statuses can help isolate a failure.

### Q2. A data engineer is troubleshooting a pipeline in the development environment. Which statements are correct?

**Objective:** Pipeline development environment

- **A.** Pipeline update logs can help identify where a dataset failed to materialize.
- **B.** Environment-specific configuration can help prevent development output from overwriting production.
- **C.** Renaming a notebook automatically fixes a missing dependency in the pipeline graph.
- **D.** Flow-level events and upstream statuses can help isolate a failure.

### Q3. A data engineer is troubleshooting a pipeline in the development environment. Which statements are correct?

**Objective:** Pipeline development environment

- **A.** Pipeline update logs can help identify where a dataset failed to materialize.
- **B.** Environment-specific configuration can help prevent development output from overwriting production.
- **C.** Renaming a notebook automatically fixes a missing dependency in the pipeline graph.
- **D.** Flow-level events and upstream statuses can help isolate a failure.

### Q4. A data engineer is troubleshooting a pipeline in the development environment. Which statements are correct?

**Objective:** Pipeline development environment

- **A.** Pipeline update logs can help identify where a dataset failed to materialize.
- **B.** Environment-specific configuration can help prevent development output from overwriting production.
- **C.** Renaming a notebook automatically fixes a missing dependency in the pipeline graph.
- **D.** Flow-level events and upstream statuses can help isolate a failure.

### Q5. A developer wants a streaming dataset rather than a periodically refreshed materialized result. What must they check?

- **A.** The dataset declaration and source/transformations use the supported streaming semantics for the pipeline framework.
- **B.** The table is stored in a folder named `streaming`.
- **C.** The dashboard has an auto-refresh checkbox.
- **D.** The schema contains a column called `stream`.


## Section 17 — Building and Running Your First DLT Pipeline

### Q1. A data engineer has run a pipeline and is validating the result. Which statements are correct?

**Objective:** Running a pipeline

- **A.** Successful execution should be followed by checking the target schema and data.
- **B.** Target configuration and dataset definitions influence where output is published.
- **C.** An execution success status proves every business rule is correct.
- **D.** Quality checks can be designed to drop, quarantine, or fail on invalid data depending on the framework and policy.

### Q2. A data engineer has run a pipeline and is validating the result. Which statements are correct?

**Objective:** Running a pipeline

- **A.** Successful execution should be followed by checking the target schema and data.
- **B.** Target configuration and dataset definitions influence where output is published.
- **C.** An execution success status proves every business rule is correct.
- **D.** Quality checks can be designed to drop, quarantine, or fail on invalid data depending on the framework and policy.

### Q3. A data engineer has run a pipeline and is validating the result. Which statements are correct?

**Objective:** Running a pipeline

- **A.** Successful execution should be followed by checking the target schema and data.
- **B.** Target configuration and dataset definitions influence where output is published.
- **C.** An execution success status proves every business rule is correct.
- **D.** Quality checks can be designed to drop, quarantine, or fail on invalid data depending on the framework and policy.

### Q4. A data engineer has run a pipeline and is validating the result. Which statements are correct?

**Objective:** Running a pipeline

- **A.** Successful execution should be followed by checking the target schema and data.
- **B.** Target configuration and dataset definitions influence where output is published.
- **C.** An execution success status proves every business rule is correct.
- **D.** Quality checks can be designed to drop, quarantine, or fail on invalid data depending on the framework and policy.

### Q5. A pipeline output changes after a code update. What is the most useful comparison?

- **A.** Compare the code/configuration revision, pipeline update logs, schema and data-quality results against the prior successful run.
- **B.** Compare only the notebook font.
- **C.** Assume Delta transaction logs are unrelated to all data changes.
- **D.** Rename the pipeline and rerun without review.


## Section 18 — Building Streaming Data Pipelines with Auto Loader

### Q1. A data engineer is operating an Auto Loader streaming pipeline. Which statements are correct?

**Objective:** Auto Loader streaming pipelines

- **A.** Auto Loader supports incremental file discovery when configured appropriately.
- **B.** Deleting a checkpoint is operationally significant and can cause replay or state-reset implications.
- **C.** Changing a schema automatically guarantees every downstream transformation remains compatible.
- **D.** Source discovery, access, checkpoint state, and query configuration are useful checks when files appear missing.

### Q2. A data engineer is operating an Auto Loader streaming pipeline. Which statements are correct?

**Objective:** Auto Loader streaming pipelines

- **A.** Auto Loader supports incremental file discovery when configured appropriately.
- **B.** Deleting a checkpoint is operationally significant and can cause replay or state-reset implications.
- **C.** Changing a schema automatically guarantees every downstream transformation remains compatible.
- **D.** Source discovery, access, checkpoint state, and query configuration are useful checks when files appear missing.

### Q3. A data engineer is operating an Auto Loader streaming pipeline. Which statements are correct?

**Objective:** Auto Loader streaming pipelines

- **A.** Auto Loader supports incremental file discovery when configured appropriately.
- **B.** Deleting a checkpoint is operationally significant and can cause replay or state-reset implications.
- **C.** Changing a schema automatically guarantees every downstream transformation remains compatible.
- **D.** Source discovery, access, checkpoint state, and query configuration are useful checks when files appear missing.

### Q4. A team uses a streaming pipeline with a checkpoint and wants to reset progress for a full reprocessing. What should they understand before deleting checkpoint state?

- **A.** Removing checkpoint state can cause data to be reprocessed or state to be lost; plan a controlled reset with correct target/idempotency behavior.
- **B.** Deleting a checkpoint only clears notebook output and has no effect on processing.
- **C.** The checkpoint contains the only copy of the source data.
- **D.** The checkpoint is a user interface preference.


### Q5. The team wants a file-arrival-driven pipeline rather than a continuously running cluster. What should it evaluate?

- **A.** A supported available-now or file-arrival/job-trigger pattern appropriate to the source and latency requirement.
- **B.** A permanent infinite stream is the only supported option.
- **C.** A dashboard alert can ingest files automatically.
- **D.** A table grant can schedule a job.


## Section 19 — Building Unified Streaming Tables with Append Flows

### Q1. A data engineer is using Git integration and deployment bundles. Which statements are correct?

**Objective:** Git and bundles

- **A.** A local Git commit does not publish changes to the remote until the changes are pushed.
- **B.** Declarative Automation Bundles can define and deploy workspace resources as code.
- **C.** Bundle validation is equivalent to a full production data-quality test.
- **D.** Explicit targets and reviewed overrides help control deployment across environments.

### Q2. A data engineer is using Git integration and deployment bundles. Which statements are correct?

**Objective:** Git and bundles

- **A.** A local Git commit does not publish changes to the remote until the changes are pushed.
- **B.** Declarative Automation Bundles can define and deploy workspace resources as code.
- **C.** Bundle validation is equivalent to a full production data-quality test.
- **D.** Explicit targets and reviewed overrides help control deployment across environments.

### Q3. A data engineer is using Git integration and deployment bundles. Which statements are correct?

**Objective:** Git and bundles

- **A.** A local Git commit does not publish changes to the remote until the changes are pushed.
- **B.** Declarative Automation Bundles can define and deploy workspace resources as code.
- **C.** Bundle validation is equivalent to a full production data-quality test.
- **D.** Explicit targets and reviewed overrides help control deployment across environments.

### Q4. A data engineer is using Git integration and deployment bundles. Which statements are correct?

**Objective:** Git and bundles

- **A.** A local Git commit does not publish changes to the remote until the changes are pushed.
- **B.** Declarative Automation Bundles can define and deploy workspace resources as code.
- **C.** Bundle validation is equivalent to a full production data-quality test.
- **D.** Explicit targets and reviewed overrides help control deployment across environments.

### Q5. A deployment accidentally points at the production target while the developer intended test. Which control helps prevent this?

- **A.** Review the explicit deployment target and environment-specific overrides before deployment, and use approval/release controls where available.
- **B.** Assume the CLI infers the target from the current notebook.
- **C.** Use one shared hard-coded catalog for all environments.
- **D.** Disable validation to avoid warnings.


## Section 20 — Change Data Capture with Auto CDC Flow

### Q1. A data engineer is diagnosing a slow Spark workload. Which statements are correct?

**Objective:** Spark performance troubleshooting

- **A.** A long-running outlier task can be evidence of data skew and should be investigated with metrics.
- **B.** Spilling indicates that execution used disk for intermediate data, often due to memory pressure or expensive operations.
- **C.** Broadcasting every table is always the fastest join strategy regardless of table size.
- **D.** Spark UI stage and task metrics can help locate bottlenecks.

### Q2. A data engineer is diagnosing a slow Spark workload. Which statements are correct?

**Objective:** Spark performance troubleshooting

- **A.** A long-running outlier task can be evidence of data skew and should be investigated with metrics.
- **B.** Spilling indicates that execution used disk for intermediate data, often due to memory pressure or expensive operations.
- **C.** Broadcasting every table is always the fastest join strategy regardless of table size.
- **D.** Spark UI stage and task metrics can help locate bottlenecks.

### Q3. A data engineer is diagnosing a slow Spark workload. Which statements are correct?

**Objective:** Spark performance troubleshooting

- **A.** A long-running outlier task can be evidence of data skew and should be investigated with metrics.
- **B.** Spilling indicates that execution used disk for intermediate data, often due to memory pressure or expensive operations.
- **C.** Broadcasting every table is always the fastest join strategy regardless of table size.
- **D.** Spark UI stage and task metrics can help locate bottlenecks.

### Q4. A data engineer is diagnosing a slow Spark workload. Which statements are correct?

**Objective:** Spark performance troubleshooting

- **A.** A long-running outlier task can be evidence of data skew and should be investigated with metrics.
- **B.** Spilling indicates that execution used disk for intermediate data, often due to memory pressure or expensive operations.
- **C.** Broadcasting every table is always the fastest join strategy regardless of table size.
- **D.** Spark UI stage and task metrics can help locate bottlenecks.

### Q5. A cluster fails to start after a library change. What is the best troubleshooting sequence?

- **A.** Inspect cluster event logs and library/runtime compatibility, isolate the recent change, and test a supported dependency version.
- **B.** Delete all tables and checkpoints.
- **C.** Assume the source data contains duplicates.
- **D.** Change every table to external.


## Section 21 — Managing Slowly Changing Dimensions Type 1

### Q1. A data engineer is comparing data sharing and federation. Which statements are correct?

**Objective:** Delta Sharing and Federation

- **A.** Delta Sharing supports governed sharing of data with recipients.
- **B.** Lakehouse Federation can query supported external sources through a governed interface.
- **C.** Delta Sharing and Lakehouse Federation are identical features with different names.
- **D.** Source/connector support and performance constraints matter when using federation.

### Q2. A data engineer is comparing data sharing and federation. Which statements are correct?

**Objective:** Delta Sharing and Federation

- **A.** Delta Sharing supports governed sharing of data with recipients.
- **B.** Lakehouse Federation can query supported external sources through a governed interface.
- **C.** Delta Sharing and Lakehouse Federation are identical features with different names.
- **D.** Source/connector support and performance constraints matter when using federation.

### Q3. A data engineer is comparing data sharing and federation. Which statements are correct?

**Objective:** Delta Sharing and Federation

- **A.** Delta Sharing supports governed sharing of data with recipients.
- **B.** Lakehouse Federation can query supported external sources through a governed interface.
- **C.** Delta Sharing and Lakehouse Federation are identical features with different names.
- **D.** Source/connector support and performance constraints matter when using federation.

### Q4. A data engineer is comparing data sharing and federation. Which statements are correct?

**Objective:** Delta Sharing and Federation

- **A.** Delta Sharing supports governed sharing of data with recipients.
- **B.** Lakehouse Federation can query supported external sources through a governed interface.
- **C.** Delta Sharing and Lakehouse Federation are identical features with different names.
- **D.** Source/connector support and performance constraints matter when using federation.

### Q5. A team shares a dataset externally. Which governance principle still applies?

- **A.** Configure the recipient/share access deliberately and avoid assuming sharing removes the need for least privilege and data classification.
- **B.** All shared data becomes public by default.
- **C.** Sharing disables auditing.
- **D.** Every recipient receives workspace-admin rights.


## Section 22 — Managing Slowly Changing Dimensions Type 2

### Q1. A data engineer is reviewing streaming reliability and Unity Catalog governance. Which statements are correct?

**Objective:** Streaming guarantees and governance

- **A.** End-to-end exactly-once behavior depends on source, engine, sink, and write semantics.
- **B.** Row filters and column masks are governance controls; hiding a column in a notebook display alone does not secure the data.
- **C.** Checkpointing alone guarantees exactly-once effects for every external side effect.
- **D.** ABAC can apply supported policies based on attributes and context.

### Q2. A data engineer is reviewing streaming reliability and Unity Catalog governance. Which statements are correct?

**Objective:** Streaming guarantees and governance

- **A.** End-to-end exactly-once behavior depends on source, engine, sink, and write semantics.
- **B.** Row filters and column masks are governance controls; hiding a column in a notebook display alone does not secure the data.
- **C.** Checkpointing alone guarantees exactly-once effects for every external side effect.
- **D.** ABAC can apply supported policies based on attributes and context.

### Q3. A data engineer is reviewing streaming reliability and Unity Catalog governance. Which statements are correct?

**Objective:** Streaming guarantees and governance

- **A.** End-to-end exactly-once behavior depends on source, engine, sink, and write semantics.
- **B.** Row filters and column masks are governance controls; hiding a column in a notebook display alone does not secure the data.
- **C.** Checkpointing alone guarantees exactly-once effects for every external side effect.
- **D.** ABAC can apply supported policies based on attributes and context.

### Q4. A user can create a table but cannot read it afterward. Which approach is most appropriate?

- **A.** Review ownership, grants, parent namespace usage privileges, and the effective access path; table creation privilege alone does not guarantee all subsequent access.
- **B.** Assume create permission always includes all privileges forever.
- **C.** Disable Unity Catalog.
- **D.** Use `OPTIMIZE` to grant access.


### Q5. A team asks whether all data must be ingested into managed Delta tables before it can be governed. What is the best answer?

- **A.** No; governance options depend on the asset and architecture, including managed/external tables, volumes, sharing and federation where supported.
- **B.** Yes; Unity Catalog governs only notebook outputs.
- **C.** Yes; external tables and volumes are never governed.
- **D.** No; governance is unnecessary if files are in cloud storage.


## Section 23 — Ensuring Data Quality in Delta Live Tables

### Q1. A data engineer is configuring data quality checks in a declarative pipeline. Which statements are correct?

**Objective:** Data quality expectations

- **A.** Expectations can define conditions records are expected to satisfy.
- **B.** Depending on the configured action, an expectation can warn about violations or drop invalid records.
- **C.** Every expectation automatically repairs invalid values without transformation logic.
- **D.** Data quality checks can help detect records that violate business rules.

### Q2. A data engineer is configuring data quality checks in a declarative pipeline. Which statements are correct?

**Objective:** Data quality expectations

- **A.** Expectations can define conditions records are expected to satisfy.
- **B.** Depending on the configured action, an expectation can warn about violations or drop invalid records.
- **C.** Every expectation automatically repairs invalid values without transformation logic.
- **D.** Data quality checks can help detect records that violate business rules.

### Q3. A data engineer is configuring data quality checks in a declarative pipeline. Which statements are correct?

**Objective:** Data quality expectations

- **A.** Expectations can define conditions records are expected to satisfy.
- **B.** Depending on the configured action, an expectation can warn about violations or drop invalid records.
- **C.** Every expectation automatically repairs invalid values without transformation logic.
- **D.** Data quality checks can help detect records that violate business rules.

### Q4. A data engineer is configuring data quality checks in a declarative pipeline. Which statements are correct?

**Objective:** Data quality expectations

- **A.** Expectations can define conditions records are expected to satisfy.
- **B.** Depending on the configured action, an expectation can warn about violations or drop invalid records.
- **C.** Every expectation automatically repairs invalid values without transformation logic.
- **D.** Data quality checks can help detect records that violate business rules.

### Q5. A data engineer wants to enforce data quality rules in a declarative pipeline. Which statements are correct?

- **A.** Expectations can define conditions that records are expected to satisfy.
- **B.** Depending on the configured action, an expectation can warn about invalid records or drop them.
- **C.** Every expectation automatically repairs invalid values without any transformation logic.
- **D.** Data quality checks can help detect records that violate business rules.
## Section 24 — Building Dynamic and Parameterized DLT Pipelines

### Q1. A data engineer is deploying a bundle to development and production. Which statements are correct?

**Objective:** Bundle deployment and CI/CD

- **A.** Environment-specific settings should be explicit and reviewable.
- **B.** Validation complements, but does not replace, testing and release controls.
- **C.** Production credentials should be committed in plain text to the bundle YAML.
- **D.** Least-privilege deployment permissions and reviewed release workflows reduce risk.

### Q2. A data engineer is deploying a bundle to development and production. Which statements are correct?

**Objective:** Bundle deployment and CI/CD

- **A.** Environment-specific settings should be explicit and reviewable.
- **B.** Validation complements, but does not replace, testing and release controls.
- **C.** Production credentials should be committed in plain text to the bundle YAML.
- **D.** Least-privilege deployment permissions and reviewed release workflows reduce risk.

### Q3. A data engineer is deploying a bundle to development and production. Which statements are correct?

**Objective:** Bundle deployment and CI/CD

- **A.** Environment-specific settings should be explicit and reviewable.
- **B.** Validation complements, but does not replace, testing and release controls.
- **C.** Production credentials should be committed in plain text to the bundle YAML.
- **D.** Least-privilege deployment permissions and reviewed release workflows reduce risk.

### Q4. A data engineer is deploying a bundle to development and production. Which statements are correct?

**Objective:** Bundle deployment and CI/CD

- **A.** Environment-specific settings should be explicit and reviewable.
- **B.** Validation complements, but does not replace, testing and release controls.
- **C.** Production credentials should be committed in plain text to the bundle YAML.
- **D.** Least-privilege deployment permissions and reviewed release workflows reduce risk.

### Q5. A team wants to prevent accidental production deployments by individual developers. Which control is most appropriate?

- **A.** Use repository review/branch protection and deployment permissions/approval gates aligned to the release process.
- **B.** Give every developer account admin rights.
- **C.** Disable Git history.
- **D.** Store the production token in a shared notebook.


## Section 25 — Recent Updates in Lakeflow Declarative Pipelines

### Q1. A data engineer is reviewing table optimization and Spark troubleshooting. Which statements are correct?

**Objective:** Optimization and troubleshooting

- **A.** Optimization choices should depend on table/workload characteristics and supported features.
- **B.** Spark UI evidence can help distinguish skew, shuffle cost, spill, and resource constraints.
- **C.** Adding notebook cells automatically reduces shuffle and spill.
- **D.** Startup failures should be investigated through logs and recent configuration or dependency changes.

### Q2. A data engineer is reviewing table optimization and Spark troubleshooting. Which statements are correct?

**Objective:** Optimization and troubleshooting

- **A.** Optimization choices should depend on table/workload characteristics and supported features.
- **B.** Spark UI evidence can help distinguish skew, shuffle cost, spill, and resource constraints.
- **C.** Adding notebook cells automatically reduces shuffle and spill.
- **D.** Startup failures should be investigated through logs and recent configuration or dependency changes.

### Q3. A data engineer is reviewing table optimization and Spark troubleshooting. Which statements are correct?

**Objective:** Optimization and troubleshooting

- **A.** Optimization choices should depend on table/workload characteristics and supported features.
- **B.** Spark UI evidence can help distinguish skew, shuffle cost, spill, and resource constraints.
- **C.** Adding notebook cells automatically reduces shuffle and spill.
- **D.** Startup failures should be investigated through logs and recent configuration or dependency changes.

### Q4. A data engineer is reviewing table optimization and Spark troubleshooting. Which statements are correct?

**Objective:** Optimization and troubleshooting

- **A.** Optimization choices should depend on table/workload characteristics and supported features.
- **B.** Spark UI evidence can help distinguish skew, shuffle cost, spill, and resource constraints.
- **C.** Adding notebook cells automatically reduces shuffle and spill.
- **D.** Startup failures should be investigated through logs and recent configuration or dependency changes.

### Q5. A query spills to disk and suffers from long-running tasks after a join. Which response is best?

- **A.** Inspect query plan and task metrics, then consider reducing data before the join, handling skew, selecting an appropriate join strategy, and right-sizing resources if evidence supports it.
- **B.** Immediately disable the transaction log.
- **C.** Always cache every DataFrame permanently.
- **D.** Assume adding more notebook cells will reduce spills.


## End of question bank

Finish each section before opening the separate answer-key file. For the closest simulation of the current exam format, use the final practice session as a timed 45-question / 90-minute mixed-domain test, but do not interpret this section bank's distribution as official weighting.
