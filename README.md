## Databricks Certified Data Engineer Associate Cert. Prep Projects

https://www.udemy.com/course/databricks-certified-data-engineer-associate-cert-prep/
https://www.reddit.com/r/databricks/comments/1r5vcnb/cleared_databricks_data_engineer_associate_here/

Extract udemy course transscripts: [chromewebstore.google.com/detail/udemy-transcript-extracto/oimlbilmdnimabebeilpndlndfoepopd](https://chromewebstore.google.com/detail/udemy-transcript-extracto/oimlbilmdnimabebeilpndlndfoepopd)
Master Databricks, Spark, Delta Lake, DLT, Lakeflow, SQL, ETL pipelines. Become databricks certified associate developer

### The lecture outlines the structure and key topics of the Databricks Certified Data Engineer Associate exam, which consists of 45 multiple-choice questions, lasts 90 minutes, and typically requires a passing score of 70-75%. The content is divided into seven sections:

1. **Databricks Intelligence Platform (6%)** : Focus on architecture and key components like Delta Lake and Unity Catalog.
2. **Data Ingestion and Loading (21%)** : Methods such as batch, streaming, and incremental ingestion, along with tools like Lakeflow Connect and JDBC.
3. **Data Transformation and Modeling (22%)** : The largest section, emphasizing data cleaning, transformations, and performance settings using PySpark and SQL.
4. **Working with Lakeflow Jobs (16%)** : Covers pipeline orchestration and task management.
5. **Implementing CI and CD (10%)** : Discusses Git integration and environment management.
6. **Troubleshooting, Monitoring, and Optimization (10%)** : Focuses on job performance tracking and optimization techniques.
7. **Governance and Security (15%)** : Involves user management, security policies, and data governance practices.

### Tech list

Delta Lake : Provides reliable data storage with ACID transactions and data consistency.

Auto Loader : Incrementally ingests new files as they arrive in cloud storage.

Delta Live Tables : A former name for Databricks declarative pipeline capabilities; now associated with Lakeflow Spark Declarative Pipelines.

Unity Catalog : Centralized data governance, permissions, and discovery.

SQL and dashboards : Support querying, analysis, and business reporting.

# Databricks Menu Summary

| Category         | Menu             | Purpose                                         |
| ---------------- | ---------------- | ----------------------------------------------- |
| Main             | New              | Create new resources                            |
|                  | Home             | Main landing page                               |
|                  | Learn            | Tutorials and learning materials                |
|                  | Workspace        | Manage notebooks and files                      |
|                  | Recents          | Access recently used items                      |
|                  | Catalog          | Browse and govern data assets                   |
|                  | Jobs & Pipelines | Schedule and orchestrate workflows              |
|                  | Compute          | Manage compute resources                        |
|                  | Discover         | Explore data and platform features              |
|                  | Marketplace      | Find shared datasets and solutions              |
| SQL              | SQL Editor       | Write and execute SQL queries                   |
|                  | Queries          | Save and manage SQL queries                     |
|                  | Dashboards       | Visualize data using charts and tables          |
|                  | Genie Agents     | Ask natural-language questions and generate SQL |
|                  | Alerts           | Notify users when query conditions are met      |
|                  | Query History    | Review executed queries                         |
|                  | SQL Warehouses   | Provide compute for SQL workloads               |
| Data Engineering | Runs             | Monitor job and pipeline executions             |
|                  | Data Ingestion   | Import data from external sources               |
|                  | Visual Data Prep | Clean and transform data visually               |
| AI/ML            | Playground       | Experiment with AI models and prompts           |
|                  | Agents           | Build AI agents to perform tasks                |
|                  | AI Gateway       | Govern and manage AI model access               |
|                  | Experiments      | Track machine learning experiments              |
|                  | Features         | Manage ML features                              |
|                  | Models           | Manage registered ML models                     |
|                  | Serving          | Deploy models and AI applications               |

## Databricks Architecture

```text
                    DATABRICKS ARCHITECTURE
                              |
             +----------------+----------------+
             |                                 |
      CONTROL PLANE                     COMPUTE PLANE
      (Management / Brain)              (Processing / Muscle)
             |                                 |
      - Web UI / Workspace              +------+------+
      - Cluster management              |             |
      - Security & access          CLASSIC       SERVERLESS
      - Unity Catalog*               COMPUTE       COMPUTE
      - Job / notebook metadata         |             |
             |                    User's cloud   Databricks'
             |                    account         cloud account
             |                    (Azure/AWS/GCP) |
             |                          |         |
             |                    User manages   Databricks
             |                    infrastructure manages
             |                          |         |
             +--------------------------+---------+
                                        |
                                 DATA PROCESSING
                                 - Spark jobs
                                 - SQL queries
                                 - Filtering / aggregation
                                        |
                                  CLOUD STORAGE
                                  - Business data
                                  - Tables / files
                                  - Logs and metadata
```

### Key Concepts

| Component          | Purpose                                                                   |
| ------------------ | ------------------------------------------------------------------------- |
| Control plane      | Manages the workspace, orchestration, configuration, and access controls. |
| Compute plane      | Executes Spark jobs, SQL queries, and data transformations.               |
| Classic compute    | Compute resources run in the customer's cloud environment.                |
| Serverless compute | Databricks manages the underlying compute infrastructure.                 |
| Storage            | Holds business data, tables, files, and relevant system data.             |

### Exam Memory Tips

- **Control plane = Brain** → management and coordination.
- **Compute plane = Muscle** → executes processing.
- **Classic = Your car** → resources in your cloud environment.
- **Serverless = Taxi** → Databricks manages the infrastructure.
- **Storage = Warehouse** → persists data and files.

*Note: Unity Catalog is a governance service managed through the control plane, while data access and enforcement can also involve compute and storage components. Databricks system storage and customer data storage are not necessarily the same location.*
