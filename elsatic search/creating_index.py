from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

print(es.info())

index_name = "elasticsearch"
index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "field1": {"type": "text"},
            "field2": {"type": "keyword"}
           
        }
    }
}
response = es.indices.create(index=index_name, body=index_settings)

if response['acknowledged']:
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Failed to create index '{index_name}'.")