# wghh-zensus-api

A simple [flask](http://flask.pocoo.org/) app that serves an api endpoint to
obtain flats ownership statistics for addresses in Hamburg, Germany.

It uses [Nominatim](https://nominatim.openstreetmap.org/) as a geocoder and
then looks into the database to find some insights.

## install

    pip install -r requirements.txt

## run

    FLASK_APP=app.py flask run

this will fire up a local webserver at [127.0.0.1:5000](http://127.0.0.1:500)

## query

just give an address via the `q` parameter as a `GET` request. You will get
back a `json` dictionary with the key `data` that is either `null` or full of
data.

### example

Query for "Bornbachstieg 2":

[http://127.0.0.1:5000/?q=Bornbachstieg%202](http://127.0.0.1:5000/?q=Bornbachstieg%202)

the result:

```json
{
  "data": {
    "flats_cooperative_owned": 21,
    "flats_cooperative_owned_q": 52,
    "flats_ngo_church_owned": 0,
    "flats_ngo_church_owned_q": 0,
    "flats_other_private_company_owned": 0,
    "flats_other_private_company_owned_q": 0,
    "flats_private_company_owned": 15,
    "flats_private_company_owned_q": 37,
    "flats_private_owned": 0,
    "flats_private_owned_q": 0,
    "flats_public_body_owned": 4,
    "flats_public_body_owned_q": 10,
    "flats_state_owned": 0,
    "flats_state_owned_q": 0,
    "flats_total": 40,
    "id": "100mN33967E43231"
  }
}
```
