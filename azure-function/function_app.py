import azure.functions as func
import logging

secret = "abc123asdf3456"
# https://abc_git:$passwordstoredasvariable@github.com/terraform-modules/infra.git
credit_card = "1234 5678 9012 3456"

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="thanh_http_trigger_azure_func")
def thanh_http_trigger_azure_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. The secr is {secret}.  This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
