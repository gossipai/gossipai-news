def create_request_body(sources, apiKey, languages=["eng","tur"], types=["news","blog"]):

    request_body = {
        "query": {
            "$query": {
                "$and": [
                    {
                        "$or": [{"sourceUri":source} for source in sources]
                    },
                    {
                        "$or": [{"lang":language} for language in languages]
                    }
                ]
            },
            "$filter": {
                "dataType": types,
                "isDuplicate": "skipDuplicates"
            }
        },
        "apiKey": apiKey
    }

    return request_body