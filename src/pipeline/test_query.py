from src.pipeline.query_engine import QueryEngine

engine = QueryEngine()

query = "UPI transaction limits"

results = engine.search(query)

for r in results:
    print("\n---\n")
    print(r)