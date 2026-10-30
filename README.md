# Backend integrations and ETL samples

These are small, runnable examples based on the types of backend and data engineering work I do: API integrations, pagination, data cleanup, SQL transformations, and source-to-target validation.

The examples use **made-up records**. They are not copies of production systems or institutional code. There are no real credentials, hostnames, report IDs, employee records, or student records here.

## Projects

- **api_integration/** — Python REST client with token-based authentication, pagination, field allowlisting, and CSV export. Mock mode works without external services.
- **book_adoption/** — Python CSV ETL that combines two synthetic bookstore feeds, fixes a composite course reference, maps term codes, keeps book identifiers as strings, and loads SQLite for a working local demo.
- **sql/** — SQL Server schema and transactional correction for malformed course references.
- **sas/** — SAS demonstration of parsing compound course references with dummy data.

## Run

Python 3.10+ recommended.

```bash
python -m unittest discover -s tests -v
python -m api_integration.extract_report --mock --output /tmp/sample_report.csv
python -m book_adoption.etl --db /tmp/book_adoption_demo.sqlite
```

Live API configuration uses environment variables: `API_BASE_URL`, `API_TENANT_ID`, `API_KEY`, and `API_REPORT_ID`. No production settings are included. A live API connection and SQL Server deployment have **not** been verified.

## Privacy and boundaries

Only synthetic data is checked in. API output uses an explicit set of allowed fields, so unrecognized data — including personal information — is not exported. These samples are independent portfolio examples, not production deployments.
