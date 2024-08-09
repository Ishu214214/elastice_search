from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

index_name = "elasticsearch"
query = {
    "query" : {
        "match_all" : {}
    }
}

results = es.search(index=index_name, body=query)
print(results)
 
