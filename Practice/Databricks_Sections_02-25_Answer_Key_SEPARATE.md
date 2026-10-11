# Databricks Certified Data Engineer Associate (2026) — Separate Answer Key

**Do not open until you finish the corresponding section test.**

Original study questions for Sections 02–25, aligned where possible to the course transcripts and the current official exam objectives. Community reports inform style only; they do not establish official topic weighting.

## How to review

- First compare your answer letters.
- Read the explanation for every incorrect answer and any answer you guessed.
- Follow the documentation link and verify version-specific behavior.
- A link is provided as a study reference; confirm that the specific feature is supported in your workspace/runtime and the applicable exam guide.

---

## Section 02 — Databricks Building Blocks

### Q1 — Correct answers: **A, B, D**

**Objective:** Databricks architecture and compute

**Why:** The control plane provides management services; compute resources execute workloads; and compute selection depends on workload capabilities and cost. Editing a cell alone does not execute its transformations.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Databricks architecture and compute

**Why:** The control plane provides management services; compute resources execute workloads; and compute selection depends on workload capabilities and cost. Editing a cell alone does not execute its transformations.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Databricks architecture and compute

**Why:** The control plane provides management services; compute resources execute workloads; and compute selection depends on workload capabilities and cost. Editing a cell alone does not execute its transformations.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answer: **A**

**Objective:** Notebook commands and languages

**Why:** Databricks notebooks support language-specific cells and SQL execution patterns; the result must be made available through a table/view or supported returned result.

**Why the other options are incorrect:**
- B: Use `pip install sql` to turn every Python cell into a SQL warehouse.
- C: Rename the notebook `.dbc` so SQL execution is enabled.
- D: Run `display()` before the SQL statement; display starts the SQL engine.

**Official documentation:** [https://docs.databricks.com/en/notebooks/index.html](https://docs.databricks.com/en/notebooks/index.html)

---

### Q5 — Correct answer: **B**

**Objective:** Notebook import/export

**Why:** Notebook source and archive formats serve different purposes. Exporting a notebook does not automatically migrate compute settings, secrets, or access grants.

**Why the other options are incorrect:**
- A: A `.dbc` archive is always a plain text Python file.
- C: A notebook can only be moved by copying its rendered output.
- D: A notebook export automatically transfers its compute, secrets, and Unity Catalog grants.

**Official documentation:** [https://docs.databricks.com/en/notebooks/notebook-export-import.html](https://docs.databricks.com/en/notebooks/notebook-export-import.html)

---

## Section 03 — Lakehouse Architecture Fundamentals

### Q1 — Correct answers: **A, B, D**

**Objective:** Lakehouse and Delta Lake

**Why:** Delta Lake uses a transaction log; medallion layers progressively curate data; and time travel depends on available history and retention. A lakehouse does not require a proprietary row-store.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Lakehouse and Delta Lake

**Why:** Delta Lake uses a transaction log; medallion layers progressively curate data; and time travel depends on available history and retention. A lakehouse does not require a proprietary row-store.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Lakehouse and Delta Lake

**Why:** Delta Lake uses a transaction log; medallion layers progressively curate data; and time travel depends on available history and retention. A lakehouse does not require a proprietary row-store.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Lakehouse and Delta Lake

**Why:** Delta Lake uses a transaction log; medallion layers progressively curate data; and time travel depends on available history and retention. A lakehouse does not require a proprietary row-store.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **B**

**Objective:** Delta history and time travel

**Why:** Delta history and transaction-log concepts explain versioned table changes and support time-travel-related workflows where configured and retained.

**Why the other options are incorrect:**
- A: Notebook command history only.
- C: Spark's `collect()` method.
- D: The workspace folder recycle bin.

**Official documentation:** [https://docs.databricks.com/en/delta/history.html](https://docs.databricks.com/en/delta/history.html)

---

## Section 04 — Data Governance & Unity Catalog

### Q1 — Correct answers: **A, C**

**Objective:** Unity Catalog

**Why:** Unity Catalog supports group grants, and effective access may require parent namespace usage privileges plus table privileges. SELECT does not grant MODIFY; external table registration does not eliminate separately granted cloud-storage access.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, C**

**Objective:** Unity Catalog

**Why:** Unity Catalog supports group grants, and effective access may require parent namespace usage privileges plus table privileges. SELECT does not grant MODIFY; external table registration does not eliminate separately granted cloud-storage access.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, C**

**Objective:** Unity Catalog

**Why:** Unity Catalog supports group grants, and effective access may require parent namespace usage privileges plus table privileges. SELECT does not grant MODIFY; external table registration does not eliminate separately granted cloud-storage access.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, C**

**Objective:** Unity Catalog

**Why:** Unity Catalog supports group grants, and effective access may require parent namespace usage privileges plus table privileges. SELECT does not grant MODIFY; external table registration does not eliminate separately granted cloud-storage access.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

### Q5 — Correct answers: **A, C**

**Objective:** Unity Catalog privileges and governance

**Why:** `SELECT` grants read access when required parent privileges are also present, and privileges can be assigned to groups. `SELECT` does not grant `MODIFY`, and registering an external table does not by itself prevent someone with separate cloud-storage permissions from accessing its files.

**Why the other options are incorrect:**
- B: Read access and modification access are distinct privileges.
- D: External-table registration does not automatically block direct access granted at the cloud-storage layer.

**Official documentation:** [Unity Catalog privileges and securable objects](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/index.html)
## Section 05 — Getting Started with ETL Apache Spark

### Q1 — Correct answers: **A, B, D**

**Objective:** ETL and Spark DataFrames

**Why:** DataFrames are distributed table-like abstractions; Spark uses lazy evaluation for transformations; and query planning enables optimization. collect() can move all rows to the driver and is risky for large datasets.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** ETL and Spark DataFrames

**Why:** DataFrames are distributed table-like abstractions; Spark uses lazy evaluation for transformations; and query planning enables optimization. collect() can move all rows to the driver and is risky for large datasets.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** ETL and Spark DataFrames

**Why:** DataFrames are distributed table-like abstractions; Spark uses lazy evaluation for transformations; and query planning enables optimization. collect() can move all rows to the driver and is risky for large datasets.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** ETL and Spark DataFrames

**Why:** DataFrames are distributed table-like abstractions; Spark uses lazy evaluation for transformations; and query planning enables optimization. collect() can move all rows to the driver and is risky for large datasets.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** DataFrame actions

**Why:** Bounded inspection avoids unnecessarily moving a large dataset to the driver or notebook output.

**Why the other options are incorrect:**
- B: Call `collect()` on every row.
- C: Convert all rows to a single Python string.
- D: Increase notebook output size until every row is visible.

**Official documentation:** [https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.limit.html](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.limit.html)

---

## Section 06 — Data Engineering with Apache Spark – Bronze Layer

### Q1 — Correct answers: **A, C**

**Objective:** Bronze layer ingestion

**Why:** Bronze generally emphasizes faithful ingestion and traceability; deeper cleansing is typically performed downstream. Final aggregates belong in curated layers, and deduplication needs a business rule.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, C**

**Objective:** Bronze layer ingestion

**Why:** Bronze generally emphasizes faithful ingestion and traceability; deeper cleansing is typically performed downstream. Final aggregates belong in curated layers, and deduplication needs a business rule.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, C**

**Objective:** Bronze layer ingestion

**Why:** Bronze generally emphasizes faithful ingestion and traceability; deeper cleansing is typically performed downstream. Final aggregates belong in curated layers, and deduplication needs a business rule.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answer: **B**

**Objective:** Data quality profiling

**Why:** Null profiling should inform a documented quality rule; blindly replacing identifiers can corrupt relationships.

**Why the other options are incorrect:**
- A: Ignore all nulls because Spark does not support null values.
- C: Replace every null with the same arbitrary customer ID.
- D: Cast the identifier to a timestamp.

**Official documentation:** [https://docs.databricks.com/en/lakehouse/medallion.html](https://docs.databricks.com/en/lakehouse/medallion.html)

---

### Q5 — Correct answer: **B**

**Objective:** External tables

**Why:** File reads and table storage semantics are separate decisions. Managed/external behavior depends on table creation and location configuration.

**Why the other options are incorrect:**
- A: A DataFrame cannot read external files.
- C: Any table created from a DataFrame is automatically external.
- D: External tables never need governance.

**Official documentation:** [https://docs.databricks.com/en/tables/external.html](https://docs.databricks.com/en/tables/external.html)

---

## Section 07 — Data Engineering with Apache Spark – Silver Layer

### Q1 — Correct answers: **A, B, D**

**Objective:** Silver layer transformations

**Why:** Silver commonly standardizes and validates data; left joins preserve left-side rows; and explode expands array/map elements. dropDuplicates does not guarantee the newest record without explicit deterministic logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Silver layer transformations

**Why:** Silver commonly standardizes and validates data; left joins preserve left-side rows; and explode expands array/map elements. dropDuplicates does not guarantee the newest record without explicit deterministic logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Silver layer transformations

**Why:** Silver commonly standardizes and validates data; left joins preserve left-side rows; and explode expands array/map elements. dropDuplicates does not guarantee the newest record without explicit deterministic logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Silver layer transformations

**Why:** Silver commonly standardizes and validates data; left joins preserve left-side rows; and explode expands array/map elements. dropDuplicates does not guarantee the newest record without explicit deterministic logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Deterministic deduplication

**Why:** A window/ranking rule explicitly encodes which record should survive. Tie-breaking matters when timestamps can match.

**Why the other options are incorrect:**
- B: Call `dropDuplicates()` and assume Spark always keeps the newest record.
- C: Sort the display output after writing and assume the stored table changes.
- D: Use `union()` to remove duplicates.

**Official documentation:** [https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.row_number.html](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.row_number.html)

---

## Section 08 — Data Engineering with Apache Spark – Gold Layer

### Q1 — Correct answers: **A, B, D**

**Objective:** Gold layer modeling

**Why:** Gold data products provide curated metrics; join cardinality should be validated; and reusable products standardize definitions. Ratios need a well-defined denominator.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Gold layer modeling

**Why:** Gold data products provide curated metrics; join cardinality should be validated; and reusable products standardize definitions. Ratios need a well-defined denominator.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Gold layer modeling

**Why:** Gold data products provide curated metrics; join cardinality should be validated; and reusable products standardize definitions. Ratios need a well-defined denominator.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Gold layer modeling

**Why:** Gold data products provide curated metrics; join cardinality should be validated; and reusable products standardize definitions. Ratios need a well-defined denominator.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **B**

**Objective:** Gold data products

**Why:** Reusable curated data products help standardize metric definitions and reduce inconsistent duplicated transformations.

**Why the other options are incorrect:**
- A: It eliminates the need for governance and data quality.
- C: It guarantees every query is free.
- D: It prevents all future schema changes.

**Official documentation:** [https://docs.databricks.com/en/lakehouse/medallion.html](https://docs.databricks.com/en/lakehouse/medallion.html)

---

## Section 09 — Real-Time Data Processing with Spark Structured Streaming

### Q1 — Correct answers: **A, B, D**

**Objective:** Structured Streaming

**Why:** A query is started with a supported start operation; checkpoints support recovery; and foreachBatch supports per-micro-batch logic. End-to-end guarantees depend on sink semantics and implementation.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Structured Streaming

**Why:** A query is started with a supported start operation; checkpoints support recovery; and foreachBatch supports per-micro-batch logic. End-to-end guarantees depend on sink semantics and implementation.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Structured Streaming

**Why:** A query is started with a supported start operation; checkpoints support recovery; and foreachBatch supports per-micro-batch logic. End-to-end guarantees depend on sink semantics and implementation.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Structured Streaming

**Why:** A query is started with a supported start operation; checkpoints support recovery; and foreachBatch supports per-micro-batch logic. End-to-end guarantees depend on sink semantics and implementation.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **B**

**Objective:** Streaming monitoring

**Why:** Streaming progress metrics help isolate source throughput, processing bottlenecks, stateful work and sink performance.

**Why the other options are incorrect:**
- A: Delete the checkpoint immediately.
- C: Increase the number of columns displayed in the notebook.
- D: Assume the only possible cause is a bad SQL syntax.

**Official documentation:** [https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html)

---

## Section 10 — Scalable Data Ingestion with Databricks Auto Loader

### Q1 — Correct answers: **A, B, D**

**Objective:** Auto Loader

**Why:** Auto Loader uses cloudFiles, supports schema tracking, and supports streaming ingestion. Its incremental file-discovery model does not mean all prior files are reprocessed on every run.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Auto Loader

**Why:** Auto Loader uses cloudFiles, supports schema tracking, and supports streaming ingestion. Its incremental file-discovery model does not mean all prior files are reprocessed on every run.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

### Q3 — Correct answers: **A, B, D**

**Objective:** Auto Loader

**Why:** Auto Loader uses cloudFiles, supports schema tracking, and supports streaming ingestion. Its incremental file-discovery model does not mean all prior files are reprocessed on every run.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answer: **A**

**Objective:** Choosing an ingestion method

**Why:** Both can support incremental ingestion scenarios, but their discovery, schema handling and orchestration characteristics differ.

**Why the other options are incorrect:**
- B: Auto Loader and `COPY INTO` are identical in every respect.
- C: `COPY INTO` always reloads every file and cannot be incremental.
- D: Auto Loader is only for JDBC databases.

**Official documentation:** [https://docs.databricks.com/en/ingestion/](https://docs.databricks.com/en/ingestion/)

---

### Q5 — Correct answers: **A, B, D**

**Objective:** Auto Loader source, schema tracking, and streaming ingestion

**Why:** Auto Loader uses the `cloudFiles` source, can track schema information in a schema location, and supports streaming ingestion.

**Why the other option is incorrect:**
- C: Auto Loader incrementally discovers and processes new files; it is not designed to reprocess every previously discovered file on every run by default.

**Official documentation:** [What is Auto Loader?](https://docs.databricks.com/en/ingestion/cloud-object-storage/auto-loader/index.html)
## Section 11 — SQL-Based Data Ingestion with COPY INTO and Delta Lake

### Q1 — Correct answers: **A, C**

**Objective:** COPY INTO

**Why:** COPY INTO supports incremental file loading and its target/schema options affect parsing. It does not deduplicate arbitrary business keys, and it is not identical to Auto Loader in every behavior.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, C**

**Objective:** COPY INTO

**Why:** COPY INTO supports incremental file loading and its target/schema options affect parsing. It does not deduplicate arbitrary business keys, and it is not identical to Auto Loader in every behavior.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, C**

**Objective:** COPY INTO

**Why:** COPY INTO supports incremental file loading and its target/schema options affect parsing. It does not deduplicate arbitrary business keys, and it is not identical to Auto Loader in every behavior.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, C**

**Objective:** COPY INTO

**Why:** COPY INTO supports incremental file loading and its target/schema options affect parsing. It does not deduplicate arbitrary business keys, and it is not identical to Auto Loader in every behavior.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **B**

**Objective:** Ingestion method selection

**Why:** Choose based on workload requirements; avoid assuming identical schema evolution, file discovery, and checkpoint semantics.

**Why the other options are incorrect:**
- A: They are interchangeable APIs with identical checkpoint and schema behavior.
- C: Only Auto Loader can read files in cloud storage.
- D: Only `COPY INTO` can write to Delta.

**Official documentation:** [https://docs.databricks.com/en/ingestion/](https://docs.databricks.com/en/ingestion/)

---

## Section 12 — Analytics, Dashboards, and AI with Databricks SQL

### Q1 — Correct answers: **A, B, D**

**Objective:** Databricks SQL

**Why:** GROUP BY rules apply to non-aggregated columns; query profiles help diagnose performance; and dashboards, queries, and alerts are distinct objects. A filter does not grant source-table privileges.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Databricks SQL

**Why:** GROUP BY rules apply to non-aggregated columns; query profiles help diagnose performance; and dashboards, queries, and alerts are distinct objects. A filter does not grant source-table privileges.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Databricks SQL

**Why:** GROUP BY rules apply to non-aggregated columns; query profiles help diagnose performance; and dashboards, queries, and alerts are distinct objects. A filter does not grant source-table privileges.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Databricks SQL

**Why:** GROUP BY rules apply to non-aggregated columns; query profiles help diagnose performance; and dashboards, queries, and alerts are distinct objects. A filter does not grant source-table privileges.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **B**

**Objective:** SQL permissions

**Why:** A dashboard does not bypass source-table authorization; check data privileges and the required compute/warehouse access.

**Why the other options are incorrect:**
- A: The dashboard color palette.
- C: The table's file extension only.
- D: The number of notebook markdown cells.

**Official documentation:** [https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/)

---

## Section 13 — Lakeflow Connect- From Raw Data to Delta Tables

### Q1 — Correct answers: **A, B, D**

**Objective:** Lakeflow Connect

**Why:** Managed connectors can reduce operational work; source support must be checked; and source credentials/access are separate from destination governance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Lakeflow Connect

**Why:** Managed connectors can reduce operational work; source support must be checked; and source credentials/access are separate from destination governance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Lakeflow Connect

**Why:** Managed connectors can reduce operational work; source support must be checked; and source credentials/access are separate from destination governance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Lakeflow Connect

**Why:** Managed connectors can reduce operational work; source support must be checked; and source credentials/access are separate from destination governance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **B**

**Objective:** Secrets and credentials

**Why:** Credentials should be handled through supported secret/credential mechanisms and least-privilege access, not embedded in code or logs.

**Why the other options are incorrect:**
- A: Hard-code credentials into the notebook and restrict notebook sharing.
- C: Print credentials to `stdout` for debugging.
- D: Store credentials in a public Git branch.

**Official documentation:** [https://docs.databricks.com/en/security/secrets/](https://docs.databricks.com/en/security/secrets/)

---

## Section 14 — Advanced Lakeflow Jobs- Dynamic, Conditional & Data-Driven Pipelines

### Q1 — Correct answers: **A, B, D**

**Objective:** Lakeflow Jobs

**Why:** Jobs model task dependencies, allow retry configuration, and support multiple trigger types. Dependencies determine order; downstream tasks do not run before required upstream work.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Lakeflow Jobs

**Why:** Jobs model task dependencies, allow retry configuration, and support multiple trigger types. Dependencies determine order; downstream tasks do not run before required upstream work.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Lakeflow Jobs

**Why:** Jobs model task dependencies, allow retry configuration, and support multiple trigger types. Dependencies determine order; downstream tasks do not run before required upstream work.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A and C**

**Objective:** Lakeflow Jobs reliability and monitoring

**Why:** Retries can recover from transient errors, while suitable timeouts and monitoring help ensure persistent failures remain visible instead of being hidden.

**Why the other options are incorrect:**
- B: Excessive retries and falsely treating runs as successful can conceal persistent defects.
- D: Removing required dependencies can cause tasks to run in the wrong order.

**Official documentation:** [Configure and monitor Lakeflow Jobs](https://docs.databricks.com/en/jobs/index.html)
### Q5 — Correct answers: **A, B, D**

**Objective:** Lakeflow Jobs dependencies, retries, and triggers

**Why:** Job tasks can be connected through dependencies, tasks support retry configuration for eligible failures, and Jobs supports scheduled and data-driven trigger types.

**Why the other option is incorrect:**
- C: Dependencies determine execution order; a downstream task does not run before its required upstream task completes successfully.

**Official documentation:** [Lakeflow Jobs](https://docs.databricks.com/en/jobs/index.html)
## Section 15 — Introduction to Delta Live Tables and Lakeflow Pipelines

### Q1 — Correct answers: **A, C, D**

**Objective:** Lakeflow Declarative Pipelines

**Why:** Declarative pipelines define transformations and use framework-managed execution; logs help diagnose runtime issues; and legacy terminology may persist in course materials. Validation does not guarantee business-data correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, C, D**

**Objective:** Lakeflow Declarative Pipelines

**Why:** Declarative pipelines define transformations and use framework-managed execution; logs help diagnose runtime issues; and legacy terminology may persist in course materials. Validation does not guarantee business-data correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, C, D**

**Objective:** Lakeflow Declarative Pipelines

**Why:** Declarative pipelines define transformations and use framework-managed execution; logs help diagnose runtime issues; and legacy terminology may persist in course materials. Validation does not guarantee business-data correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, C, D**

**Objective:** Lakeflow Declarative Pipelines

**Why:** Declarative pipelines define transformations and use framework-managed execution; logs help diagnose runtime issues; and legacy terminology may persist in course materials. Validation does not guarantee business-data correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Schema evolution in pipelines

**Why:** Schema changes should be diagnosed through the configured schema behavior and pipeline logs, then handled deliberately.

**Why the other options are incorrect:**
- B: Only the notebook theme.
- C: Whether the SQL warehouse name has spaces.
- D: Whether the catalog has enough rows.

**Official documentation:** [https://docs.databricks.com/en/ldp/](https://docs.databricks.com/en/ldp/)

---

## Section 16 — Exploring the DLT Development Environment

### Q1 — Correct answers: **A, B, D**

**Objective:** Pipeline development environment

**Why:** Logs, environment-specific configuration, and upstream flow events are useful troubleshooting tools. Renaming a notebook does not automatically fix pipeline dependencies.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Pipeline development environment

**Why:** Logs, environment-specific configuration, and upstream flow events are useful troubleshooting tools. Renaming a notebook does not automatically fix pipeline dependencies.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Pipeline development environment

**Why:** Logs, environment-specific configuration, and upstream flow events are useful troubleshooting tools. Renaming a notebook does not automatically fix pipeline dependencies.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Pipeline development environment

**Why:** Logs, environment-specific configuration, and upstream flow events are useful troubleshooting tools. Renaming a notebook does not automatically fix pipeline dependencies.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Streaming tables and materialized views

**Why:** Streaming behavior is determined by the framework's supported dataset definitions and source semantics, not naming conventions.

**Why the other options are incorrect:**
- B: The table is stored in a folder named `streaming`.
- C: The dashboard has an auto-refresh checkbox.
- D: The schema contains a column called `stream`.

**Official documentation:** [https://docs.databricks.com/en/ldp/](https://docs.databricks.com/en/ldp/)

---

## Section 17 — Building and Running Your First DLT Pipeline

### Q1 — Correct answers: **A, B, D**

**Objective:** Running a pipeline

**Why:** Validate output schema/data, confirm target configuration, and choose quality actions deliberately. A successful run alone does not prove business correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Running a pipeline

**Why:** Validate output schema/data, confirm target configuration, and choose quality actions deliberately. A successful run alone does not prove business correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Running a pipeline

**Why:** Validate output schema/data, confirm target configuration, and choose quality actions deliberately. A successful run alone does not prove business correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Running a pipeline

**Why:** Validate output schema/data, confirm target configuration, and choose quality actions deliberately. A successful run alone does not prove business correctness.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Pipeline debugging

**Why:** Versioned code/config and run evidence help explain changed output; validate whether the change is intended.

**Why the other options are incorrect:**
- B: Compare only the notebook font.
- C: Assume Delta transaction logs are unrelated to all data changes.
- D: Rename the pipeline and rerun without review.

**Official documentation:** [https://docs.databricks.com/en/ldp/](https://docs.databricks.com/en/ldp/)

---

## Section 18 — Building Streaming Data Pipelines with Auto Loader

### Q1 — Correct answers: **A, B, D**

**Objective:** Auto Loader streaming pipelines

**Why:** Auto Loader incrementally discovers files; checkpoint deletion can affect recovery/replay; and source access/discovery/configuration should be checked for missing files. Schema changes do not guarantee downstream compatibility.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Auto Loader streaming pipelines

**Why:** Auto Loader incrementally discovers files; checkpoint deletion can affect recovery/replay; and source access/discovery/configuration should be checked for missing files. Schema changes do not guarantee downstream compatibility.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Auto Loader streaming pipelines

**Why:** Auto Loader incrementally discovers files; checkpoint deletion can affect recovery/replay; and source access/discovery/configuration should be checked for missing files. Schema changes do not guarantee downstream compatibility.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answer: **A**

**Objective:** Checkpoint recovery

**Why:** Checkpoint deletion is operationally significant; reset only with an understood replay strategy and sink behavior.

**Why the other options are incorrect:**
- B: Deleting a checkpoint only clears notebook output and has no effect on processing.
- C: The checkpoint contains the only copy of the source data.
- D: The checkpoint is a user interface preference.

**Official documentation:** [https://docs.databricks.com/en/structured-streaming/checkpoints.html](https://docs.databricks.com/en/structured-streaming/checkpoints.html)

---

### Q5 — Correct answer: **A**

**Objective:** Auto Loader and job triggers

**Why:** Available-now processing and file-arrival triggers can fit periodic or event-driven ingestion when supported by the chosen architecture.

**Why the other options are incorrect:**
- B: A permanent infinite stream is the only supported option.
- C: A dashboard alert can ingest files automatically.
- D: A table grant can schedule a job.

**Official documentation:** [https://docs.databricks.com/en/jobs/triggers.html](https://docs.databricks.com/en/jobs/triggers.html)

---

## Section 19 — Building Unified Streaming Tables with Append Flows

### Q1 — Correct answers: **A, B, D**

**Objective:** Git and bundles

**Why:** Commit and push are distinct; bundles support resource-as-code deployment; and explicit targets reduce environment mistakes. Bundle validation does not replace data-quality testing.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Git and bundles

**Why:** Commit and push are distinct; bundles support resource-as-code deployment; and explicit targets reduce environment mistakes. Bundle validation does not replace data-quality testing.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Git and bundles

**Why:** Commit and push are distinct; bundles support resource-as-code deployment; and explicit targets reduce environment mistakes. Bundle validation does not replace data-quality testing.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Git and bundles

**Why:** Commit and push are distinct; bundles support resource-as-code deployment; and explicit targets reduce environment mistakes. Bundle validation does not replace data-quality testing.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Bundle deployment targets

**Why:** Explicit targets and reviewed overrides reduce the risk of deploying to the wrong environment.

**Why the other options are incorrect:**
- B: Assume the CLI infers the target from the current notebook.
- C: Use one shared hard-coded catalog for all environments.
- D: Disable validation to avoid warnings.

**Official documentation:** [https://docs.databricks.com/en/dev-tools/bundles/settings.html](https://docs.databricks.com/en/dev-tools/bundles/settings.html)

---

## Section 20 — Change Data Capture with Auto CDC Flow

### Q1 — Correct answers: **A, B, D**

**Objective:** Spark performance troubleshooting

**Why:** Skew, spilling, and stage/task metrics are useful performance clues. Broadcasting every table is not appropriate regardless of size.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Spark performance troubleshooting

**Why:** Skew, spilling, and stage/task metrics are useful performance clues. Broadcasting every table is not appropriate regardless of size.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Spark performance troubleshooting

**Why:** Skew, spilling, and stage/task metrics are useful performance clues. Broadcasting every table is not appropriate regardless of size.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Spark performance troubleshooting

**Why:** Skew, spilling, and stage/task metrics are useful performance clues. Broadcasting every table is not appropriate regardless of size.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Compute troubleshooting

**Why:** Startup and library failures are usually diagnosed through event logs, runtime compatibility and dependency isolation, not data transformations.

**Why the other options are incorrect:**
- B: Delete all tables and checkpoints.
- C: Assume the source data contains duplicates.
- D: Change every table to external.

**Official documentation:** [https://docs.databricks.com/en/compute/troubleshooting/](https://docs.databricks.com/en/compute/troubleshooting/)

---

## Section 21 — Managing Slowly Changing Dimensions Type 1

### Q1 — Correct answers: **A, B, D**

**Objective:** Delta Sharing and Federation

**Why:** Delta Sharing and Federation address different patterns; federation depends on supported sources and connector performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Delta Sharing and Federation

**Why:** Delta Sharing and Federation address different patterns; federation depends on supported sources and connector performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Delta Sharing and Federation

**Why:** Delta Sharing and Federation address different patterns; federation depends on supported sources and connector performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Delta Sharing and Federation

**Why:** Delta Sharing and Federation address different patterns; federation depends on supported sources and connector performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Delta Sharing governance

**Why:** Data sharing requires deliberate recipient and data access configuration and remains a governance responsibility.

**Why the other options are incorrect:**
- B: All shared data becomes public by default.
- C: Sharing disables auditing.
- D: Every recipient receives workspace-admin rights.

**Official documentation:** [https://docs.databricks.com/en/delta-sharing/](https://docs.databricks.com/en/delta-sharing/)

---

## Section 22 — Managing Slowly Changing Dimensions Type 2

### Q1 — Correct answers: **A, B, D**

**Objective:** Streaming guarantees and governance

**Why:** Streaming guarantees depend on the whole pipeline; row/column policies are governance controls; and ABAC uses supported attributes/context. Checkpointing alone cannot guarantee every external side effect.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Streaming guarantees and governance

**Why:** Streaming guarantees depend on the whole pipeline; row/column policies are governance controls; and ABAC uses supported attributes/context. Checkpointing alone cannot guarantee every external side effect.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Streaming guarantees and governance

**Why:** Streaming guarantees depend on the whole pipeline; row/column policies are governance controls; and ABAC uses supported attributes/context. Checkpointing alone cannot guarantee every external side effect.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answer: **A**

**Objective:** Unity Catalog privileges

**Why:** Creation, namespace usage, ownership, and read privileges are distinct concepts; diagnose the effective permissions.

**Why the other options are incorrect:**
- B: Assume create permission always includes all privileges forever.
- C: Disable Unity Catalog.
- D: Use `OPTIMIZE` to grant access.

**Official documentation:** [https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/)

---

### Q5 — Correct answer: **A**

**Objective:** Unity Catalog assets

**Why:** Unity Catalog supports governance across multiple asset types and architectures; exact controls depend on the asset type and configuration.

**Why the other options are incorrect:**
- B: Yes; Unity Catalog governs only notebook outputs.
- C: Yes; external tables and volumes are never governed.
- D: No; governance is unnecessary if files are in cloud storage.

**Official documentation:** [https://docs.databricks.com/en/data-governance/unity-catalog/](https://docs.databricks.com/en/data-governance/unity-catalog/)

---

## Section 23 — Ensuring Data Quality in Delta Live Tables

### Q1 — Correct answers: **A, B, D**

**Objective:** Data quality expectations

**Why:** Expectations encode conditions; configured actions may warn or drop; and checks reveal business-rule violations. Repair requires explicit transformation logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Data quality expectations

**Why:** Expectations encode conditions; configured actions may warn or drop; and checks reveal business-rule violations. Repair requires explicit transformation logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Data quality expectations

**Why:** Expectations encode conditions; configured actions may warn or drop; and checks reveal business-rule violations. Repair requires explicit transformation logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Data quality expectations

**Why:** Expectations encode conditions; configured actions may warn or drop; and checks reveal business-rule violations. Repair requires explicit transformation logic.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answers: **A, B, D**

**Objective:** Data quality expectations

**Why:** Expectations express data-quality conditions. Depending on the action configured, invalid records can be recorded as violations or dropped, and checks help identify records that break business rules.

**Why the other option is incorrect:**
- C: Expectations do not automatically fix invalid values; remediation requires appropriate transformation logic.

**Official documentation:** [Manage data quality with pipeline expectations](https://docs.databricks.com/en/delta-live-tables/expectations.html)
## Section 24 — Building Dynamic and Parameterized DLT Pipelines

### Q1 — Correct answers: **A, B, D**

**Objective:** Bundle deployment and CI/CD

**Why:** Explicit settings, validation plus testing, and least privilege improve release safety. Secrets should not be committed in plain text.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Bundle deployment and CI/CD

**Why:** Explicit settings, validation plus testing, and least privilege improve release safety. Secrets should not be committed in plain text.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Bundle deployment and CI/CD

**Why:** Explicit settings, validation plus testing, and least privilege improve release safety. Secrets should not be committed in plain text.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Bundle deployment and CI/CD

**Why:** Explicit settings, validation plus testing, and least privilege improve release safety. Secrets should not be committed in plain text.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q5 — Correct answer: **A**

**Objective:** Deployment governance

**Why:** Least-privilege deployment permissions and reviewed release workflows reduce accidental or unauthorized production changes.

**Why the other options are incorrect:**
- B: Give every developer account admin rights.
- C: Disable Git history.
- D: Store the production token in a shared notebook.

**Official documentation:** [https://docs.databricks.com/en/dev-tools/bundles/](https://docs.databricks.com/en/dev-tools/bundles/)

---

## Section 25 — Recent Updates in Lakeflow Declarative Pipelines

### Q1 — Correct answers: **A, B, D**

**Objective:** Optimization and troubleshooting

**Why:** Optimization should be evidence-based; Spark UI helps diagnose execution issues; and startup failures require log/configuration investigation. Notebook cell count does not inherently improve performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q2 — Correct answers: **A, B, D**

**Objective:** Optimization and troubleshooting

**Why:** Optimization should be evidence-based; Spark UI helps diagnose execution issues; and startup failures require log/configuration investigation. Notebook cell count does not inherently improve performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q3 — Correct answers: **A, B, D**

**Objective:** Optimization and troubleshooting

**Why:** Optimization should be evidence-based; Spark UI helps diagnose execution issues; and startup failures require log/configuration investigation. Notebook cell count does not inherently improve performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

---

### Q4 — Correct answers: **A, B, D**

**Objective:** Optimization and troubleshooting

**Why:** Optimization should be evidence-based; Spark UI helps diagnose execution issues; and startup failures require log/configuration investigation. Notebook cell count does not inherently improve performance.

**Official documentation:** [Databricks documentation](https://docs.databricks.com/en/)

### Q5 — Correct answer: **A**

**Objective:** Spark SQL performance

**Why:** Optimization should target the observed bottleneck; filtering, join strategy, skew mitigation and resources can help depending on evidence.

**Why the other options are incorrect:**
- B: Immediately disable the transaction log.
- C: Always cache every DataFrame permanently.
- D: Assume adding more notebook cells will reduce spills.

**Official documentation:** [https://spark.apache.org/docs/latest/sql-performance-tuning.html](https://spark.apache.org/docs/latest/sql-performance-tuning.html)

---

## Final reminder

These questions are original practice material. They are not actual Databricks exam questions, and the number of questions per course section does not represent official exam weighting. For version-sensitive details, the applicable official exam guide and current documentation take precedence over course videos or candidate reports.
