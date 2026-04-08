# Warehouse Cost Advisor

Python analytics project for query cost analysis. It packages a small but reviewable workflow with deterministic scoring, JSON outputs, and unit tests.

## What It Shows

- warehouse optimization, compute attribution, and savings recommendations
- clear ingestion and summarization logic
- CLI entrypoint and test coverage

## Run

```bash
python -m src.analyzer --input data/queries.ndjson --output out/report.json
```

## Test

```bash
python -m unittest discover -s tests
```
