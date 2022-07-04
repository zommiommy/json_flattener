2 script, uploader + servizio

```
./payload_uploader.py -s ./settings.json ENDPOINT -- "a:[]" "a:1" "a:2" "a:3"
```

{   
    "log_level":"info", # solo stdout va bene
    "mysql":{

    },
    "endpoints":{
        "endpoint1":{
            "method":"POST",
            "cookies":"cookies",
            "url:"url",
            "user":"user",
            "password":"password",
            "verify_ssl":false,
            "timeout":60,
            "retry_count":10, # -1 infinito, 0 provo e se non va' non e' un problema
            "ordered":false,
        },
    }
}

schema
```
id, timestamp, status, endpoint, json_payload
```

status = {new, locked, failed, success}

unit con restart, il servizio ha un parametro di sleep tra le call,esce solo in errore
e systemd lo riavvia da solo