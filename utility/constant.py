class Constant:
    service = "email-notification-service"
    local_port = "5018"
    frontend_port = "5173"


    email = {
        "ACCOUNT_VERIFICATION": {
            "FROM_EMAIL": "admin@cloudneuros.com",
            "SUBJECT": "CloudNeuros Account Verification",
            "ENDPOINT": "/user/account/verify"

        }
        
    }
    base_url = "http://localhost:"
    dao_port = "5010"

    dao = {
        "create": "/api/create",
        "read": "/api/read",
        "list": "/api/read_list",
        "update": "/api/update",
        "delete": "/api/delete",
        "read_all": "/api/read_all",
        "query": "/api/query"
    }

    table = {
        "DATASTORE": "datastore",
        "DATASTORE_ROLES": "datastore_roles",
        "DATASET": "dataset",
        "DATASET_ROLES": "dataset_roles",
        "FILES": "files",
        "DATASTORE_CONFIG": "datastore_config",
        "DATASET_FILES": "dataset_files",
    }

