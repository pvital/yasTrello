# yasTrello
yet another simple Trello app

Simple Python program to add a Trello card with labels and a comment to a
specified X column of board Y.

## Trello API Key and Token

To be able to submit requests to Trello API, it is necessary to create an API
key to authentication and authorization. You can get your API key by logging
into Trello and visiting https://trello.com/app-key. Your API key should be 32
character string comprised of random alphanumeric characters.

It is also necessary an API token to be able to make requests. Trello uses a
delegated authentication and authorization flow, so the application never
has to deal with storing or handling usernames or passwords. Instead, this
application passes control to Trello (identifying itself via the API key) and
once Trello has allowed the user to choose an account and sign in, Trello will
hand the user and control back to your application, along with an API Token.

On the same page where you found your API key (https://trello.com/app-key), you
should see a section below the key that reads:

```
Most developers will need to ask each user to __authorize__ your application.
If you are looking to build an application for yourself, or are doing local
testing, you can manually generate a __Token__.
```

Follow the process and get the API key and API Token strings. Since this token 
can be used to access all of your Trello account so keep it safe! Because of
this, this app stores in a simple way both values in a file following JSON
syntax. This file should be stored in the yastrello directory and named as
"api_credentials.json" and following the pattern:

```
{
    "api_key": "<API KEY STRING>",
    "token": "<API TOKEN STRING>"
}
```

Without that, you are not able to connect Trello API and submit requests.
